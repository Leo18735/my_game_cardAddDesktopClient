import json
from os.path import exists


def get_config(config_path: str) -> dict:
    """
    Loads config from specific file
    :param config_path: filePath for config
    :return: config as dictionary
    """
    config: dict = {}
    if exists(config_path):
        with open(config_path, "r") as f:
            config = json.load(f)
    else:
        with open(config_path, "w") as f:
            json.dump({}, f)
    return config


def store_config(config: dict, config_path: str) -> None:
    """
    stores config from dict to file
    :param config: config as dict
    :param config_path: filePath as string
    :return: Nothing
    """
    with open(config_path, "w") as f:
        json.dump(config, f)
    return
