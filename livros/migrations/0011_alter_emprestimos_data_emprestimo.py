# Generated by Django 5.1.2 on 2024-11-03 16:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0010_alter_emprestimos_data_emprestimo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimos',
            name='data_emprestimo',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
