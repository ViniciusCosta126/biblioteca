# Generated by Django 4.2.3 on 2023-08-02 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0008_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='livros',
            name='categoria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='livro.categoria'),
            preserve_default=False,
        ),
    ]
