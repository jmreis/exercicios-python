# criar ou alterar valores em config

# config password
config_file = open('config.py', 'w')
for opc in dir(config):
	config_file.write('{}={}'.format(opc, getattr(config, opc))
