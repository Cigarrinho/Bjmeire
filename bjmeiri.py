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

    cursor.execute(" select nome, senha from login_funcionario where nome = '{}' and senha = '{}'". format(login, senha_v))

    for (nome, senha) in cursor:
        if login == nome or senha_v == senha:
            chama_opçoes()
        elif login != nome or senha_v != senha:
            func_login.nome.setText('|Nome ou senha INVALIDOS|')

# |=-----------------------------------------------------------------VERIFICA_SENHA_USER--------------------------------------------------------------------------=| #

def verifica_senha_user():
    
    global login

    
    
    login = user_login.nome.text()

    senha_v = user_login.senha.text()

    catalogo.nome.setText(login)

    tela_user.nome.setText(login)

    tela_user.user_2.setText(login)

    cursor = connect.cursor()

    cursor.execute(" select nome, senha from login_cliente where nome = '{}' and senha = '{}'". format(login, senha_v))

    for (nome, senha) in cursor:
        if login == nome or senha_v == senha:
            chama_catalogo()
        elif login != nome or senha_v != senha:
            user_login.nome.setText('|Nome ou senha INVALIDOS|')

# |=-------------------------------------------------------------------------------------------------------------------------------------------=| #

def cadastro_cliente():

    linha1 = cadastro.nome.text()

    linha2 = cadastro.email.text()

    linha3 = cadastro.senha.text()

    linha4 = cadastro.cep.text()

    linha5 = cadastro.telefone.text()

    linha6 = cadastro.endereco.text()

    linha7 = cadastro.nasc.text()

    linha8 = cadastro.cpf.text()


    inserir = "INSERT INTO cadastro (id, nome, email, senha, cep, telefone, endereco, nasc, cpf) values (null, %s, %s, %s, %s, %s, %s, %s, %s)"
    
    dados = (linha1, linha2, linha3, linha4, linha5, linha6, linha7, linha8)

    cursor = connect.cursor()

    cursor.execute(inserir, dados)
  
    connect.commit()

    cursor.close()

# |=-------------------------------------------------------------------------------------------------------------------------------------------=| #

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


# |=-------------------------------------------------------------------------------------------------------------------------------------------=| #

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

# |=-------------------------------------------------------------------------------------------------------------------------------------------=| #

def chama_L_user():
    user_login.show()
    pre_login.hide()
    

def chama_L_func():
    func_login.show()
    pre_login.hide()

def volta_func_user():
    cd_user.hide()
    cadastro.hide()
    pre_login.show()
    func_login.hide()
    user_login.hide()

def chama_login():
    cadastro.hide()
    user_login.show()

def cadastro_user():
    user_login.hide()
    cd_user.show()

def volta_cd_user():
    user_login.show()
    cd_user.hide()

def volta_login():
    func_login.show()
    cd_opções.hide()

# Função para mostrar a tela de cadastro e esconder a tela de login

def chama_cadastro(): 
    cadastro.show()
    cd_opções.hide()
   
# Função para mostrar a tela de catalogo e esconder a tela de cadastro

def chama_catalogo():
    catalogo.show()
    user_login.hide()

# Função para mostrar a tela de escolha e esconder a tela de login

def chama_opçoes():
    cd_opções.show()
    func_login.hide()
    cadastro.hide()
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
    cadastro.show()
    cd_opções.hide()

# Função para chamar tela do usuario

def chama_user():
    tela_user.show()
    catalogo.hide()


# |=-------------------------------------------------------------------------------------------------------------------------------------------=| #

app=QtWidgets.QApplication([])

pre_login=uic.loadUi('pre_login.ui') # Inicializador antes da tela de login

user_login=uic.loadUi('login_user.ui') # Inicializador antes da tela de login do cliente

func_login=uic.loadUi('login_func.ui') # Inicializador da tela de login

tela_user=uic.loadUi('client.ui') # Inicializador da area do cliente

cd_user=uic.loadUi('cd_user.ui') # Inicalizador da tela de cadastro de usuario

cadastro=uic.loadUi('cadastro.ui') # Inicializador da tela de cadastro

catalogo=uic.loadUi('catalogo.ui') # Inicializador da tela de catálogo

cd_opções=uic.loadUi('cd_opções.ui') # Inicializador da tela de escolhas

cd_vendas=uic.loadUi('cd_vendas.ui') # Inicializador da tela de cadastro de vendas

cd_prod=uic.loadUi('cd_prod.ui') # Inicializador da tela de cadastro de produtos

