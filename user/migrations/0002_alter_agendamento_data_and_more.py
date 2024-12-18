# Generated by Django 5.1.1 on 2024-10-15 13:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendamento',
            name='data',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='agendamento',
            name='destinatario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mensagens_recebidas', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='agendamento',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='agendamento',
            name='remetente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mensagens_enviadas', to=settings.AUTH_USER_MODEL),
        ),
    ]
