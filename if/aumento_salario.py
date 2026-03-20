salario = int(input("Digite seu salario: "))

if salario > 1250:
    print(f"Seu novo salario é {(salario*0.10)+salario}")
else:
    print(f"Seu novo salario é {(salario*0.15)+salario}")
    