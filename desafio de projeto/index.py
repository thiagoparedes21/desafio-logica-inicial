nomeHeroi = input("Digite o nome do seu herói: ")
xpHeroi = float(input("Digite o XP do seu herói: "))
nivelHeroi = ""

while nomeHeroi:
    if xpHeroi < 1000:
        nivelHeroi = "Ferro"
        break
    elif xpHeroi >= 1000 and xpHeroi <= 2000:
        nivelHeroi = "Bronze"
        break
    elif xpHeroi >= 2001 and xpHeroi <= 5000:
        nivelHeroi = "Prata"
        break
    elif xpHeroi >= 5001 and xpHeroi <= 7000:
        nivelHeroi = "Ouro"
        break
    elif xpHeroi >= 7001 and xpHeroi <= 8000:
        nivelHeroi = "Platina"
        break
    elif xpHeroi >= 8001 and xpHeroi <= 9000:
        nivelHeroi = "Ascendente"
        break
    elif xpHeroi >= 9001 and xpHeroi <= 10000:
        nivelHeroi = "Imortal"
        break
    else:
        nivelHeroi = "Radiante"
        break
print(f"O herói de nome {nomeHeroi} está no nível {nivelHeroi}.")
