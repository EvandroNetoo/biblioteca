# Generated by Django 4.1.7 on 2023-02-26 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0012_alter_emprestimo_data_devolução_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emprestimo',
            name='tempo_devolução',
        ),
    ]
