# Generated by Django 4.1 on 2022-10-17 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_alter_rabota_project_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rabota',
            name='step1',
            field=models.CharField(blank=True, max_length=249, null=True, verbose_name='Шаг 1'),
        ),
    ]
