# Generated by Django 4.2.6 on 2024-01-06 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='centre',
            name='CodeCNTR',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='client',
            name='CodeCL',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='employe',
            name='CodeEMP',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='fournisseur',
            name='CodeF',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='produit',
            name='CodeP',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
