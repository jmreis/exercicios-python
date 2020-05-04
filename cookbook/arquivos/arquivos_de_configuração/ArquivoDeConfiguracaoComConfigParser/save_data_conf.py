import ConfigParser

# instanciando a classe
config = ConfigParser.ConfigParser()
# adicionando secao
config.add_section("DB")
# configurando dados
config.set("DB", "host", host)
config.set("DB", "port", port)
config.set("DB", "user", user)
# abrindo arquivo
file = open("db.conf", "w")
# escrevendo no arquivo
config.write(file)
# fechando arquivo
file.close()
