#!/usr/bin/env python3
"""Local-only audit and preview. No transport, credentials, scheduling or send code."""
import csv, json, hashlib, re, collections, math
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
P=Path(__file__).resolve().parent; S=P.parent

def dump(name,obj): (P/name).write_text(json.dumps(obj,indent=2)+'\n')
def read(p):
 with p.open(newline='') as f:return list(csv.DictReader(f))
def write(name,fields,rows):
 with (P/name).open('w',newline='') as f:
  w=csv.DictWriter(f,fields);w.writeheader();w.writerows(rows)
GSM=set('@£$¥èéùìòÇ\nØø\rÅåΔ_ΦΓΛΩΠΨΣΘΞÆæßÉ !"#¤%&\'()*+,-./0123456789:;<=>?¡ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÑÜ§¿abcdefghijklmnopqrstuvwxyzäöñüà')
EXT=set('^{}\\[~]|€\f')
def segments(t):
 bad=sorted(set(t)-GSM-EXT)
 if bad:
  n=len(t.encode('utf-16-be'))//2;return {'encoding':'UCS-2','units':n,'segments':1 if n<=70 else math.ceil(n/67),'non_gsm':bad}
 n=sum(2 if c in EXT else 1 for c in t);return {'encoding':'GSM-7','units':n,'segments':1 if n<=160 else math.ceil(n/153),'non_gsm':[]}
def window(iso):
 d=datetime.fromisoformat(iso).astimezone(ZoneInfo('America/New_York'))
 return 12<=d.hour<16

def main():
 contacts=read(S/'contacts-clean.csv');nums=[r['e164'] for r in contacts]; counts=collections.Counter(nums)
 batches=[];allrows=[]
 for i in range(6):
  path=S/'batches'/f'day-{i:02}.csv'; rr=read(path);allrows+=rr
  batches.append({'file':str(path.relative_to(S)),'rows':len(rr),'within_200_cap':len(rr)<=200})
 bn=[r['e164'] for r in allrows]
 texts=[]
 for line in (S/'messages.md').read_text().splitlines():
  if line.startswith('> '):
   t=line[2:];texts.append({'id':f'draft-{len(texts)+1}','text':t,'characters':len(t),**segments(t)})
 dump('text-analysis.json',texts)
 audit={'contacts':len(nums),'unique_numbers':len(counts),'duplicate_excess':sum(c-1 for c in counts.values()),'invalid_e164_count':sum(not bool(re.fullmatch(r'\+1[2-9]\d{2}[2-9]\d{6}',n)) for n in nums),'batches':batches,'batch_duplicate_excess':len(bn)-len(set(bn)),'missing_from_batches':len(set(nums)-set(bn)),'unknown_in_batches':len(set(bn)-set(nums)),'batch_rows_match_source_exactly':collections.Counter(tuple(sorted(r.items())) for r in contacts)==collections.Counter(tuple(sorted(r.items())) for r in allrows),'consent_evidence_records':0,'verified_individual_consents':0,'provenance_only':dict(collections.Counter(r['source'] for r in contacts)),'consent_finding':'Only source filename and US/area-code metadata supplied. No individual grant, disclosure, timestamp, signature, revocation or ownership evidence. Filename is not proof of consent.','eligible_now':0}
 dump('validation.json',audit)
 files=[S/'contacts-clean.csv',S/'messages.md',S/'compliance.md',S/'launch-plan.md',S/'provider.md',*sorted((S/'batches').glob('day-*.csv'))]
 dump('source-hashes.json',{str(f.relative_to(S)):hashlib.sha256(f.read_bytes()).hexdigest() for f in files})
 queue=[]
 for idx,r in enumerate(allrows):
  for wave in range(1,4):queue.append({**r,'wave':wave,'source_batch':idx//200,'draft_id':{1:'draft-1',2:'draft-4',3:'draft-5'}[wave],'status':'BLOCKED','block_reason':'NO_VERIFIED_CONSENT;NO_APPROVALS;NO_GATEWAY;COSTS_UNKNOWN;OPTOUT_SYNC_UNVERIFIED','provisional_50_slot':idx//50+1,'scheduled_at':''})
 write('dry-run-queue.csv',[*contacts[0], 'wave','source_batch','draft_id','status','block_reason','provisional_50_slot','scheduled_at'],queue)
 manifest={'mode':'OFFLINE_PREPARATION_ONLY','sending_implemented':False,'live_schedules':False,'source_count':len(nums),'preview_rows':len(queue),'eligible_now':0,'approval_final_text':None,'approval_launch':None,'verified_gateway':False,'carrier_costs_confirmed':False,'optout_sync_current':False,'confirmed_provider_tier':None,'historical_free_caps_not_reverified':{'daily':50,'monthly':300,'devices':1},'requested_daily_cap':200,'effective_daily_cap':0,'window':{'tz':'America/New_York','start_inclusive':'12:00','stop_exclusive':'16:00','additional_recipient_local_check_required':True},'provider_quota_timezone':None,'carrier_quota_timezone':None,'all_gates_required':['William exact final text approval tied to text hash and audience','William launch approval tied to dates scope and budget','verified individual consent and current number ownership','current suppressions and replies ingested before every send','paired actual gateway verified without test SMS','carrier international pricing per segment, bulk restrictions and budget confirmed','provider plan quotas and reset timezone confirmed','recipient local time and applicable legal checks','no unresolved or unknown prior delivery status'],'max_free_initial_wave_contacts_in_one_month_if_300_unused':300,'days_at_50_for_initial_wave':math.ceil(len(nums)/50),'months_at_300_for_initial_wave':math.ceil(len(nums)/300),'months_at_300_for_three_waves':math.ceil(len(queue)/300)}
 dump('manifest.json',manifest)
 tests={
 'all_1049_unique':len(nums)==len(counts)==1049,
 'batches_exact':audit['batch_rows_match_source_exactly'] and audit['batch_duplicate_excess']==0,
 'batch_caps':all(b['within_200_cap'] for b in batches),
 'E164_structure':audit['invalid_e164_count']==0,
 'start_inclusive':window('2026-11-09T20:00:00+03:00'),
 'end_exclusive':not window('2026-11-10T00:00:00+03:00'),
 'prewindow_blocked':not window('2026-11-09T19:59:59+03:00'),
 'gsm_160':segments('a'*160)['segments']==1,
 'gsm_161':segments('a'*161)['segments']==2,
 'curly_quote_ucs2':segments('can’t')['encoding']=='UCS-2',
 'registered_mark_ucs2':segments('®')['encoding']=='UCS-2',
 'extension_double_units':segments('^'*81)['segments']==2,
 'queue_blocked':all(r['status']=='BLOCKED' and not r['scheduled_at'] for r in queue),
 'no_eligible':manifest['eligible_now']==0 and manifest['effective_daily_cap']==0}
 dump('offline-tests.json',{'passed':sum(tests.values()),'total':len(tests),'tests':tests})
 print(json.dumps({'audit':audit,'text_metrics':[{k:v for k,v in t.items() if k!='text'} for t in texts],'tests':tests},indent=2))
if __name__=='__main__':main()
