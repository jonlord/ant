# Generated by Django 3.1.3 on 2020-11-11 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=255)),
                ('client', models.CharField(max_length=255)),
                ('marketplace', models.CharField(max_length=255)),
                ('eurozone', models.IntegerField()),
                ('status', models.CharField(max_length=255)),
                ('read', models.BooleanField(default=False)),
                ('processed', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Row',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_reference', models.CharField(max_length=255)),
                ('color_reference', models.CharField(max_length=255)),
                ('size_position', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=4, max_digits=10)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
            ],
        ),
    ]