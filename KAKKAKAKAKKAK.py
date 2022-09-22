from http import client
from PyQt5 import uic, QtWidgets # Import do Pyqt5
import mysql
import mysql.connector


connect = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '202173',
        database = 'bjmeire'
    )

# |=-----------------------------------------------------------------VERIFICA_SENHA_FUNC--------------------------------------------------------------------------=| #

def verifica_senha_func():
    
    global login
    
    login = func_login.nome.text()

    senha_v = func_login.senha.text()

    cursor = connect.cursor()

    cursor.execute(" select nome, senha from cd_func where nome = '{}' and senha = '{}'". format(login, senha_v))

    for (nome, senha) in cursor:
        if login == nome or senha_v == senha:
            chama_opçoes()
            func_login.nome.setText('')
            func_login.senha.setText('')
        elif login != nome or senha_v != senha:
            func_login.nome.setText('|Nome ou senha INVALIDOS|')

# |=-----------------------------------------------------------------FUNÇÃO PARA VERIFICAR USUARIO E SENHA--------------------------------------------------------------------------=| #

def verifica_senha_user():
    
    global login

    
    
    login = user_login.nome.text()

    senha_v = user_login.senha.text()

    catalogo.nome.setText(login)

    tela_user.nome.setText(login)

    tela_user.nome.setText(login)

    cursor = connect.cursor()

    cursor.execute(" select nome, senha from cd_user where nome = '{}' and senha = '{}'". format(login, senha_v))

    for (nome, senha) in cursor:
        if login == nome or senha_v == senha:
            chama_catalogo()
            user_login.nome.setText('')
            user_login.senha.setText('')
        elif login != nome or senha_v != senha:
            user_login.nome.setText('|Nome ou senha INVALIDOS|')

# |=------------------------------------------------------------FUNÇAO PARA CADASTRODE CLIENTE-------------------------------------------------------------------------------=| #

def cadastro_cliente():

    linha1 = cd_user.nome.text()

    linha2 = cd_user.senha.text()

    linha3 = cd_user.nasc.text()

    linha4 = cd_user.cpf.text()

    linha5 = cd_user.cep.text()

    linha6 = cd_user.endereco.text()

    linha7 = cd_user.telefone.text()

    linha8 = cd_user.email.text()


    inserir = "INSERT INTO cd_user (id ,nome ,senha , nasc ,cpf ,cep ,endereco ,telefone ,email) values (null, %s, %s, %s, %s, %s, %s, %s, %s)"
    
    dados = (linha1, linha2, linha3, linha4, linha5, linha6, linha7, linha8)

    cursor = connect.cursor()

    cursor.execute(inserir, dados)
  
    connect.commit()

    cursor.close()

# |=------------------------------------------------------------FUNÇAO PARA CADASTRODE FUNCIONARIO-------------------------------------------------------------------------------=| #

def cadastro_func():

    linha1 = cd_func.nome.text()

    linha2 = cd_func.email.text()

    linha3 = cd_func.senha.text()

    linha4 = cd_func.cep.text()

    linha5 = cd_func.telefone.text()

    linha6 = cd_func.endereco.text()

    linha7 = cd_func.nasc.text()

    linha8 = cd_func.cpf.text()


    inserir = "INSERT INTO cd_func (id ,nome ,senha , nasc ,cpf ,cep ,endereco ,telefone ,email) values (null, %s, %s, %s, %s, %s, %s, %s, %s)"
    
    dados = (linha1, linha2, linha3, linha4, linha5, linha6, linha7, linha8)

    cursor = connect.cursor()

    cursor.execute(inserir, dados)
  
    connect.commit()

    cursor.close()

# |=---------------------------------------------------------------FUNÇÃO PARA CADASTRO DE FORNECEDOR----------------------------------------------------------------------------=| #

def cadastro_forn():
    
    linha1 = cd_fornecedor.id.text()

    linha2 = cd_fornecedor.nome.text()

    linha3 = cd_fornecedor.id_prod.text()

    linha4 = cd_fornecedor.marca.text()

    linha5 = cd_fornecedor.produto.text()

    linha6 = cd_fornecedor.quantidade.text()

    linha7 = cd_fornecedor.telefone.text()

    linha8 = cd_fornecedor.email.text()

    inserir = "INSERT INTO cd_fornecedor (codigo, nome, cd_produto, marca, produto, quantidade, telefone, email) values (null, %s, %s, %s, %s, %s, %s, %s, )"
    
    dados = (linha1, linha2, linha3, linha4, linha5, linha6, linha7, linha8)

    cursor = connect.cursor()

    cursor.execute(inserir, dados)

    connect.commit()

    cursor.close()


