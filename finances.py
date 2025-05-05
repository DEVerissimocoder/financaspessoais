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
    arquivo=json.load()
    with open('financespessoais.json', 'a', encoding='utf-8') as arquivo:
        json.dump(dict_expenses, arquivo, ensure_ascii=False)
        
def listExpense():
    with open('financespessoais.json', 'r') as arquivo:
        conteudo = json.load(arquivo)
    print(f'''
          ----------------  -------  ---------  --------  -----------------
          |  FORMA_PAGAM     PESSOA   DESCRIÇÃO  STATUS    MODALIDADE     |
          ----------------  -------  ---------  --------  -----------------
          |      {conteudo['payment_method']}         {conteudo['person']}      {conteudo['description']}      {conteudo['status']}     {conteudo['modalidade']}   |
          -----------------------------------------------------------------   
''')
    return conteudo
   
#listExpense()
createExpense()