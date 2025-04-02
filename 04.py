distancia = float(input("Informe a distância percorrida (km): "))
tempo = float(input("Informe o tempo gasto na viagem (horas): "))

if tempo > 0:
    velocidade_media = distancia / tempo
    print(f"\nA velocidade média foi de {velocidade_media:.2f} km/h.")
else:
    print("\nO tempo da viagem deve ser maior que zero.")