# |=----------------------------------------------------------FUNÇÂO PARA CADASTRO DE PRODUTO---------------------------------------------------------------------------------=| #

def cadastro_prod():
    
    linha1 = cd_prod.nome.text()

    linha2 = cd_prod.preco.text()

    linha3 = cd_prod.tipo.text()

    linha4 = cd_prod.marca.text()

    linha5 = cd_prod.tamanho.text()

    linha6 = cd_prod.preco_comp.text()

    inserir = "INSERT INTO cd_prod (id, nome, preco, tipo, marca, tamanho,preco_compra ) values (null, %s, %s, %s, %s, %s, %s)"
    
    dados = (linha1, linha2, linha3, linha4, linha5, linha6)

    cursor = connect.cursor()

    cursor.execute(inserir, dados)

    connect.commit()

    cursor.close()

# |=----------------------------------------------------------FUNÇÃO PARA VER DADOS DO CLIENTE---------------------------------------------------------------------------------=| #

def alteracao(): 
    
    dados.show()
    tela_user.hide()

    cursor = connect.cursor()
    sql = "SELECT * FROM bjmeire.cd_userwhere nome= '{}'".format(login)
    cursor.execute(sql)

    leitura_sql = cursor.fetchall()

    dados.tableWidget.setRowCount(len(leitura_sql))
    dados.tableWidget.setColumnCount(9)

    for i in range(0, len(leitura_sql)):
        for j in range(0, 9):
            dados.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(leitura_sql[i][j])))

# |=----------------------------------------------------------FUNÇÃO PARA EXCLUIR DADOS DO CLIENTE ---------------------------------------------------------------------------------=| #

def excluir_dados(): 

    linha =  alter_meiri.tableWidget.currentRow()
    alter_meiri.tableWidget.removeRow(linha)

    cursor = connect.cursor()
    cursor.execute('SELECT id FROM cadastro')
    execute_sql = cursor.fetchall()
    valor_id = execute_sql[linha][0]
    cursor.execute("DELETE FROM cadastro WHERE id = " + str(valor_id))

# |=----------------------------------------------------------FUNÇÃO PARA EDIÇÃO DE DADOS---------------------------------------------------------------------------------=| #

def edicao_dados(): 
    global numero_id
    
    

    cursor = connect.cursor()
    cursor.execute('SELECT * FROM cd_user')
    execute_sql = cursor.fetchall()

    for linha in linhas:
        valor_id = execute_sql[linha][0]
        cursor.execute("SELECT * FROM bjmeire.cd_userwhere nome= '{}'".format(login))
        editar = cursor.fetchall()
        dados.show()

        numero_id = valor_id

        dados.id.setText(linha[0])
        dados.nome.setText(linha[1])
        dados.senha.setText(linha[2])
        dados.cpf.setText(linha[3])
        dados.dt_nasc.setText(linha[4])
        dados.endereco.setText(linha[5])
        dados.cep.setText(linha[6])
        dados.telefone.setText(linha[7])
        dados.gmail.setText(linha[8])


# |=------------------------------------------------------------FUNÇÕES DE CHAMAR TELAS-------------------------------------------------------------------------------=| #

# Função para chamar login do cliente

def chama_L_user():
    user_login.show()
    pre_login.hide()
    
# Função para chamar tela de login do funcionario

def chama_L_func():
    func_login.show()
    pre_login.hide()

# Função para voltar a tela de opções

def volta_func_user():
    cd_user.hide()
    cd_func.hide()
    pre_login.show()
    func_login.hide()
    user_login.hide()

# Função para voltar tela de login do usuario

def chama_login():
    cd_user.hide()
    user_login.show()

# Função para chamar tela de cadastro do usuario

def cadastro_user():
    user_login.hide()
    cd_user.show()

# Função para  voltar a tela de login do usuario

