from django.db import models

# Create your models here.
UFS = [
           ('SP', 'São Paulo'),
           ('RJ', 'Rio de Janeiro'),
           ('ES', 'Espirito Santo'),
           ('MG', 'Minas Gerais')
     ]



class Cidade(models.Model):
    nome = models.CharField(max_length=50)
    uf = models.CharField(max_length=2, choices=UFS)

    def __str__(self):
        return self.nome



class Contato(models.Model):
    #Opcoes do campo Estado Civil
    # primeiro valor da tupla é o que vai no banco
    # o segundo é o que vai na tela     


    ESTADO_CIVIS =[
     ('S', 'Solteiro'),
     ('C', 'Casado'),
     ('D', 'Divorciado'),
     ('V', 'Viuvo')
     ]



    nome = models.CharField(max_length=200)
    apelido = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    data_nascimento = models.DateField(verbose_name='Data de Nascimento')
    endereco = models.CharField(max_length=200, verbose_name='Endereço')
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=51, blank=True, null=True)
    cep = models.CharField(max_length=9)
    bairro = models.CharField(max_length=100)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    estado = models.CharField(max_length=2, choices=UFS, null=True)
    estado_civil = models.CharField(max_length=1, choices=ESTADO_CIVIS, null=True)
    
    def __str__(self):
        return self.nome

    # configuração deste modelo
    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'


class Telefone(models.Model):
    TIPOS_TELEFONE = [
    ('RES', 'Residencial'),
    ('COM', 'Comercial'),
    ('REC', 'Recado'),
    ('CEL', 'Celular')
    ]
    contato = models.ForeignKey(Contato, on_delete=models.CASCADE)
    ddd = models.IntegerField()
    numero = models.CharField(max_length=10)
    tipo = models.CharField(max_length=3,choices=TIPOS_TELEFONE)
    IsWhatsapp = models.BooleanField(verbose_name="Tem Whatsapp ?")

    def __str__(self):
        return f'({self.ddd}) {self.numero}'


    



