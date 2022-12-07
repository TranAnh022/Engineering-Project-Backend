# Generated by Django 4.1.3 on 2022-11-29 23:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('composition', '0005_alter_compositions_material'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compositions',
            name='material',
        ),
        migrations.AddField(
            model_name='materials',
            name='compositions',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='composition.compositions'),
        ),
    ]