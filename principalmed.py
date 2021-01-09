
listadem={}
listadep={}
consultas={}

def escreverArquivoMédicos():
    with open('dadosmédicos.txt', 'w') as arquivosMedicos:
        for key in listadem.keys():
            arquivosMedicos.write(f'{key} {listadem[key]["Nome"]} {listadem[key]["CPF"]} {listadem[key]["Sexo"]}'
                                  f' {listadem[key]["status"]}\n')


def escreverArquivoPacientes():
    with open('dadosacientes.txt', 'w') as arquivosPacientes:
        for key in listadep.keys():
            arquivosPacientes.write(f'{key} {listadep[key]["Nome"]} {listadep[key]["Sexo"]}\n')


def escreverArquivoConsultas():
    with open('consultas.txt', 'w') as arquivosConsultas:
        for key in consultas:
            arquivosConsultas.write(f'{key} {consultas[key]["CPF"]} {consultas[key]["Tipo da consulta"]} '
                                    f'{consultas[key]["CRM do médico"]} {consultas[key]["Status da consulta"]} '
                                    f'{consultas[key]["Valor"]}')

def usarArquivoMédicos():
    try:
        with open('dadosmédicos.txt', 'r') as arquivosMedicos:
            for linha in arquivosMedicos:
                linha = linha.strip().split()
                crm = linha[0]
                listadem[crm] = {'Nome': linha[1], 'CPF': linha[2], 'Sexo': linha[3], 'status': linha[4]}
    except FileNotFoundError:
        open('dadosmédicos.txt', 'w')


def usarArquivoPacientes():
    try:
        with open('dadosacientes.txt', 'r') as arquivosPacientes:
            for linha in arquivosPacientes:
                linha = linha.strip().split()
                cpf = linha[0]
                listadep[cpf] = {'Nome': linha[1], 'Sexo': linha[2]}
    except FileNotFoundError:
        open('dadosacientes.txt', 'w')


def usarArquivoConsultas():
    try:
        with open('Consultas.txt', 'r') as arquivoConsultas:
            for linha in arquivoConsultas:
                linha = linha.strip().split()
                data = linha[0]
                consultas[data] = {'CPF': linha[1], 'Tipo da consulta': linha[2], 'CRM do médico': linha[3],
                                   'Status da consulta': linha[4], 'Valor': linha[5]}
    except FileNotFoundError:
        open('Consultas.txt', 'w')


def cadastromed():
        nome = input("Nome do médico:")
        while True:
            try:
                crm=int(input("CRM do médico(sem pontuação):"))
            except TypeError:
                print('Digite sem pontuação!')
                continue
            else:
                crm=str(crm)
                break
        while True:
            try:
                cpfm=int(input("CPF do médico(sem pontuação):"))
            except TypeError:
                print('Digite sem pontuação!')
                continue
            else:
                cpfm=str(cpfm)
                break
        while True:
            sexom = input("Sexo do médico(Masculino/Feminino):").capitalize()
            if sexom == "Masculino" or sexom == "Feminino":
                break
            else:
                print("Digite um dos dois!")
        while True:
            status=input("Status do médico(Ativo/Inativo):").capitalize()
            if status=="Ativo" or status=="Inativo":
                break
            else:
                print("Digite um dos dois!")
        listadem['{}'.format(crm)]={'Nome':'{}'.format(nome),'CPF':'{}'.format(cpfm),'Sexo':'{}'.format(sexom),'status':'{}'.format(status)}
        return cadastromed




def cadastropac():
    nome = input("Nome do paciente:")
    while True:
        try:
            cpfp=int(input("CPF do paciente(sem pontuação):"))
        except TypeError:
            print('Digite sem pontuação!')
            continue
        else:
            cpfp=str(cpfp)
            break
    while True:
        sexop = input("Sexo do paciente(Masculino/Feminino):").capitalize()
        if sexop == "Masculino" or sexop == "Feminino":
            break
        else:
            print("Digite um dos dois!")
    listadep['{}'.format(cpfp)] = {'Nome': '{}'.format(nome), 'Sexo': '{}'.format(sexop)}
