# piot
Series of scripts for streamlining the use of an Pi as an IoT device for data collection and monitoring

## initial configuration of Pi
Flash a micro sd card with [Raspbian Lite](https://www.raspberrypi.org/downloads/raspbian/)
Connect your Pi to internet and enable ssh
Login over ssh and procede to next section

## connect your sensors
Currently, PIoT only supports boolean sensors. 
For input pins, use [7,11,13,15,19,21,23] and [8,10,12,14,16,18,22] for output.

## installing dependendies
```
sudo apt update && sudo apt-get install -y git python3-pip python3
pip3 install adafruit-io
pip3 install datetime
pip3 install RPi.GPIO
pip3 install os
```
## download the piot respository and configure
```
git clone https://www.github.com/mitchpehora/piot
cd piot
```
Before running the setup script, make sure you know your Adafruit username and AIO key.The next command will prompt you for them.
```
python3 initalSetup.py
```

## configure adafruit
Create a feed for each boolean (on/off or high/low) sensor you intend to use. use the following notation:
![adafruit configuration](https://raw.githubusercontent.com/mitchpehora/piot/master/images/adaFruitFeedConfiguration.png)
Each sensor belongs to a feed group called piot.

## running the weight rack
```
python3 weightRack.py
```


