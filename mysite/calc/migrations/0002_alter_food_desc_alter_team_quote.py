# Generated by Django 4.0.3 on 2022-04-01 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='desc',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='team',
            name='quote',
            field=models.TextField(),
        ),
    ]
