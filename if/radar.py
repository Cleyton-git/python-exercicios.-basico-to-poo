velocidade = int(input("Digite sua velocidade: "))

if velocidade > 80:
    print(f"Vc foi multado em {(velocidade-80)*7}R$")
else:
    print("Muito bom cidadão ta andando nos conformes")
    