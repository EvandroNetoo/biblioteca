# Generated by Django 4.1.7 on 2023-02-28 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0015_livros_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='emprestimo',
            name='avaliacao',
            field=models.CharField(choices=[('PE', 'Péssimo'), ('RU', 'Ruim'), ('RE', 'Regular'), ('BO', 'Bom'), ('OT', 'Ótimo')], default=1, max_length=2),
            preserve_default=False,
        ),
    ]
