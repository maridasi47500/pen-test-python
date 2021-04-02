echo "ma radio va être lancée sur le <a href=\"http://localhost:3000\">localhost</a>"
chromium-browser "http://localhost:3000" &
xterm -l -hold -e "cd /home/mary/radiohaker && echo 'entrez le mot de passe et entrez rails s' && bash -l -c 'rails s'"
