telefones=[]
funcionarios=[]

op_funcionario=0
funcionarios_vazio=True

def novo_funcionario():
    global op_funcionario
    global funcionario_alvo
    global funcionarios_vazio
    print("\n----Cadastre um novo Funcionário----\n")
    numero = op_funcionario
    funcionario_alvo=numero
    nome = str(input("\nNome: "))
    cpf= int(input("\nCpf: "))
    cargo = str(input("\nCargo: "))
    salario = float(input("\nSalario: "))
    telefone = int(input("\nTelefone: "))
    telefones.append(telefone)
    funcionario = {"Indice": numero, "Nome": nome, "Cpf": cpf,"Cargo":cargo,"Salario":salario, "Telefone":telefones[op_funcionario]}
    funcionarios.append(funcionario)
    mostrar_funcionario()
    op_funcionario+=1
    funcionarios_vazio=False

def editar_funcionario():
    op_cpf=int(input("\nEncontre um funcionario atraves do Cpf: "))
    op_encontrar=False
    for i in range(len(funcionarios)):
      if funcionarios[i]["Cpf"]==op_cpf:
          funcionarios[i]["Nome"]= str(input("\nNome: "))
          funcionarios[i]["Cpf"]=int(input("\nCpf: "))
          funcionarios[i]["Cargo"]=str(input("\nCargo: "))
          funcionarios[i]["Salario"]=telefone = int(input("\nSalario: "))
          telefones[i]=telefone = int(input("\nTelefone: "))
          op_encontrar=True
    if op_encontrar==False: print("Funcinario não encontrado.")

def funcionariosVazio():
  print("A lista de funcionarios está vazia. Tente outra opção.")
  menu_principal()

def mostrar_funcionario():
    for i in range(len(funcionarios)):
        if funcionarios[i]["Indice"]==funcionario_alvo:
            print("\nInformações do funcionario: ")
            print(funcionarios[i])

def pesquisar_funcionario():
    op_cpf=int(input("\nEncontre um funcionario atraves do Cpf: "))
    for i in range(len(funcionarios)):
        if funcionarios[i]["Cpf"]==op_cpf:
            print("\nInformações do funcionario: ")
            print("\nNome: "+str(funcionarios[i]["Nome"])+"\nCpf: "+str(funcionarios[i]["Cpf"])+"\nCargo: "+str(funcionarios[i]["Cargo"])+"\nSalario: R$"+str(funcionarios[i]["Salario"])+"\nTelefone: "+str(telefones[i])+"\n")
    
def cadastrar_telefone():
    op_cpf=int(input("\nEncontre um funcionario atraves do Cpf: "))
    op_encontrar=False
    for i in range(len(funcionarios)):
        if funcionarios[i]["Cpf"]==op_cpf:
            novo_numero=int(input("\nDigite o numero novo: "))
            telefones[i]=novo_numero
            op_encontrar=True
    if op_encontrar==False: print("Funcinario não encontrado.")

def deletar_funcionario():
    op_cpf=int(input("\nEncontre um funcionario atraves do Cpf: "))
    for i in range(len(funcionarios)):
        if funcionarios[i]["Cpf"]==op_cpf:
            del(funcionarios[i])
            del(telefones[i])
            print("Funcionario deletado.")
            break        

def menu_principal():
    op_menu_principal = int(input("-------------------------\n 1- Cadastro de Funcionarios \n 2- Pesquisar Funcionario \n 3- Cadastrar novo telefone \n 4- Editar dados do Funcionário \n 5- Deletar funcionário \n 0- Sair \n-------------------------\n"))
    if op_menu_principal == 1:
        novo_funcionario()
        menu_principal()
    elif op_menu_principal==2:
      if len(funcionarios)==0:
        funcionariosVazio()
      else: 
        pesquisar_funcionario() 
        menu_principal()
    elif op_menu_principal==3:
      if len(funcionarios)==0:
        funcionariosVazio()
      else:
        cadastrar_telefone() 
        menu_principal()
    elif op_menu_principal==4:
      if len(funcionarios)==0:
        funcionariosVazio()
      else: 
        editar_funcionario() 
        menu_principal()
    elif op_menu_principal==5:
      if len(funcionarios)==0:
        funcionariosVazio()
      else: 
        deletar_funcionario() 
        menu_principal()
    elif op_menu_principal==0:
      pass
    else:
        print("\nOpção inválida.\n")
        menu_principal()

menu_principal()