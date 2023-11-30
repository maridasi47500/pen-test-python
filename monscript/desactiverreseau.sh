RESEAU=$(ifconfig | grep 172.20 -B 1 | awk '{print $1}')
HEY=$(echo $RESEAU | awk '{print $1}')
echo $HEY
sudo ifconfig $HEY down
