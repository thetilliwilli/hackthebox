#!/bin/bash
curl -XPOST -H'Content-Type: application/json' -d'{"email":"tilli@willi.gmail","password":"123456"}' http://10.10.11.120/api/user/login

