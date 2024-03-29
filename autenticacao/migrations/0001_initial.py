# Generated by Django 4.0.4 on 2022-12-05 02:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Atuacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('atuacao', models.CharField(max_length=5, null=True, unique=True, verbose_name='atuacao')),
            ],
        ),
        migrations.CreateModel(
            name='Bairro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bairro', models.CharField(max_length=30, null=True, unique=True, verbose_name='bairro')),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=2, null=True, unique=True, verbose_name='estado')),
            ],
        ),
        migrations.CreateModel(
            name='Universidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instituicao', models.CharField(max_length=100, null=True, unique=True, verbose_name='instituicao')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='autenticacao.estado')),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rua', models.CharField(max_length=200, null=True, unique=True, verbose_name='rua')),
                ('cep', models.CharField(max_length=9, null=True, unique=True, verbose_name='cep')),
                ('bairro', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='autenticacao.bairro')),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.CharField(max_length=18, null=True, unique=True, verbose_name='cnpj')),
                ('representante', models.CharField(max_length=50, null=True, verbose_name='representante')),
                ('atuacao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='autenticacao.atuacao')),
                ('endereco', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='autenticacao.endereco')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Complemento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=5, null=True, verbose_name='numero')),
                ('complemento', models.CharField(max_length=50, null=True, verbose_name='complemento')),
                ('endereco', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='autenticacao.endereco')),
            ],
        ),
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cidade', models.CharField(max_length=30, null=True, verbose_name='cidade')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autenticacao.estado')),
            ],
        ),
        migrations.AddField(
            model_name='bairro',
            name='cidade',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='autenticacao.cidade'),
        ),
        migrations.CreateModel(
            name='Ativacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=128)),
                ('ativo', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(blank=True, max_length=14, null=True, unique=True, verbose_name='cpf')),
                ('atuacao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='autenticacao.atuacao')),
                ('endereco', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='autenticacao.endereco')),
                ('instituicao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='autenticacao.universidades')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
