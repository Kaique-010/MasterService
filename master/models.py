from django.db import models

class Base(models.Model):
    criado = models.DateField('Data de Criação', auto_now_add=True) 
    modificado = models.DateTimeField('Data de Modificação', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True  



class Categoria(Base):
    nome = models.CharField('Nome da Categoria', max_length=50)

    def __str__(self):
        return self.nome

class Grupo(Base):
    nome = models.CharField('Nome do Grupo', max_length=50)
    categoria = models.ForeignKey(Categoria, related_name='grupos', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Especialidade(Base):
    nome = models.CharField('Nome da Especialidade', max_length=50)
    grupo = models.ForeignKey(Grupo, related_name='especialidades', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Servicos(Base):
    titulo = models.CharField('Título do Serviço', max_length=50)
    categoria = models.ForeignKey(Categoria, related_name='servicos', on_delete=models.CASCADE)
    grupo = models.ForeignKey(Grupo, related_name='servicos', on_delete=models.CASCADE)
    especialidade = models.ForeignKey(Especialidade, related_name='servicos', on_delete=models.CASCADE)
    observacoes_uteis = models.TextField('Observações Úteis', max_length=100, blank=True, null=True)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['id', 'titulo']
        verbose_name = 'Serviço'  
        verbose_name_plural = 'Serviços'
