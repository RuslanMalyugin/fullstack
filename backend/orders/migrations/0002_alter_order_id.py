# Generated by Django 4.0.1 on 2022-01-11 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]
