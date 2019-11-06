# piot
series of scripts for streamlining the use of an rpi as an IoT device for data collection and monitoring

#GPIO SUPPORT, PYTHON ESSENTIALS, ADAFRUIT
sudo apt update && sudo apt-get install -y git python3-pip python3
sudo pip3 install adafruit-io 


#clone the repository, run the initial setup command
sudo git clone https://www.github.com/mitchpehora/piot
cd piot
sudo python3 piot/initalSetup.py

#run the rack
sudo python3 weightRack.py
