===== Create tamplate "New Document"
cd Templates/
touch "New_Document"


===== FIX DESKTOP ICONS
1.sudo apt install chrome-gnome-shell gnome-shell-extension-prefs
2.need to install new icons with fix: Desktop Icons NG (DING) 
3.need to turn off old icons: Activities > Extansions > off Desctop Icons


===== INSTALL CAFFEINE
from gnome extantions

===== DO DESKTOP WITH BACKGROUND COLOR
gsettings set org.gnome.desktop.background picture-uri ""
gsettings set org.gnome.desktop.background primary-color '#000000'

===== DATE FORMAT
install gnome extantion from gnome plugin "Panel Date Format"
dconf write /org/gnome/shell/extensions/panel-date-format/format "'%H:%M    %a, %d.%m.%y'"


===== UPDATE SETTINGS
settings > About > Software Updates > 
need to choose sources and partners


===== Settings of Text Editor
autosave


===== Setting of Terminal
color

===== Keyboard Language
add russian


===== Flash Player
sudo apt install adobe-flashplugin


===== GNOME TWEAK TOOL
sudo apt install gnome-tweak-tool


===== VLC PLAYER
sudo apt install vlc -y
sudo apt install ubuntu-restricted-extras -y


===== INSTALL ADMIN APPS

= htop
sudo snap install htop


= netstat
sudo apt install net-tools

= netcat
sudo apt install netcat

= glances
sudo snap install glances

= Gparted
sudo apt install gparted -y


= Timeshift
sudo apt-add-repository -y ppa:teejee2008/ppa
sudo apt update
sudo apt install timeshift

= tmux
sudo apt  install tmux

= vim
sudo apt install vim
===== INSTALL DEV ======================================================================

= pip
sudo apt install python3-pip -y

= GIT
sudo apt install git -y

= Docker
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release -y


curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg


echo \
  "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null


sudo apt-get update


sudo apt-get install docker-ce docker-ce-cli containerd.io -y

= Postman
install from US

= VS Code
install from US

= RDM(redis)
install from US

= PyCharm
install from US

= DB Browser for SQLite
install from US

===== BROWSERS and SMM TOOL =================================================================
= chrome
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i --force-depends google-chrome-stable_current_amd64.deb

= firefox setting
about:config
layout.css.devPixelsPerPx     1.25

= tor
= skype
= telegramm
= ZOOM

= Slack

===== LINKEDIN: сделать linkedin.com перенаправление через тор 
sudo nano /etc/tor/torrc
SocksPort localhost:9050 # Bind to this address:port too.

sudo iptables -A INPUT -p tcp -m multiport --dports 9050 -j ACCEPT

need to install FozyProxy
add new Proxy: SOCKS5   localhost:9050
add pettern: white pattern: linkedin  linkedin.com





















