import configparser

config=configparser.RawConfigParser()
config.read("C:\\Users\\Admin\\PycharmProjectsgitHubAutomation\\Configuration\\config.ini")

class ReadPropeties:

    @staticmethod
    def getUrl():
        url=config.get("LogIn Info","url")
        return url

    @staticmethod
    def getUsername():
        username=config.get("LogIn Info","userName")
        return username

    @staticmethod
    def getPassword():
       password=config.get("LogIn Info", "Password")
       return password

