import json


class SingletonConfiguration:
    _instance = None
    _config = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SingletonConfiguration, cls).__new__(cls)
        return cls._instance

    def load_config(self):
        if self._config is None:
            with open('example_config_path.json', 'r') as file:
                self._config = json.load(file)
        return self._config


# Usage
if __name__ == "__main__":
    singleton1 = SingletonConfiguration()
    config1 = singleton1.load_config()
    singleton2 = SingletonConfiguration()
    config2 = singleton2.load_config()
    print(singleton1 is singleton2)
    print(config1 == config2)
