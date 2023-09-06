import pymysql


conexao = pymysql.connect(
    host = 'localhost',
    user = 'root', 
    password = '', 
    database = 'mercadinho',
)

cursor = conexao.cursor()
condition = True 

while condition == True:

    print ("Olá sou Billy, seu assistente de Gerencimanento de Mercadinho")
    print ("Irei te ajudar no que for preciso!!")
    print ("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

    # Começa o loop do While
    resposta = input("Você deseja começar as atividades? S/N")
    if (resposta == "S") or (resposta == "s") :
        print ("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print ("Fico contente!")

        # Escolhe a tabela que vai trabalhar
        print ('As tabelas disponíveis para você são:')
        print (" 1 - Tabela Clientes\n 2 - Tabela Produto\n 3 - Tabela Vendas"  )

        escolha = input("Em qual tabela você deseja trabalhar? ")

        # Começa o if/else da tabela Cliente
        if escolha == '1' :
            print ("Que maravilha, vamos trablhar com Clientes!") 
            print ("Quais dessas opções você deseja executar? ")
            print (" 1 - Adicionar um novo Cliente\n 2 - Atualizar Registro de Cliente\n 3 - Buscar por um Cliente\n 4 - Deletar Registro do Cliente")
            escolha_cliente = input("Qual a sua escolha?" )

            # Insert Cliente    
            if escolha_cliente == '1': 
                print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                print("Vamos adicionar um novo cliente, você vai precisar do nome e enderenço para registrar!")
                nome_ins = input("Insira o nome do novo cliente:")
                endereco_ins = input("Insira o endereço do novo cliente:")
                telefone_ins = input("Insira o telefone do novo cliente:")
                
                comando_ins =f'INSERT INTO  clientes (nome, endereco,telefone) VALUES ("{nome_ins}", "{endereco_ins}", "{telefone_ins}")'
                cursor.execute(comando_ins)
                conexao.commit() #edita o banco de dados
                print("Atividade realizada com sucesso!")
            
            
            # Update Cliente
            elif escolha_cliente == '2': 
                print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                print("Vamos atualizar um cliente, você vai precisar do nome para atualizar o endereço!")
                nome_upd = input("Insira o nome do cliente: ")
                endereco_upd = input("Insira o novo endereço do cliente: ")

                comando_upd = f'UPDATE clientes SET endereco = "{endereco_upd}" WHERE nome = "{nome_upd}"'
                cursor.execute(comando_upd)
                conexao.commit()
                print("Atividade realizada com sucesso!")
            
            
            # Select Cliente
            elif escolha_cliente == '3': 
                print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                print("Então estamos procurando por um cliente! Insira o nome dele e irei procurar nos registros")

                nome_slt = input ("Insira o nome do cliente: ")
                
                comando_slt = f'SELECT * FROM clientes  WHERE nome = "{nome_slt}"'
                cursor.execute(comando_slt)
                resultado = cursor.fetchall() 
                print(resultado)
                conexao.commit()
                print("Atividade realizada com sucesso!")
            

            # Delete Cliente
            elif escolha_cliente =='4': 
                print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                print("Tudo bem, vamo excluir um cliente! Insira o nome dele e irei executar a exclusão")
            
                nome_del = input ("Insira o nome do cliente que deseja excluir: ")

                comando_del = f'DELETE FROM clientes WHERE nome = "{nome_del}"'
                cursor.execute(comando_del)
                conexao.commit()
                print("Atividade realizada com sucesso!")
            

        # Começa if/else Produto 
        elif escolha == '2' :
            print ("Que maravilha, vamos trabalhar com Produtos!")
            print ("Quais dessas opções você deseja executar? ")
            print (" 1 - Adicionar um novo Produto\n 2 - Atualizar Registro de Produto\n 3 - Buscar por um Produto\n 4 - Deletar Registro do Produto")
            escolha_produto = input("Qual a sua escolha?" )

            # Insert Produto
            if escolha_produto == '1': 
                print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                print("Vamos adicionar um novo produto, você vai precisar do nome, quantidade e preco para registrar!")
                nome_ins = input("Insira o nome do novo produto:")
                quantidade_ins = input("Insira a quantidade do novo produto:")
                preco_ins = input("insira o preco do novo produto:")

                comando_ins_prd =f'INSERT INTO  produtos ( nome, quantidade, preco) VALUES ("{nome_ins}", "{quantidade_ins}", "{preco_ins}")'
                cursor.execute(comando_ins_prd)
                conexao.commit() #edita o banco de dados
                print("Atividade realizada com sucesso!")
            
            
            # Update Produto
            elif escolha_produto == '2': 
                print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                print("Vamos atualizar um Produto, você vai precisar do nome para atualizar o preco!")
                nome_upd = input("Insira o nome do produto: ")
                preco_upd = input("Insira o novo preco do produto: ")

                comando_upd_prd = f'UPDATE produtos  SET preco = "{preco_upd}" WHERE nome = "{nome_upd}"'
                cursor.execute(comando_upd_prd)
                conexao.commit()
                print("Atividade realizada com sucesso!")
            
            # Select Produto
            elif escolha_produto == '3': 
                print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                print("Então estamos procurando por um Produto! Insira o nome dele e irei procurar nos registros")

                nome_slt = input ("Insira o nome do produto: ")
                
                comando_slt_prd = f'SELECT * FROM produtos  WHERE nome = "{nome_slt}"'
                cursor.execute(comando_slt_prd)
                resultado = cursor.fetchall() 
                print(resultado)
                conexao.commit()
                print("Atividade realizada com sucesso!")

            # Delete Produto
            elif escolha_produto =='4': 
                print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                print("Tudo bem, vamo excluir um Produto! Insira o nome dele e irei executar a exclusão")
            
                nome_del = input ("Insira o nome do produto que deseja excluir: ")
                    
                comando_del_prd = f'DELETE FROM produtos WHERE nome = "{nome_del}"'
                cursor.execute(comando_del_prd)
                conexao.commit()
                print("Atividade realizada com sucesso!")

        # Começa if/else Vendas
        elif escolha == '3' :
            print("Que maravilha, vamos trabalhar com Vendas!")
            print ("Quais dessas opções você deseja executar? ")
            print (" 1 - Adicionar uma nova Venda\n 2 - Atualizar Registro de Venda\n 3 - Buscar por uma Venda\n 4 - Deletar Registro da Venda")
            escolha_venda = input("Qual a sua escolha?" )

            # Insert Vendas
            if escolha_venda == '1': 
                print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                print("Vamos adicionar uma nova Venda, você vai precisar do id cliente e o id produto, além da data da venda e a quantidade para registrar!")
                id_cli_ins = input("Insira o id do cliente:")
                id_prd_ins = input("Insira o id do produto vendido:")
                qtd_vnd = input("Insira a quantidade do produto vendido: ")
                data_vnd = input("Insira a data da venda, seguindo o modelo - YYYY-MM-DD: ")
                
                comando_ins_vnd =f'INSERT INTO  vendas (id_produto, id_cliente, quantidade, data_venda) VALUES ("{id_cli_ins}", "{id_prd_ins}", "{qtd_vnd}", "{data_vnd}")'
                cursor.execute(comando_ins_vnd)
                conexao.commit() #edita o banco de dados
                print("Atividade realizada com sucesso!")
            
            # Update Vendas
            elif escolha_venda == '2': 
                print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                print("Vamos atualizar uma Venda, você vai precisar do registro para atualizar a transição!")
                id_cli_upd = input("Insira o id do cliente: ")
                id_prd_upd = input("Insira o id do produto: ")
                qtd_vnd_upd = input("Insira a nova quantidade do produto vendido: ")

                comando_upd_vnd = f'UPDATE vendas SET quantidade = "{qtd_vnd_upd}" WHERE id_cliente = "{id_cli_upd}" and id_produto = "{id_prd_upd}"'
                cursor.execute(comando_upd_vnd)
                conexao.commit()
                print("Atividade realizada com sucesso!")
            
            # Select Vendas
            elif escolha_venda == '3': 
                print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                print("Então estamos procurando por uma Venda! Insira o regitro da Venda e irei procurar nos registros")

                venda_slt = input ("Insira o id do cliente: ")
                
                comando_slt_vnd = f'SELECT * FROM vendas  WHERE id_cliente = "{venda_slt}"'
                cursor.execute(comando_slt_vnd)
                resultado = cursor.fetchall() 
                print(resultado)
                conexao.commit()
                print("Atividade realizada com sucesso!")

            # Delete Vendas
            elif escolha_venda =='4': 
                print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                print("Tudo bem, vamo excluir uma Venda! Insira o registro da venda e irei executar a exclusão")
            
                id_cli_del = input ("Insira o id do cliente que deseja excluir a venda: ")
                id_prd_del = input ("Insiera o id do produto que deseja excluir a venda: ")
                    
                comando_del_vnd = f'DELETE FROM vendas WHERE id_cliente = "{id_cli_del}" and id_produto = "{id_prd_del}"'
                cursor.execute(comando_del_vnd)
                conexao.commit()
                print("Atividade realizada com sucesso!")
        else :
            print ("Não entendi sua escolha! Que pena!")
    
    #Finaliza While - Encerra loop 
    else : 
        print("Espero ter ajudado! Até mais!")
        condition = False
        break