cd_fornecedor=uic.loadUi('cd_fornecedor.ui') # Inicializador da tela de cadastro de fornecedor

pagamentos=uic.loadUi('pagamentos.ui') # Inicializador da tela de pagamento

# |=---------------------------------------------------------------PRE_LOGIN----------------------------------------------------------------------------=| #

pre_login.cliente.clicked.connect(chama_L_user)
pre_login.funcionario.clicked.connect(chama_L_func)

# |=---------------------------------------------------------------LOGIN_FUNC----------------------------------------------------------------------------=| #

func_login.registrar.clicked.connect(cadastro_user) # Botão de entrar da tela de login
func_login.entrar.clicked.connect(verifica_senha_func) # Botão de entrar da tela de login para tela de escolha
func_login.voltar.clicked.connect(volta_func_user) # Botão para voltar a tela de login

# |=---------------------------------------------------------------LOGIN_USER----------------------------------------------------------------------------=| #

user_login.registrar.clicked.connect(cadastro_user) # Botão de entrar da tela de login
user_login.entrar.clicked.connect(verifica_senha_user) # Botão de entrar da tela de login para tela de escolha
user_login.voltar.clicked.connect(volta_func_user) # Botão para voltar a tela de login

# |=----------------------------------------------------------------CD_USER----------------------------------------------------------------------=| #

cd_user.click.clicked.connect(volta_func_user) # Botão entrar tela login

cd_user.inscrevase.clicked.connect(volta_cd_user) # Botão para finaçlizar cadastro 


# |=------------------------------------------------------------CADASTRO-------------------------------------------------------------------------------=| #

cadastro.inscrevase.clicked.connect(cadastro_cliente) # funçao cadastro cliente

cadastro.inscrevase.clicked.connect(chama_catalogo) # Botão de inscrever-se da tela de login

cadastro.login.clicked.connect(volta_func_user) # Botão para chamar a tela de login

cadastro.voltar.clicked.connect(chama_opçoes)

catalogo.user.clicked.connect(chama_user) #Botão para chamar tela do usuario


# |=-------------------------------------------------------------CD_OPÇÔES----------------------------------------------------------------------------------=| #

cd_opções.vendas.clicked.connect(chama_vendas) # Botão de 'cadastro de vendas' da tela de escolha para o cadastro de vendas

cd_opções.prod.clicked.connect(chama_produtos) # Botão de 'cadastro de produtos' da tela de escolha para o cadastro de produtos

cd_opções.voltar.clicked.connect(volta_login) # Botão 'voltar' da tela de escolha para a tela de login

cd_opções.forne.clicked.connect(chama_forne) # Botão 'cadastro de fornecedores'  na tela de escolha para a tela de fornecedores
 
cd_opções.cliente.clicked.connect(chama_cadastro_op) # Botão de 'cadastro de cliente' na tela de escolha para a tela de cadastro de clientes

# |=----------------------------------------------------------------CD_PROD---------------------------------------------------------------------------------=| #

cd_prod.finalizar.clicked.connect(cadastro_prod) # Botão de 'voltar' da tela de cadastro de produtos para a tela de escolha

cd_prod.finalizar.clicked.connect(volta_op_prod) # Botão para chamar as opções apos cadastro de um produto

cd_prod.voltar.clicked.connect(volta_op_prod) # Botão de 'voltar' da tela de cadastro de vendas para a tela de escolha

# |=----------------------------------------------------------------CD_FORNECEDOR--------------------------------------------------------------------------=| #

cd_fornecedor.voltar.clicked.connect(volta_forn) # Botão de 'voltar' na tela de cadastro de fornecedores para a tela de cadastro de escolha

cd_fornecedor.finalizar.clicked.connect(volta_forn) # Botão para votar a tela de opçoes ao finalizar o cadastro de fornecedores

# |=------------------------------------------------------------------CATALOGO-----------------------------------------------------------------------------=| #

catalogo.carrinho.clicked.connect(tela_pagamento) # Botão do carrinho para tela de pagamento

# |=---------------------------------------------------------------------PAGAMENTOS------------------------------------------------------------------------=| #

pagamentos.voltar.clicked.connect(voltar_catalogo) # Botão 'voltar' da tela de pagamento para o catalogo

# |=-------------------------------------------------------------------------------------------------------------------------------------------------------=| #


pre_login.show() # Tela inicial de login

app.exec() # Execução das janelas