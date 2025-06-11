import configparser

class ConfigManager:
    def __init__(self, config_file_path):
        self.config_file_path = config_file_path
        self.config = configparser.ConfigParser()
        self.read_config()

    def read_config(self):
        self.config.read(self.config_file_path)

    def get_config(self, section, key):
        return self.config.get(section, key)

    def set_config(self, section, key, value):
        self.config.set(section, key, value)
        with open(self.config_file_path, 'w') as configfile:
            self.config.write(configfile)

    def get_all_configs(self):
        all_configs = {}
        for section in self.config.sections():
            all_configs[section] = {key: self.config.get(section, key) for key in self.config[section]}
        return all_configs



