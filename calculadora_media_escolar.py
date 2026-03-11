print("Vamos calcular a média das suas notas, e descobrir se você passou de ano, ficou de recuperação ou foi reprovado! :)")

def pegar_nota(numero):
	nota = float(input(f"Nota {numero}: ").replace(",", "."))
	while nota < 0 or nota > 10:
		print("Nota inválida. Digite um valor entre 0 e 10.")
		nota = float(input(f"Nota {numero}: ").replace(",", "."))
	return nota

quantidade =int(input("Quantas notas deseja calcular? "))
notas = []
for i in range(quantidade):
	nota = pegar_nota(i + 1)
	notas.append(nota)


media	= sum(notas) / len(notas)

print(f"A sua média é: {media:.2f}")

if media >= 7:
	print("Meus parabéns, você foi aprovado!")
elif media >= 5:
	print("Faltou pouco, você está de recuperação, estude bem!")
else:
	print("Você foi reprovado, tente novamente no ano que vem! Ps:Temos desconto para repetentes :)")