import ConfigParser

config = ConfigParser.ConfigParser()
config.read('db.conf')

db_connect(config.get('DB', 'host'),
           config.get('DB', 'port'),
           config.get('DB', 'user'))
