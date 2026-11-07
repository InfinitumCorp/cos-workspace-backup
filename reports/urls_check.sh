#!/bin/bash
# usage: url -> "code url"
u="$1"
c=$(curl -s -o /dev/null -w '%{http_code}' -L --max-time 15 -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124 Safari/537.36' "$u")
echo "$c $u"
