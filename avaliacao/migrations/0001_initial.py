# Generated by Django 5.1.1 on 2024-10-14 16:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('master', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], verbose_name='Nota')),
                ('comentario', models.TextField(blank=True, null=True, verbose_name='Comentário')),
                ('criado', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
                ('servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avaliacoes', to='master.servicos')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avaliacoes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-criado'],
                'unique_together': {('usuario', 'servico')},
            },
        ),
    ]
