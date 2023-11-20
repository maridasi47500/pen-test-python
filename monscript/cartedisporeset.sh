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
pacmd set-card-profile 1 a2dp_sink
pacmd set-default-sink  bluez_sink.E8_85_4B_74_6E_CC
pacmd set-default-source bluez_sink.E8_85_4B_74_6E_CC.monitor

echo "=========\n"
espeak how are you
espeak -vfr+f5 "Bonjour tu parles bien le français? comment vas tu?"

echo "=========\n"
espeak how are you
echo "=========\n"




espeak hi there say hello
