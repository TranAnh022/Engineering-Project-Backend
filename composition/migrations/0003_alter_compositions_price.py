# Generated by Django 4.1.3 on 2022-11-22 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('composition', '0002_compositions_date_compositions_percentage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compositions',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
    ]
