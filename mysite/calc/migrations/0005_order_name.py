# Generated by Django 4.0.3 on 2022-04-07 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0004_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='name',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
