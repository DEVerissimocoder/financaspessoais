import json


def createExpense():
    payment_method =    input("informe a forma de pagamento\n")
    person =            input("informe a pessoa devedora\n")
    description =       input("informe uma descrição\n")
    value =             float(input("informe o valor da despesa\n"))
    status =            input("informe o status\n")
    modalidade =        input("informe a modalidade\n")


    dict_expenses={
        "payment_method": payment_method,
        "person"        : person,
        "description"   : description,
        "status"        : status,
        "modalidade"    : modalidade
    } 
    with open('financespessoais.json', 'a', encoding='utf-8') as arquivo:
        json.dump(dict_expenses, arquivo)
        arquivo.write('\n')
def updateExpense():
    with open('financespessoais.json', 'r') as arquivo:
        conteudo = json.load(arquivo)
    print('-------forma de pagamento\n---------')
    print(f'{conteudo['payment_method']}')
    print('----------\ndevedor\n----------')
    print(conteudo['person'])
    print('----------\ndescrição\n----------')
    print(conteudo['description'])
    print('----------\nstatus\n----------')
    print(conteudo['status'])
    print('----------\nmodalidade\n----------')
    print(conteudo['modalidade'])
        
updateExpense()