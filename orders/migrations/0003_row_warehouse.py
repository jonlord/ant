# Generated by Django 3.1.3 on 2020-11-16 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20201112_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='row',
            name='warehouse',
            field=models.CharField(default=0, max_length=255),
        ),
    ]
