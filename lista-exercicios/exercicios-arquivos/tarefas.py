"""
Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo, contendo um relatório dos endereços IP válidos e inválidos.

    O arquivo de entrada possui o seguinte formato: 

200.135.80.9
192.168.1.1
8.35.67.74
257.32.4.5
85.345.1.2
1.2.3.4
9.8.234.5
192.168.0.256

    O arquivo de saída possui o seguinte formato: 

[Endereços válidos:]
200.135.80.9
192.168.1.1
8.35.67.74
1.2.3.4

[Endereços inválidos:]
257.32.4.5
85.345.1.2
9.8.234.5
192.168.0.256
"""
def ex001():

    def test_txt():

        with open('ip.txt', 'r') as data:
            for line in data:
                print(line)
    #test_txt()

    def test_regex():
        
        import re
        from pprint import pprint

        with open('ip.txt', 'r') as data:
            regex = r"""
                    (?:\s|^) # Start of string or word boundary
                    ( # Capture Group
                    (?:  # Non-Capture Group for X.
                    (?:    # Nested NCG for 0..255
                    (?:\d){1,2}|  # Allow any single digit or any pair of digits or
                    (?:1\d{2})|   # 3 Digits starting with 1 or
                    (?:2[0-4]\d)| # 3 Digists starting with 20..24 or
                    (?:25[0-5])   # 250..255
                    )      # this should allow X=0..255 in the NCG
                    \.     # Must be followed by a literal .
                    ){3} # X. Must repeat exactly 3 times
                    (?: # NCG for final 0..255
                    (?:\d{1,2})|  # Allow any single digit or any pair of digits or
                    (?:1\d{2})|   # 3 Digits starting with 1 or
                    (?:2[0-4]\d)| # 3 digits starting 20..24 or
                    (?:25[0-5])  # 250.255
                    )   # End of final 0.255
                    ) # End of capture group
                    (?:\s|$) # Must be followed by EOS or wspace
	                """
            pattern = re.compile(regex)
            for line in data:
                print(re.findall(pattern, line))
    test_regex()

ex001()

"""
A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos. 
Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, 
e identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu 
gerar o seguinte arquivo, chamado "usuarios.txt":

alexandre       456123789
anderson        1245698456
antonio         123456456
carlos          91257581
cesar           987458
rosemary        789456125

Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa que gere um relatório, 
chamado "relatório.txt", no seguinte formato:

ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso

1    alexandre       434,99 MB             16,85%
2    anderson       1187,99 MB             46,02%
3    antonio         117,73 MB              4,56%
4    carlos           87,03 MB              3,37%
5    cesar             0,94 MB              0,04%
6    rosemary        752,88 MB             29,16%

Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB

O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários, de forma a agilizar a execução do programa. A conversão da espaço ocupado em disco, de bytes para megabytes deverá ser feita através de uma função separada, que será chamada pelo programa principal. O cálculo do percentual de uso também deverá ser feito através de uma função, que será chamada pelo programa principal. 
"""
