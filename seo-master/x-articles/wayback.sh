for u in $(python3 -c "import json;[print(x[2]) for x in json.load(open('index.json'))]") https://x.com/infinitumceo/status/2097223267358757183 https://x.com/infinitumceo/status/2097223351651766471 https://x.com/infinitumceo/status/2095860351791194402 https://x.com/infinitumceo/status/2109367089731399765 https://x.com/infinitumceo/status/2092197732295336180 https://x.com/infinitumceo/status/2090752445349580867 https://x.com/infinitumceo/status/2089710026176786458 https://x.com/infinitumceo/status/2083866189428637943; do
  r=$(curl -s -o /dev/null -w "%{http_code} %{redirect_url}" -m 120 -A "Mozilla/5.0" "https://web.archive.org/save/$u")
  loc=$(curl -sI -m 60 "https://archive.org/wayback/available?url=$u" >/dev/null; curl -s -m 60 "https://archive.org/wayback/available?url=$u" | python3 -c "import sys,json;s=json.load(sys.stdin).get('archived_snapshots',{}).get('closest',{});print(s.get('url',''),s.get('timestamp',''))")
  echo "$u | save:$r | latest:$loc"; sleep 8
done
