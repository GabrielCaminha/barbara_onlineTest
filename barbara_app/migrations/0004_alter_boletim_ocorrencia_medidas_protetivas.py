# Generated by Django 5.1.1 on 2024-11-08 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barbara_app', '0003_boletim_ocorrencia_evidencias'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boletim_ocorrencia',
            name='medidas_protetivas',
            field=models.CharField(default='Nao necessarias', max_length=255),
        ),
    ]