def volta_cd_user():
    user_login.show()
    cd_user.hide()

# Função para função para voltartela de login do funcionario 

def volta_login():
    func_login.show()
    cd_opções.hide()

# Função para mostrar a tela de cadastro e esconder a tela de login

def chama_cadastro(): 
    cd_func.show()
    cd_opções.hide()
   
# Função para mostrar a tela de catalogo e esconder a tela de cadastro

def chama_catalogo():
    catalogo.show()
    user_login.hide()
    tela_user.hide()

# Função para mostrar a tela de escolha e esconder a tela de login

def chama_opçoes():
    cd_opções.show()
    func_login.hide()
    cd_func.hide()
    cd_prod.hide()
    cd_fornecedor.hide()
    cd_vendas.hide()
   
# Função para mostrar a tela de cadastro de vendas e esconder a tela de vendas

def chama_vendas():
    cd_vendas.show()
    cd_opções.hide()
   
# Função para mostrar a tela de cadastro de produto e esconder a tela de vendas

def chama_produtos():
    cd_prod.show()
    cd_opções.hide()

# Função para esconder a tela de escolha e mostrar a tela de login

def chama_cdvendas():
    cd_vendas.hide()
    cd_opções.show()

# Função para esconder a tela de cadastro de produtos e mostrar a tela de escolha

def volta_op_prod():
    cd_prod.hide()
    cd_opções.show()

# Função para esconder a tela de cadastro de venda e mostrar a tela de escolha

def volta_telaVendas_op():
    cd_vendas.hide()
    cd_opções.show()
   
# Função para mostrar a tela de pagamento e esconder a tela de catalogo

def tela_pagamento():
    pagamentos.show()
    catalogo.hide()

# Função para esconder a tela de pagamentos e mostrar a tela de  catalogo

def voltar_catalogo():
    pagamentos.hide()
    catalogo.show()
   
# Função para mostrar a tela de cadastro de fornecedor e esconder a tela de escolha

def chama_forne():
    cd_fornecedor.show()
    cd_opções.hide()

# Função para voltar tela opções _ fornecedores
 
def volta_forn():
    cd_opções.show()
    cd_fornecedor.hide()

# Função para esconder a tela de cadastro de cliente para a tela de vendas

def chama_cadastro_op():
    cd_func.show()
    cd_opções.hide()

# Função para chamar tela do usuario

def chama_user():
    tela_user.show()
    catalogo.hide()

# Função desfazer login do usuario

def sair():
    tela_user.hide()
    pre_login.show()

# |=-------------------------------------------------------------------------------------------------------------------------------------------=| #

app=QtWidgets.QApplication([])

pre_login=uic.loadUi('pre_login.ui') # Inicializador antes da tela de login

user_login=uic.loadUi('login_user.ui') # Inicializador antes da tela de login do cliente

func_login=uic.loadUi('login_func.ui') # Inicializador da tela de login

tela_user=uic.loadUi('client.ui') # Inicializador da area do cliente

cd_user=uic.loadUi('cd_user.ui') # Inicalizador da tela de cadastro de usuario

cd_func=uic.loadUi('cd_func.ui') # Inicializador da tela de cadastro

catalogo=uic.loadUi('catalogo.ui') # Inicializador da tela de catálogo

cd_opções=uic.loadUi('cd_opções.ui') # Inicializador da tela de escolhas

cd_vendas=uic.loadUi('cd_vendas.ui') # Inicializador da tela de cadastro de vendas

cd_prod=uic.loadUi('cd_prod.ui') # Inicializador da tela de cadastro de produtos

cd_fornecedor=uic.loadUi('cd_fornecedor.ui') # Inicializador da tela de cadastro de fornecedor

pagamentos=uic.loadUi('pagamentos.ui') # Inicializador da tela de pagamento

dados=uic.loadUi('info_user.ui') # Inicializador da tela de informações de usuarios
 
# |=---------------------------------------------------------------PRE_LOGIN----------------------------------------------------------------------------=| #

pre_login.cliente.clicked.connect(chama_L_user)
pre_login.funcionario.clicked.connect(chama_L_func)

# |=---------------------------------------------------------------LOGIN_FUNC----------------------------------------------------------------------------=| #

