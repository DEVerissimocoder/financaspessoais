from django.db import models

# Create your models here.
from django.db import models

class Person(models.Model):
    nome = models.CharField(max_length=20)

    TIPO_CHOICES = [
        ("creditor", "Credor"),
        ("deptor", "Devedor"),
    ]

    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default="deptor")

    def is_upperClass(self):
        return self.tipo

    def __str__(self):
        return self.nome

class CardFatura(models.Model):
    nome=models.CharField(max_length=50)
    METHOD_PAYMENT = {
        "debit": "débito",
        "credit": "crédito"
    }
    method_payment = models.CharField(max_length=50, choices=METHOD_PAYMENT, default="debito")

    def is_upperClass(self):
        return self.method_payment
    
    def __str__(self):
        return self.nome


class Expense(models.Model):
    card= models.ForeignKey(CardFatura, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    date = models.DateField()
    MODALITY = {
    "health": {
        "gym": "academia",
        "pharmacy": "farmácia",
        "exams": "exames",
        "doctorAppointment": "consulta"
    },
    "food": {
        "market": "mercado",
        "snackBar": "lanchone",
        "bakey": "padaria"
    },
    
    "education": {
        "school": "escola",
        "publicTender": "concurso",
        "faculty": "faculdade"
    },
    "transport": {
        "van": "van",
        "bus": "onibus",
    },
    "leisure": {
        "cinema": "cinema",
        "park": "parque",
        "party": "festa",
    },
    "loan": {
        "consignado": "consignado",
        "informal": "informal",
    },
    "donation": {
        "gift": "presente",
        "alms": "esmola",
    },

    "house": {
        "reform": "reforma",
        "utensils": 'utensílios',
        "forniture": "móveis",
        "conta_agua": "conta de água",
        "conta_luz": "conta de luz",
    },
    "outhers":{
        "beautifull": "beleza",
        "plano_funeraria": "plano funerária",
        "seguro_vida": "plano de vida",
        "seguro_carro": "seguro de carro",
        "credito_celular": "credito para celular",
        
    },
    "vestuario": "vestuario",
    
}
    description= models.CharField(max_length=50)
    value=models.FloatField()
    STATUS = {
        "pago": "pago",
        "a pagar": "a pagar"
    }
    status = models.CharField(max_length=20, choices=STATUS, default="recebido")
    modality = models.CharField(max_length=20, choices=MODALITY)
    def __str__(self):
        return self.description
    
    def is_upperClass(self):
        return self.status, self.modality
    
   
class Revenue(models.Model):
    card= models.ForeignKey(CardFatura, on_delete=models.CASCADE)
    person= models.ForeignKey(Person, on_delete=models.CASCADE, default=1)
    date = models.DateField()
    description=models.CharField(max_length=50)
    value = models.FloatField()
    STATUS = {
        "recebido": "recebido",
        "a receber": "a receber"
    }
    status = models.CharField(max_length=20, choices=STATUS, default="recebido")

    def is_upperClass(self):
        return self.status

class Investment(models.Model):
    date= models.DateField()
    description= models.CharField(max_length=50)   
    valor=models.FloatField()
    profit = models.FloatField()

    def __str__(self):
        return self.description

