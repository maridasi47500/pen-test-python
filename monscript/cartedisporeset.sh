. ./venv/bin/activate
pacmd list-cards
echo "=========\n"
pacmd list-cards | grep profil
echo "=========\n"
pactl list cards short
pulseaudio --check
echo "=========\n"
pulseaudio -k
espeak hi there say hello
pulseaudio -D
echo "=========\n"
#pacmd set-card-profile 0 output:analog-stereo+input:analog-stereo
echo "=========\n"
espeak hello
echo "=========\n"
echo $MESAIRPODS
str1=":"
str2="_"

myairpod=""
myairpod=$(echo $MESAIRPODS | tr ":" "_")
echo $myairpod

pacmd set-card-profile 1 a2dp_sink
echo $myairpod
pacmd set-default-sink  "bluez_sink.$myairpod"

pacmd set-default-source "bluez_sink.$myairpod.monitor"



echo "=========\n"
espeak how are you
espeak -vfr+f5 "Bonjour tu parles bien le français? comment vas tu?"

echo "=========\n"
espeak how are you
echo "=========\n"




espeak hi there say hello
