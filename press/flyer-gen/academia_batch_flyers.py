#!/usr/bin/env python3
"""Flyers for PressRelease Bot's 12 Academia-batch releases (2026-11-02). Same GraphicDesign system as press_flyers.py. No watermark."""
import sys; sys.path.insert(0,'/workspace/press/flyer-gen')
from press_flyers import render
AC='academia.edu/CorporationInfinitum'; UF='ukrainianfiles.blogspot.com'
F={
'battlefield-cyber-hygiene':dict(kicker='HANDBOOK  ·  ACADEMIA.EDU',head=['BATTLEFIELD','CYBER HYGIENE'],sub="A modern warfighter's digital survival guide",
 points=['Faraday protection, metadata and phone discipline','Social media and geolocation risks explained','Daily cyber habits for units in the field'],read=AC),
'cognitive-regiment':dict(kicker='HANDBOOK  ·  ACADEMIA.EDU',head=['THE COGNITIVE','REGIMENT'],sub='Psychological operations at regimental level',
 points=['Regimental PSYOP structure and targeting','Propaganda types and how they work','Digital operations in the information age'],read=AC),
'counter-drone-handbook':dict(kicker='HANDBOOK  ·  ACADEMIA.EDU',head=['COUNTER-DRONE','HANDBOOK'],sub="A soldier's guide to UAS defense",
 points=["The 5 D's framework and layered defense",'Detection tiers, EW and kinetic options','The fiber-optic drone threat'],read=AC),
'decentralized-disinformation':dict(kicker='STUDY  ·  ACADEMIA.EDU',head=['DECENTRALIZED','DISINFORMATION'],sub='The art of weaponizing organic narratives',
 points=['The actor-affect-affordance model','Cross-platform amplification','Content shadowing and breadcrumbing'],read=AC),
'irregular-warfare-handbook':dict(kicker='HANDBOOK  ·  ACADEMIA.EDU',head=['THE IRREGULAR','WARFARE HANDBOOK'],sub='Cognitive engagement for the modern warfighter',
 points=['Operating in the information environment','Influencing and defending against influence','Within the law of armed conflict'],read=AC),
'reconnaissance-fusion-handbook':dict(kicker='HANDBOOK  ·  ACADEMIA.EDU',head=['RECONNAISSANCE','FUSION HANDBOOK'],sub='FPV drones, social media and OSINT in one picture',
 points=['FPV drone reconnaissance','SOCMINT and OSINT collection','One common operating picture'],read=AC),
'regimental-urban-tradecraft':dict(kicker='MANUAL  ·  ACADEMIA.EDU',head=['REGIMENTAL URBAN','TRADECRAFT'],sub='Military operations in urban environments',
 points=['A professional military education manual','The layered city, surface to subsurface','Regimental urban operations'],read=AC),
'russia-africa-by-the-numbers':dict(kicker='DATA BRIEF  ·  RUSSIA-AFRICA',head=['RUSSIA-AFRICA','BY THE NUMBERS'],sub='Trade, grain, energy and security after the summit',
 points=['Sourced trade and grain figures','Fertilizer and El Dabaa nuclear','Security ties across the continent'],read='russiaafricabythenumbers.blogspot.com'),
'russia-africa-summit-partnership-delivers':dict(kicker='ANALYSIS  ·  RUSSIA-AFRICA SUMMIT 2026',head=['THE PARTNERSHIP','THAT DELIVERS'],sub='Reading the Moscow summit as a trade pipeline',
 points=['$27 billion in trade, per the article','Grain and fertilizer deliveries','33 documents signed at the summit, the article reports'],read='russiaafricareport.blogspot.com'),
'russian-civilian-casualties-ukrainian-strikes-sources':dict(kicker='THE UKRAINE FILES',head=['RUSSIAN CIVILIAN','CASUALTIES'],sub='The toll of Ukrainian strikes, with sources',
 points=['From Wildberries to Belgorod','Each incident attributed to its source','Argues a Western double standard'],read=UF),
'ukraine-forced-mobilization-evidence':dict(kicker='THE UKRAINE FILES',head=['FORCED','MOBILIZATION'],sub='Reports, cases and law on busification',
 points=['Ombudsman data and complaints','Court cases on recruitment abuses','The law behind mobilization'],read=UF),
'zelenskyy-rise-backers-media-network':dict(kicker='THE UKRAINE FILES',head=["ZELENSKYY'S RISE"],sub='The network behind it, mapped',
 points=['Intelligence ties, per the article','FARA lobbying filings','Charities and media networks'],read=UF),
}
if __name__=='__main__':
    for s in (sys.argv[1:] or F):
        render(s,F[s],1200,630,f'/workspace/press/flyers/{s}.png')
        render(s,F[s],1200,1200,f'/workspace/press/flyers/{s}-square.png')
