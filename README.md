# piot
series of scripts for streamlining the use of an rpi as an IoT device for data collection and monitoring

## installing dependendies
```
sudo apt update && sudo apt-get install -y git python3-pip python3
pip3 install adafruit-io
pip3 install datetime
```
## download the piot respository and configure
```
sudo git clone https://www.github.com/mitchpehora/piot
cd piot
```
before running the setup script, make sure you know your Adafruit username and AIO key
```
sudo python3 initalSetup.py
```

## running the weight rack
```
sudo python3 weightRack.py
```

## setting the script to run at boot
edit the following file:
```
sudo nano /home/pi/.bashrc
```
add the following to the end of the file
```
sudo python3 /home/pi/piot/weightRack.py
```
