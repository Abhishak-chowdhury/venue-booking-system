# Generated by Django 4.2.1 on 2023-08-20 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_book_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='end_date',
            field=models.DateField(blank=True, null=True, verbose_name='end date'),
        ),
        migrations.AlterField(
            model_name='book',
            name='from_date',
            field=models.DateField(blank=True, null=True, verbose_name='booking date'),
        ),
    ]
