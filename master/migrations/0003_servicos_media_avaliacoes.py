# Generated by Django 5.1.1 on 2024-11-26 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0002_servicos_prestador'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicos',
            name='media_avaliacoes',
            field=models.FloatField(default=0.0, verbose_name='Média das Avaliações'),
        ),
    ]