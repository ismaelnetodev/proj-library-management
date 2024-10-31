# Generated by Django 5.1.2 on 2024-10-31 12:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0003_alter_livros_data_devolucao_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='livros',
            name='cartegoria',
        ),
        migrations.AddField(
            model_name='livros',
            name='categoria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='livros.categoria'),
            preserve_default=False,
        ),
    ]