func_login.entrar.clicked.connect(verifica_senha_func) # Botão de entrar da tela de login para tela de escolha
func_login.voltar.clicked.connect(volta_func_user) # Botão para voltar a tela de login

# |=---------------------------------------------------------------LOGIN_USER----------------------------------------------------------------------------=| #

user_login.registrar.clicked.connect(cadastro_user) # Botão de entrar da tela de login
user_login.entrar.clicked.connect(verifica_senha_user) # Botão de entrar da tela de login para tela de escolha
user_login.voltar.clicked.connect(volta_func_user) # Botão para voltar a tela de login

# |=------------------------------------------------------------CD_FUNC-------------------------------------------------------------------------------=| #

cd_func.inscrevase.clicked.connect(cadastro_func) # funçao cadastro cliente

cd_func.inscrevase.clicked.connect(chama_opçoes) # Botão de inscrever-se da tela de login

#cd_func.login.clicked.connect(volta_func_user) # Botão para chamar a tela de login

cd_func.voltar.clicked.connect(chama_opçoes)

# |=------------------------------------------------------------CD_USER-------------------------------------------------------------------------------=| #

cd_user.inscrevase.clicked.connect(cadastro_cliente) # funçao cadastro cliente

cd_user.inscrevase.clicked.connect(chama_catalogo) # Botão de inscrever-se da tela de login

cd_user.login.clicked.connect(volta_func_user) # Botão para chamar a tela de login

# |=-------------------------------------------------------------CD_OPÇÔES----------------------------------------------------------------------------------=| #

cd_opções.vendas.clicked.connect(chama_vendas) # Botão de 'cadastro de vendas' da tela de escolha para o cadastro de vendas

cd_opções.prod.clicked.connect(chama_produtos) # Botão de 'cadastro de produtos' da tela de escolha para o cadastro de produtos

cd_opções.voltar.clicked.connect(volta_login) # Botão 'voltar' da tela de escolha para a tela de login

cd_opções.forne.clicked.connect(chama_forne) # Botão 'cadastro de fornecedores'  na tela de escolha para a tela de fornecedores
 
cd_opções.func.clicked.connect(chama_cadastro_op) # Botão de 'cadastro de cliente' na tela de escolha para a tela de cadastro de clientes

# |=----------------------------------------------------------------CD_PROD---------------------------------------------------------------------------------=| #

cd_prod.finalizar.clicked.connect(cadastro_prod) # Botão de 'voltar' da tela de cadastro de produtos para a tela de escolha

cd_prod.finalizar.clicked.connect(volta_op_prod) # Botão para chamar as opções apos cadastro de um produto

cd_prod.voltar.clicked.connect(volta_op_prod) # Botão de 'voltar' da tela de cadastro de vendas para a tela de escolha

# |=----------------------------------------------------------------CD_FORNECEDOR--------------------------------------------------------------------------=| #

cd_fornecedor.voltar.clicked.connect(volta_forn) # Botão de 'voltar' na tela de cadastro de fornecedores para a tela de cadastro de escolha

cd_fornecedor.finalizar.clicked.connect(volta_forn) # Botão para votar a tela de opçoes ao finalizar o cadastro de fornecedores

# |=------------------------------------------------------------------CATALOGO-----------------------------------------------------------------------------=| #

catalogo.carrinho.clicked.connect(tela_pagamento) # Botão do carrinho para tela de pagamento

catalogo.user.clicked.connect(chama_user) #Botão para chamar tela do usuario

# |=------------------------------------------------------------------------TELA USUARIO-------------------------------------------------------------------------------=| #

tela_user.alt_dados.clicked.connect(edicao_dados)

tela_user.catalogo.clicked.connect(chama_catalogo)

tela_user.sair.clicked.connect(sair)

tela_user.del_dados.clicked.connect(excluir_dados)

tela_user.con_dados.clicked.connect(edicao_dados)

# |=---------------------------------------------------------------------PAGAMENTOS------------------------------------------------------------------------=| #

pagamentos.voltar.clicked.connect(voltar_catalogo) # Botão 'voltar' da tela de pagamento para o catalogo

# |=-------------------------------------------------------------------------------------------------------------------------------------------------------=| #


pre_login.show() # Tela inicial de login

app.exec() # Execução das janelas