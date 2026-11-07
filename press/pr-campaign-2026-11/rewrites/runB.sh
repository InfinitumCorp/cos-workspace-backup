#!/bin/bash
cd /workspace/press/pr-campaign-2026-11/rewrites
for s in russia-sanctions-analysis russias-economy-under-sanctions zelenskyys-rise ukraine-aid-ngos ukraine-forced-mobilization russian-civilian-casualties polish-supermarket russia-state-guided-capitalism media-double-standard legitimate-military-targets ukraine-foreign-fighters azov; do
  out=$(python3 submit_pl.py $s 2>&1); echo "$(date '+%H:%M') $out" | tee -a runB.log
  if ! echo "$out" | grep -q "PUBLISH 200.*edit/" ; then echo "STOP: non-success on $s" | tee -a runB.log; exit 1; fi
  if echo "$out" | grep -qiE "blocked|banned|suspend|not accepting|Slow down"; then echo "STOP: block/limit on $s" | tee -a runB.log; exit 1; fi
  sleep 630
done
echo ALLDONE | tee -a runB.log
