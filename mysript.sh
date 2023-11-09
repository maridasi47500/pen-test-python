iproxy 2222 22 &
xterm -hold -e "ssh -p 2222 root@localhost ls"
