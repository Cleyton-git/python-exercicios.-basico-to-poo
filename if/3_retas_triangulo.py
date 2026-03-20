reta1 = int(input("1 reta em CM: "))
reta2 = int(input("2 reta em CM: "))
reta3 = int(input("3 reta em CM: "))

if reta1 + reta2 > reta3 and reta2 + reta3 > reta1 and reta1 + reta3 > reta2 :
    print("É possivel formar um triangulo")
else:
    print("Não é possivel forma um triangulo")
    