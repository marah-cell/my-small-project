#!/bin/bash

check_nginx() {
status=$(systemctl is-active nginx)
if [ "$status" = "active" ]; then
echo "nginx is runing"
else 
echo "i will start it"
sudo systemctl start nginx
fi
}
check_nginx
