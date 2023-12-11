import json

class AppConfig:

    @classmethod
    def load_config(cls, file_path):
        with open(file_path) as file:
            cls.config = json.load(file)
        return cls.config

    @classmethod
    def get_config(cls, key):
        if cls.config is None:
            raise ValueError("Configuration not loaded. Use AppConfig.load_config(file_path) first.")
        if '.' in key:
            keys = key.split('.')
            current = cls.config
            for k in keys:
                if isinstance(current, dict) and k in current:
                    current = current[k]
                else:
                    return None
            return current
        elif key in cls.config:
            return cls.config[key]
        else:
            return None

# Загрузка конфигурации при запуске приложения
AppConfig.load_config('app_config.json')

# Получение значения конфигурации через класс
assert AppConfig.get_config('database') == {
    'host': '127.0.0.1', 'port': 5432,
    'database_name': 'postgres_db',
    'user': 'owner',
    'password': 'ya_vorona_ya_vorona'}
assert AppConfig.get_config('database.user') == 'owner'
assert AppConfig.get_config('database.password') == 'ya_vorona_ya_vorona'
assert AppConfig.get_config('database.pass') is None
assert AppConfig.get_config('password.database') is None

# Создание экземпляра класса AppConfig
config = AppConfig()

# Получение значения конфигурации через экземпляр класса
assert config.get_config('max_connections') == 10
assert config.get_config('min_connections') is None

# Еще один экземпляр класса AppConfig
conf = AppConfig()

# Проверка, что значения параметров одинаковы для всех экземпляров
assert conf.get_config('max_connections') == 10
assert conf.get_config('database.user') == 'owner'
assert conf.get_config('database.host') == '127.0.0.1'
assert conf.get_config('host') is None

print('Good')
