import MySQLdb

host = "localhost"
user = "aplicacao"
password = "123456"
db = "escola_curso"
port = 3306

con = MySQLdb.connect(host, user, password, db, port)

c = con.cursor(MySQLdb.cursors.DictCursor) #a complementação torna o resultado em um dicionario, se estivesse vazio viria em uma tupla

def select(fields, tables, where=None):
	global c 
	query = "SELECT " + fields + " FROM " + tables
	if (where):
		query = query + " WHERE " + where
	c.execute(query)
	return c.fetchall()

"""result = select("nome, cpf", "alunos") #campo where não obrigatorio
print(result[0]["cpf"])"""

def insert(values, table, fields=None):
	global c, con
	query = "INSERT INTO " + table
	if(fields):
		query = query + " (" + fields + ") "
	query = query + " VALUES " + ",".join(["(" + v + ")" for v in values])

	c.execute(query)
	con.commit()

'''values = [
	"DEFAULT, 'João Pedro', '2000-01-01', 'Av das Pedras', 'Betim', 'MG', '12345678911'",
	"DEFAULT, 'Maria Pedro', '2000-01-01', 'Av das Pedras', 'Betim', 'MG', '12345678910'"]

insert(values, "alunos")
print(select("*","alunos"))'''

def update(sets, table, where=None):
	global c, con
	query = "UPDATE " + table
	query = query + " SET " + ",".join([field + " = '" + value + "'" for field, value in sets.items()])
	if (where):
		query = query + " WHERE " + where
	c.execute(query)
	con.commit()

"""update({"nome":"João Martins","cidade": "Curitiba"}, "alunos", "id_aluno = 8")
print(select("*", "alunos", "id_aluno = 8"))"""

def delete(table, where):
	global c, con
	query = "DELETE FROM " + table + " WHERE " + where
	c.execute(query)
	con.commit()

"""print(select("*","alunos","id_aluno = 9"))
print(delete("alunos", "id_aluno = 9"))
print(select("*","alunos","id_aluno = 9"))"""

