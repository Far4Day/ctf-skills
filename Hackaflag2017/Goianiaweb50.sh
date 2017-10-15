#!/bin/bash

curl --user-agent \
"Firefox Hunter Flag" -s "https://hackaflag.com.br/90012/web50/vendor/bootstrap/js/bootstrap.min.js"\
 | grep "localStorage.setItem" | sed 's/.*localStorage.setItem//g' | tr '"' ' ' | \
 awk '{print $2}' | base64 -d
