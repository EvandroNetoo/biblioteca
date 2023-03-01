from django.db import models
from datetime import date, timedelta
from usuarios.models import Usuario


class Categoria(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.TextField()
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nome


class Livros(models.Model):
    img = models.ImageField(upload_to='capa_livro', null=True, default=True)
    nome = models.CharField(max_length=100)
    autor = models.CharField(max_length=30)
    co_autor = models.CharField(max_length=30, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    emprestado = models.BooleanField(default=False)
    data_cadastro = models.DateField(default=date.today)


    class Meta:
        verbose_name = 'Livro'

    def __str__(self):
        return self.nome


class Emprestimo(models.Model):
    choices = (
        ('PE', 'Péssimo'),
        ('RU', 'Ruim'),
        ('RE', 'Regular'),
        ('BO', 'Bom'),
        ('OT', 'Ótimo'),

    )
    livro = models.ForeignKey(Livros, on_delete=models.DO_NOTHING)
    nome_emprestado = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING, blank=True, null=True)
    nome_emprestado_anonimo = models.CharField(max_length=30, blank=True, null=True)
    data_emprestimo = models.DateField(default=date.today)
    data_devolucao = models.DateField(blank=True, null=True)
    avaliacao = models.CharField(max_length=2, choices=choices, blank=True, null=True)

    def __str__(self):
        if not self.nome_emprestado_anonimo:
            return f'{self.nome_emprestado} | {self.livro}'
        else:
            return f'{self.nome_emprestado_anonimo} | {self.livro}'
