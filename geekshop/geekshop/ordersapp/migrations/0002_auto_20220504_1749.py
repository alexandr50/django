# Generated by Django 3.2.6 on 2022-05-04 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_product'),
        ('ordersapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrederItem',
            new_name='OrderItem',
        ),
        migrations.AlterField(
            model_name='order',
            name='paid',
            field=models.DateTimeField(blank=True, null=True, verbose_name='оплачен'),
        ),
    ]
