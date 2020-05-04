
a = 80000
b = 200000
ano = 0
taxa = a * 0.03
while True:
    a = a + taxa
    print(a)
    ano += 1
    if a == b:
        print(ano)
        break

