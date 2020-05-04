#!/usr/bin/env python
# -*- coding: utf8 -*-
""" Resolução de exercicios wiki Python Brasil
Estrutura de Repetição.
"""


def main():

    def ex001():
        while True:
            nota = input("Digite uma nota de 0 a 10: ")
            if int(nota) >= 0 and int(nota) <= 10: 
                try:
                    saida = 's'
                    if nota == saida:
                        print("done")
                        break
                    print("Nota: {}".format(nota))
                except NameError:
                    raise("done")

            else:
                print("Erro!! Digite um valor de 0 a 10") 


    def ex002():
        while True:
            nome = str(input('Nome: '))
            senha = str(input('senha'))
            print('Digite s para sair')
            if nome == senha:
                print('OPS!!! Digite uma senha diferente do seu nome')
            elif nome == 's' or senha == 's':
                print('Closed')
                break
            else:
                continue


    def ex003():
        """[*]Faça um programa que leia e valide as seguintes informações:

    Nome: maior que 3 caracteres;
    Idade: entre 0 e 150;
    Salário: maior que zero;
    Sexo: 'f' ou 'm';
    Estado Civil: 's', 'c', 'v', 'd'; """

        while True:
            def get_nome():
                nome = input("Nome(> 3 letras): ")
                if len(nome) < 3:
                    print("Digite um nome com mais caracteres")
                    get_nome()
                else:
                    return nome
                
            def get_idade():
                idade = int(input("Idade(0 a 150): "))
                if idade < 0 or idade > 150:
                    print("Digite idade entre 0 e 150")
                    get_idade()
                else:
                    return idade
                
            def get_salario():
                salario = float(input("Salario(>0): "))
                if salario < 0:
                    print("Digite um salario valido(>0)")
                    get_salario()
                else:
                    return salario
                
            def get_sexo():
                sexo = input("Sexo(f, m): ")
                opcoes = ('m', 'f')
                if sexo not in opcoes:
                    print("Digite uma opção valida")
                    get_sexo()
                else:    
                    return sexo
                
            def get_estado_civil():
                estado_civil = input("Estado Civil(s, c, d, v): ")
                opcoes = ('s', 'c', 'd', 'v')
                if estado_civil not in opcoes:
                    print("Digite uma opção válida")
                    get_estado_civil()
                else:
                    return estado_civil
                
            def sair():
                saida = input("Deseja contunuar?(y/n) ")
                if saida == 'n':
                    print('Closed')
                    exit(0)
                

            def run():
                get_nome()
                get_idade()
                get_salario()
                get_sexo()
                get_estado_civil()
                sair()
            run()

    def ex004():
        """[ ]Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de
    crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.
    Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse
    ou iguale a população do país B, mantidas as taxas de crescimento."""
        # taxas de crescimento
        taxa_a = 0.03
        taxa_b = 0.015
        # numero de habitantes
        a = 80000
        b = 200000
        while b >= 200000:
            

            
                
                
    def resolucao():
            # ex001()
            # ex002()
            ex003()
    resolucao()

if __name__ == "__main__":
    main()

