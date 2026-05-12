temperaturas = [
    [28, 31, 34, 33],
    [25, 27, 29, 28],
    [32, 35, 36, 34],
    [24, 26, 25, 27]
]

for i, sala_temp in enumerate(temperaturas):
    # print(sala_temp)

    soma = 0
    crit = 0

    for temp in sala_temp:
        soma = soma + temp
        if temp >= 33:
            crit += 1

    media = soma / 4

    print(f"Sala {i+1}")
    print(f"Média:{media}")
    print(f"Registros críticos:{crit}")
    print()
