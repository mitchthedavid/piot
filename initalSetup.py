validType=False
validNumber=False

maxSensors=25

while validType == False or validNumber == False:
    try:
        numSensors=int(input("Please enter the number of boolean sensors: "))
        if numSensors<28 and numSensors>0:
            validType=True
            validNumber=True
    except:
        print ("not valid, please try again")

