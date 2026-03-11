print("Vamos calcular as suas 4 notas do ano, e descobrir se você passou de ano, ficou de recuperação ou foi reprovado! :)")

def pegar_nota(numero):
	nota = float(input(f"Nota {numero}: ").replace(",", "."))
	while nota < 0 or nota > 10:
		print("Nota inválida. Digite um valor entre 0 e 10.")
		nota = float(input(f"Nota {numero}: ").replace(",", "."))
	return nota

nota1 = pegar_nota(1)
nota2 = pegar_nota(2)
nota3 = pegar_nota(3)
nota4 = pegar_nota(4)


media	= (nota1 + nota2 + nota3 + nota4) / 4

print(f"A sua média é: {media:.2f}")

if media >= 7:
	print("Meus parabéns, você foi aprovado!")
elif media >= 5:
	print("Faltou pouco, você está de recuperação, estude bem!")
else:
	print("Você foi reprovado, tente novamente no ano que vem! Ps:Temos desconto para repetentes :)")