# Generated by Django 4.1 on 2022-09-16 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_products_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('Author', models.CharField(max_length=100)),
                ('price', models.PositiveIntegerField()),
                ('Publisher', models.CharField(max_length=100)),
                ('qty', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.DeleteModel(
            name='Products',
        ),
    ]
