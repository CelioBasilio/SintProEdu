# Generated by Django 4.0.4 on 2022-12-05 04:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mensagens',
            name='aluno',
        ),
        migrations.RemoveField(
            model_name='mensagens',
            name='empresa',
        ),
        migrations.AddField(
            model_name='mensagens',
            name='email_de',
            field=models.EmailField(default=1, max_length=50, verbose_name='email de'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mensagens',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='usuario', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mensagens',
            name='projeto',
            field=models.CharField(max_length=50, verbose_name='Projeto'),
        ),
    ]
