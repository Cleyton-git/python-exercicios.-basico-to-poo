distancia = int(input("Distancia da viagem em KM: "))

if distancia < 200:
    print(f"Sua viagem de {distancia}km's fica no valor de {distancia*0.50}R$")
else:
    print(f"Sua viagem de {distancia}km's fica no valor de {distancia*.45}R$")
