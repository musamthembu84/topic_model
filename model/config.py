from configparser import ConfigParser

config_object = ConfigParser ()

config_object["TWITTERAUTH"] = {
    "ACCESS_TOKEN" : "703575776936005632-FjYSE9jmQEhl6FGxaLQIp8KGm0N9rEf",
    "ACCESS_SECRET" : "VFo08hhyYwJAI8A1QtEDXuZzTCHTkp8hyVNsSZvYFjfYw",
    "CONSUMER_KEY" : "ATyQnHGDt5HoWbdC7geil8NgH",
    "CONSUMER_SECRET" : "WcjCUT1T554qNuWfp50Kss4pcwY9txrV2hvPBrBuXN0SufzMJj"
}

data(){
    
}

with open('config.ini', 'w') as conf:
    config_object.write(conf)


