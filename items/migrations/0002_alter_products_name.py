# Generated by Django 5.0.2 on 2024-02-23 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
