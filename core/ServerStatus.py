import requests
import datetime
import json

# get minecraft data function
def getStatus(address):
    currentDateTime = datetime.datetime.utcnow()

    getData = requests.get("https://api.mcsrvstat.us/2/"+address)
    dataResult = json.loads(getData.text)

    serverAddress = dataResult['hostname'] if dataResult['online'] else " "
    serverPort = dataResult['port'] if dataResult['online'] else " "
    serverisOnline = "<a:upnode:1236261218512011346> " if dataResult['online'] else "<a:downnode:1236264807322091580> "
    serverPlayersOnline = dataResult['players']['online'] if dataResult['online'] else " "
    serverPlayersMax = dataResult['players']['max'] if dataResult['online'] else " "
    serverVersion = dataResult['version'] if dataResult['online'] else " "
    serverMotd = '\n'.join(dataResult['motd']['clean']) if dataResult['online'] else " "

    return(serverAddress,serverPort,serverisOnline,serverPlayersOnline,serverPlayersMax,serverVersion,serverMotd, currentDateTime)