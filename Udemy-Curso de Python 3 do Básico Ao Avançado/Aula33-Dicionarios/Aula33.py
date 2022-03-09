##criar dicionarios

#d1 ={'chave1':'valor da chave'}
#d1['nova_chave'] = 'Valor da nova chave'

#print(d1)

##outra maneira de criar
#d1 = dict(chave1='Valor da chave', chave2="Valor da outra chave")
#d1['nova_chave'] = 'Valor da nova chave'

#print(d1)

##apagar chave
#del d1['chave2']

##pegar valores e chaves

#d1 = {
#    'str':'valor',
#    123:"Outro valor",
#    (1,2,3,4):'Tupla',
#}

#print('str' in d1)
#print('str' in d1.keys())
#print('valor' in d1.values())

##Acessando todos os itens

"""d1 = {
    'chave1':'valor',
    'chave 2':"Outro valor",
    'chave 3':'Tupla',
}

for k, v in d1.items():
    print(k, v)"""

#Usando dict dentro de dict

"""clientes = {
    'cliente1':{
        'nome':'Luiz',
        'sobrenome':'Otavio',
    },
    'cliente2':{
        'nome':'João',
        'sobrenome':'Moreira',
    },
    'cliente3':{
        'nome':'Maria',
        'sobrenome':'Moreira',
    },
}

for cliente_k, clientes_v in clientes.items():
    print(f'Exibindo{cliente_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')"
""