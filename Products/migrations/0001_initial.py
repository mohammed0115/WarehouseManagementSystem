# Generated by Django 3.0.6 on 2020-09-06 03:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='category name')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categorys',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Product Name')),
                ('p_type', models.CharField(max_length=50, verbose_name='Product Type')),
                ('sale_price', models.IntegerField(verbose_name='Sale price')),
                ('p_cost', models.IntegerField(verbose_name='Product cost')),
                ('serial_number', models.CharField(max_length=50, verbose_name='serial number')),
                ('company', models.CharField(max_length=50, verbose_name='company production')),
                ('product_created', models.DateField(verbose_name='date create')),
                ('product_end', models.DateField(verbose_name='End date')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.Category', verbose_name='Category type')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 's',
            },
        ),
    ]