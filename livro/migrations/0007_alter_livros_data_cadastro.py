# Generated by Django 4.2.3 on 2023-08-02 12:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0006_alter_livros_data_devolucao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livros',
            name='data_cadastro',
            field=models.DateField(default=datetime.date(2023, 8, 2)),
        ),
    ]