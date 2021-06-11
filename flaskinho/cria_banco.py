import sqlite3


#importando a lib sqlite3, que já vem no Python, então não há necessidade de usar pip install
connection = sqlite3.connect('banco.db') #criando a conexão com BD
cursor = connection.cursor() #cursor serve para selecionar os registros no BD

cria_tabela = 'CREATE TABLE IF NOT EXISTS hoteis(hotel_id text PRIMARY KEY,\
 nome text, estrelas real, diaria real, cidade text )' #usando comando sql para criar uma tabela com os atributos da nossa classe Hotel

cria_hotel = 'INSERT INTO hoteis VALUES ("efga", "Hotel Ef Gales", 2.2, 150.25, "São Paulo")'

cursor.execute(cria_tabela) #nosso cursor executará o comando SQL armazenado em cria_tabela para criar o banco
cursor.execute(cria_hotel)

connection.commit()
connection.close()