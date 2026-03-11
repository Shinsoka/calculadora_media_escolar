continuar = "s"

while continuar == "s":
			
			print("Vamos calcular as suas 4 notas do ano, e descobrir se você passou de ano, ficou de recuperação ou foi reprovado! :)")

			nota1	=	float(input("Nota 1: "))
			while nota1 < 0 or nota1 > 10:
				print("Nota inválida. Digite um valor entre 0 e 10.")
				nota1 = float(input("Nota 1: "))

			nota2 	=	float(input("Nota 2: "))
			while nota2 < 0 or nota2 > 10:
				print("Nota inválida. Digite um valor entre 0 e 10.")
				nota2 = float(input("Nota 2: "))

			nota3 	=	float(input("Nota 3: "))
			while nota3 < 0 or nota3 > 10:
				print("Nota inválida. Digite um valor entre 0 e 10.")
				nota3 = float(input("Nota 3: "))

			nota4 	=	float(input("Nota 4: "))
			while nota4 < 0 or nota4 > 10:
				print("Nota inválida. Digite um valor entre 0 e 10.")
				nota4 = float(input("Nota 4: "))

			media	= (nota1 + nota2 + nota3 + nota4) / 4

			print("A sua média é:", round(media, 2))

			if media >= 7:
				print("Meus parabéns, você foi aprovado!")
			elif media >= 5:
				print("Faltou pouco, você está de recuperação, estude bem!")
			else:
				print("Você foi reprovado, tente novamente no ano que vem! Ps:Temos desconto para repetentes :)")
			continuar = input("Deseja continuar? (s/n): ")

print("Programa encerrado")