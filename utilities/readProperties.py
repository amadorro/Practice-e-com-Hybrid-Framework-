
# This is good for reusability by removing hardcode values
import configparser

config = configparser.RawConfigParser()
# read data from .ini file
config.read("./Configurations/config.ini")

# get .ini variables
class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getEmail():
        email = config.get('common info', 'email')
        return email

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password