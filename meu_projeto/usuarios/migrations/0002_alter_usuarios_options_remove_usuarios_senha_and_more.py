# Generated by Django 5.1.1 on 2024-10-15 18:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usuarios',
            options={'verbose_name': 'Usuário', 'verbose_name_plural': 'Usuários'},
        ),
        migrations.RemoveField(
            model_name='usuarios',
            name='senha',
        ),
        migrations.AddField(
            model_name='usuarios',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='usuarios',
            name='mensagem',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='usuarios',
            name='profissao',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='idade',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(150)]),
        ),
    ]
