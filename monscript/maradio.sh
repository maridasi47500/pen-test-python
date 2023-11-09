echo "ma radio va être lancée"
chromium-browser "http://localhost:3000" &
xterm -l -hold -e "(cd /home/mary/radiohaker && echo 'entrez le mot de passe et entrez rails s' && sudo -s)"
