menu = 0

def abrirArquivo():
	nome = input("Digite o nome do arquivo que deseja abrir: ")
	arquivo = open(nome)
	return arquivo

def lerArquivo(arquivo):
	linhas = arquivo.readlines()
	for linha in linhas:
		print linhas.strip()



while menu != 3:
	print("(1) Abrir arquivo\n(2) Ler arquivo aberto\n(3) Sair\n")
	menu = input("Digite a opção desejada: ")
	if menu == 1:
		arquivo = abrirArquivo()
	elif menu == 2:
		lerArquivo(arquivo)