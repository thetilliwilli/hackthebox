#!/bin/bash
curl -XPOST -H'Content-Type: application/json' -d'{"name":"theadmin","email":"tilli2@willi.gmail","password":"123456"}' http://10.10.11.120/api/user/register
