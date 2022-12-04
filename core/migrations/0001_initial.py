# Generated by Django 4.1.3 on 2022-12-04 12:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('autenticacao', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50, verbose_name='Titulo do Projeto')),
                ('dataInicio', models.DateTimeField(auto_now_add=True, verbose_name='Data Inicial')),
                ('atualiza', models.DateTimeField(auto_now=True)),
                ('dataLimite', models.DateField(verbose_name='Data limite para conclusão')),
                ('descreva', models.TextField(verbose_name='Descreva o Projeto')),
                ('atuacao', models.CharField(choices=[('ADM', 'Administração'), ('AGR', 'Agricultura - Pecuária'), ('ALI', 'Alimentação'), ('ART', 'Artes - Arquitetura - Design'), ('VEN', 'Comercial e Vendas'), ('EXT', 'Comércio Exterior'), ('COM', 'Comunicação - Marketing'), ('CIV', 'Construção civil'), ('ECO', 'Ecologia - Meio ambiente'), ('EDU', 'Educação'), ('ELE', 'Elétrica - Eletrônica'), ('FIN', 'Financeira'), ('GEO', 'Geologia - Agrimensura'), ('HOT', 'Hotealaria - Turismo'), ('INF', 'Informatica - TI'), ('JUD', 'Jurídica'), ('MEC', 'Mecânica - Mecatronica'), ('QUI', 'Química'), ('PRO', 'Produção - Industrial'), ('SAU', 'Saúde'), ('SUP', 'Suprimentos'), ('TEL', 'Telecomunicação'), ('VET', 'Veterinária')], max_length=3, null=True, verbose_name='Área de atuação')),
                ('status', models.CharField(choices=[('P', 'Aguardado Alunos'), ('F', 'Em andamento'), ('E', 'Realizados')], max_length=1, null=True)),
                ('aluno1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='aluno1', to='autenticacao.aluno')),
                ('aluno2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='aluno2', to='autenticacao.aluno')),
                ('aluno3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='aluno3', to='autenticacao.aluno')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Mensagens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_de', models.EmailField(max_length=50, verbose_name='email de')),
                ('projeto', models.CharField(max_length=50, verbose_name='Projeto')),
                ('dataEnvio', models.DateTimeField(auto_now_add=True, verbose_name='Data de Envio')),
                ('atualiza', models.DateTimeField(auto_now=True)),
                ('mensagem', models.TextField(verbose_name='Conteúdo da mensagem')),
                ('statusMensagem', models.CharField(choices=[('P', 'Mensagem postada'), ('V', 'Mensagem Visualizada')], max_length=1, null=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='usuario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
