import configparser

config = configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")


class ReadConfig:
    @staticmethod
    def get_app_url():
        url = config.get('common data', 'baseurl')
        return url

    @staticmethod
    def get_username():
        username = config.get('common data', 'username')
        return username

    @staticmethod
    def get_password():
        password = config.get('common data', 'password')
        return password
