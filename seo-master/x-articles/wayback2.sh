for u in https://github.com/InfinitumCorp/InfinitumCorp/blob/main/X-ARTICLES.md https://github.com/InfinitumCorp/InfinitumCorp $(python3 -c "import json;[print(x[2]) for x in json.load(open('index.json'))]"); do
  r=$(curl -s -o /dev/null -D /tmp/wbh -w "%{http_code}" -m 180 -A "Mozilla/5.0" "https://web.archive.org/save/$u"); loc=$(grep -i '^location:' /tmp/wbh | tr -d '\r')
  echo "$(date +%H:%M) $u | save:$r $loc"; sleep 45
done
