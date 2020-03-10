
# coding: utf-8

# # Programa de cadastro de funcionarios em python 3

# Programa de cadastro de funcionario com nome, telefone, celular, email, cep, bairro.
# 
# Valido de idade de funcionario.
# 

# Nome do funcionario

# In[ ]:


nome = str(input("Digite o nome do funcionario: "))
print("Concluído")


# Validando idade do funcionario

# In[ ]:


#Idade do funcionario
idade = int(input("Digite a idade do funcionario: "))
if idade > 18:
    print("Funcionario aprovado pode continuar o cadastro!")
if idade < 18:
    print("Funcionario não aprovado não pode ser cadastrado !")


# Validando e-mail do funcionario

# In[ ]:


#E-Mail do funcionario    
email = str(input("Digite o email do funcionario: "))
def valid_email(string):
    pos = string.find("@")
    dot = string.rfind(".")
    if pos < 1:
        return False
    if dot < pos + 2:
        return False
    if dot + 2 >= len(string):
        return False
    return True
print("E-Mail aprovado funcionario !")


# Cadastro de funcionarios 
# Cadastra nome, telefone, email, celular.
# 

# In[ ]:


#Cadastro do funcionario 1
nome = str(input("Digite o nome do funcionario primeiro: "))
idade = int(input("Digite a idade do nuncionario: "))
telefone = int(input("Digite o numero de telefone do primeiro funcionario: "))
celular = int(input("Digite o numero de celular do primeiro funcionario: "))
email = str(input("Digite o email do funcionario do primeiro funcionario: "))
bairro = str(input("Digite o nome do bairro do primeiro funcionario: "))
CEP = int(input("Digite o numero do cep do primeiro funcionario: "))
print("\n")
#Cadastro do funcionario 2
nome = str(input("Digite o nome do funcionario segundo: "))
idade = int(input("Digite a idade do nuncionario: "))
telefone = int(input("Digite o numero de telefone do primeiro funcionario: "))
celular = int(input("Digite o numero de celular do Segundo funcionario: "))
email = str(input("Digite o email do funcionario do segundo funcionario: "))
bairro = str(input("Digite o nome do bairro do segundo funcionario:  "))
CEP = int(input("Digite o numero do cep do segundo funcionario: "))
print("\n")
#Cadastro do funcionario 3
nome = str(input("Digite o nome do funcionario terceiro: "))
idade = int(input("Digite a idade do nuncionario: "))
telefone = int(input("Digite o numero de telefone do terceiro funcionario: "))
celular = int(input("Digite o numero de celular do Terceiro funcionario: "))
email = str(input("Digite o email do funcionario do terceiro funcionario: "))
bairro = str(input("Digite o nome do bairro do terceiro funcionario: "))
CEP = int(input("Digite o numero do cep do terceiro funcionario: "))
print("\n")
print("Cadastro funcionarios concluído com sucesso !")

