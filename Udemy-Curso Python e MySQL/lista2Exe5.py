arquivo = open("seq.fasta")
linhas = arquivo.readlines()
multifasta = {}

for linha in linhas:
	if linhas[0] == ">":
		seq_atual = linha[1:].strip()
		multifasta[seq_atual] = ""
	else:
		multifasta[seq_atual] = multifasta[seq_atual]+linhas.strip()
print multifasta