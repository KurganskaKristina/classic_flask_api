from os import environ

from classic_api.config import Config

config_path = environ.get("CONFIG_PATH") or '/home/kristina/PycharmProjects/users_api/config.json'
config = Config(config_path).read()

CONFIG_REQUIRED_FIELDS = ["database"]

DATABASE = {
    'drivername': config["database"]['drivername'],
    'host': config["database"]["host"],
    'port': config["database"]['port'],
    'username': config["database"]['username'],
    'password': config["database"]['password'],
    'database': config["database"]['database']
}