def regdecons():
    cont=1
    while True:
        data=input('Data da consulta(Formato ddmmaaaa):')
        while True:
            tipo=input('Retorno ou primeira consulta?(Responda com "Retorno"/"Primeira")')
            if tipo=='Primeira':
                valor=300
                break
            elif tipo=='Retorno':
                valor=100
                break
            else:
                print('Digite como foi pedido!')
        while True:
            try:
                cpf = int(input("CPF do paciente(sem pontuação):"))
            except TypeError:
                print('Digite sem pontuação!')
                continue
            else:
                cpf=str(cpf)
                break
        while True:
            try:
                crm=int(input("CRM do médico(sem pontuação):"))
            except TypeError:
                print('Digite sem pontuação!')
                continue
            else:
                crm=str(crm)
                break
        if listadem[crm]['status']=='Inativo':
            print('Médico não esta disponível!')
            continue
        else:
            while '{}.{}'.format(data,cont) in consultas:
                cont+=1
            if '{}.{}'.format(data,1) not in consultas:
                cont=1
            consultas['{}.{}'.format(data,cont)] ={'CPF': cpf, 'Tipo da consulta': tipo, 'CRM do médico': crm,
                               'Status da consulta': 'Ativa', 'Valor': valor}
            break
def cancdecons():
    while True:
        x=0
        data = input('Data da consulta(Formato ddmmaaaa):')
        while True:
            try:
                cpf = int(input("CPF do paciente(sem pontuação):"))
            except TypeError:
                print('Digite sem pontuação!')
                continue
            else:
                cpf=str(cpf)
                break
        while True:
            try:
                crm = int(input("CRM do médico(sem pontuação):"))
            except TypeError:
                print('Digite sem pontuação!')
                continue
            else:
                crm=str(crm)
                break
        for i in consultas:
            if i in consultas:
                if consultas[i]['CPF']==cpf:
                    if consultas[i]['CRM do médico']==crm:
                        consultas[i]['Status da consulta']='Inativa'
                        consultas[i]['Valor']=0
                        x=2
                        break
                    else:
                        print('Médico não relacionado a essa consulta!')
                        x=1
                else:
                    print('CPF não tem consultas registradas!')
                    x=1
            else:
                print('Data não reservada para consulta!')
                x=1
        if x==1:
            continue
        elif x==2:
            break
def relatdepac():
    for i in listadep:
        print('Nome: {}\nCPF: {}\nSexo: {}'.format(listadep[i]['Nome'],i,listadep[i]['Sexo']))
        print('=-='*10)
def relatdemed():
    for i in listadem:
        if listadem[i]['status']=='Ativo':
            print('Nome: {}\nCPF: {}\nSexo: {}\nCRM: {}'.format(listadem[i]['Nome'],listadem[i]['CPF'],listadem[i]['Sexo'],i))
            print('=-='*10)
def relatdecons():
    valorarrecadado=0
    data=input('Informe a data(Formato ddmmaaaa):')
    for i in consultas:
        print('Data: {}\n'
              'CRM do médico: {}\n'
              'Nome do médico: {}\n'
              'CPF do paciente: {}\n'
              'Nome do paciente: {}\n'
              'Status da consulta: {}\n'
              'Tipo da consulta: {}\n'
              'Valor da consulta: R${},00'.format(data,
                                                  consultas[i]['CRM do médico'],
                                                  listadem[consultas[i]['CRM do médico']]['Nome'],
                                                  consultas[i]['CPF'],
                                                  listadep[consultas[i]['CPF']]['Nome'],
                                                  consultas[i]['Status da consulta'],
                                                  consultas[i]['Tipo da consulta'],
                                                  consultas[i]['Valor']))
        print('=-='*10)
        valorarrecadado += int(consultas[i]['Valor'])
    print('Valor arrecadado: R${},00'.format(valorarrecadado))





usarArquivoMédicos()
usarArquivoConsultas()
usarArquivoPacientes()

while True: #principal
    try:
        print()
        print('=-='*10)
        print("Menu:\n"
              "1-Cadastro de Médicos\n"
              "2-Cadastro de Pacientes\n"
              "3-Registrar Consulta\n"
              "4-Cancelar Consulta\n"
              "5-Relatório de Pacientes\n"
              "6-Relatório de Médicos Ativos\n"
              "7-Relatório de Consultas por Data\n"
              "0-Sair")
        print('=-=' * 10)
        escolha = int(input('Opção:'))
    except:
        print('Digite um dos números!')
        continue
    if escolha==0:
        break
    elif escolha==1:
        print()
        cadastromed()
    elif escolha==2:
        print()
        cadastropac()
    elif escolha==3:
        print()
        regdecons()
    elif escolha==4:
        print()
        cancdecons()
    elif escolha==5:
        print()
        relatdepac()
    elif escolha==6:
        print()
        relatdemed()
    elif escolha==7:
        print()
        relatdecons()

escreverArquivoMédicos()
escreverArquivoConsultas()
escreverArquivoPacientes()