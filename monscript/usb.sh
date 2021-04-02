USB_ID=`egrep -i "mct u232|pl2303|keyspan" -m 1 /proc/tty/driver/usbserial | awk '{ printf( "$d", $1 )}'`
if [ -z $USB_ID ]
then
   echo $echo_n "No USB serial adapter found.";
   exit 1
fi
