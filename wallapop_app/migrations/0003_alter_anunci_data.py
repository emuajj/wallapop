# Generated by Django 4.1 on 2023-02-28 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallapop_app', '0002_alter_comentari_data_com'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anunci',
            name='data',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]