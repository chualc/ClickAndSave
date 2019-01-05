import shelve

class SettingInfo:
    def __init__(self):
        self.speed = "low"
        self.temperature = 20


settingFile = shelve.open('settingInfo')

def saveInfo(userId, speed, temperature):
    i = SettingInfo()
    i.speed = speed
    i.temperature = temperature
    settingFile[userId] = i

def saveSpeed(userId, speed):
    if userId in settingFile: # retrieve record
        i = settingFile[userId]
        del settingFile[userId]
    else: # new record
        i = SettingInfo()

    i.speed = speed
    settingFile[userId] = i


def saveTemperature(userId, temperature):
    if userId in settingFile: # retrieve record
        i = settingFile[userId]
        del settingFile[userId]
    else: # new record
        i = SettingInfo()
    i.temperature = temperature
    settingFile[userId] = i

def getInfo(userId):
    if userId in settingFile:
        return settingFile[userId]
    else:
        return None
