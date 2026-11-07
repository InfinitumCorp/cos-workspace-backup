u="$1"; h="$2"
curl -s -m 20 "$u" -o /tmp/p.html -w "%{http_code}\n"; grep -o '<h1[^>]*>[^<]*' /tmp/p.html; echo "md count: $(grep -c '\*\*' /tmp/p.html)"
echo "- 2026-10-31 | $h | PressLiftoff | $u | indexed: no (new)" >> /workspace/press/published.md
