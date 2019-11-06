# piot
 debian package for streamlining the use of an rpi as an IoT device for data collection and monitoring

#should be able to pass array of packages to statement in loop


#GPIO SUPPORT, PYTHON ESSENTIALS, ADAFRUIT
sudo apt update && sudo apt-get install -y git python3-pip python3
sudo pip3 install adafruit-io 


#clone the repository, run the initial set command
sudo git clone https://www.github.com/mitchpehora/piot && sudo python3 piot/initialSetup.py

#run the rack
sudo piot/weightRack.py
