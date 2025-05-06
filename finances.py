import json

lista=[]
def createExpense():
    payment_method =    input("informe a forma de pagamento\n")
    person =            input("informe a pessoa devedora\n")
    """description =       input("informe uma descrição\n")
    value =             float(input("informe o valor da despesa\n"))
    status =            input("informe o status\n")
    modalidade =        input("informe a modalidade\n")"""

    dict_expenses={
        "payment_method": payment_method,
        "person"        : person        
    } 
    conteudo_arquivo=listExpense()
    print(conteudo_arquivo)
    '''if not conteudo_arquivo:
        print("arquivo vazio")
        with open('financespessoais.json', 'w', encoding='utf-8') as arquivo:
            json.dump(arquivo, ensure_ascii=False)        
    else:      
        print("arquivo tem algum conteudo")
        with open('financespessoais.json', 'w', encoding='utf-8') as arquivo:
            json.dump(conteudo_arquivo.append(dict_expenses), arquivo)
    print(conteudo_arquivo)
            '''
def listExpense():
    with open('financespessoais.json', 'r') as arquivo:
        conteudo = json.load(arquivo)
        print(conteudo, type(conteudo))
    print(f'''
          ----------------  -------  ---------  --------  -----------------
          |  FORMA_PAGAM     PESSOA   DESCRIÇÃO  STATUS    MODALIDADE     |
          ----------------  -------  ---------  --------  -----------------
          |      {conteudo[0]['payment_method']}         {conteudo[0]['person']}|
          -----------------------------------------------------------------   
''')
    return conteudo
   

createExpense()
listExpense()