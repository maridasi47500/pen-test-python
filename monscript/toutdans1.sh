/etc/init.d/bluetooth restart
. ./venv/bin/activate
pacmd list-cards
echo "=========\n"
pacmd list-cards | grep profil
echo "=========\n"
pactl list cards short
echo "=========\n"
#pacmd set-card-profile 0 output:analog-stereo+input:analog-stereo
echo "=========\n"
espeak hello
echo "=========\n"
pacmd set-card-profile 1 a2dp_sink
echo $MESAIRPODS
str1=":"
str2="_"
myairpod=""
myairpod=$(echo $MESAIRPODS | tr ":" "_")
echo $myairpod

pacmd set-default-sink bluez_sink.E4_90_FD_23_79_04.a2dp_sink
#pacmd set-default-card "bluez_card.$myairpod"
#pacmd set-default-source "bluez_card.$myairpod.monitor"
pacmd set-default-sink "bluez_sink.$myairpod.a2dp_sink"
pacmd set-default-source "bluez_sink.$myairpod.a2dp_sink.monitor"

echo "=========\n"
espeak how are you
espeak -vfr+f5 "Bonjour tu parles bien le français? comment vas tu?"
echo "=========\n"
