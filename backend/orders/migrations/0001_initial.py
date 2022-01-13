# Generated by Django 4.0.1 on 2022-01-11 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('specialization', models.CharField(default='', max_length=100)),
                ('name', models.CharField(default='', max_length=100)),
                ('date', models.CharField(default='', max_length=100)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
    ]