# Generated by Django 4.2.6 on 2024-01-13 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_manager', '0002_alter_centre_codecntr_alter_client_codecl_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fournisseur',
            name='Solde',
        ),
        migrations.AddField(
            model_name='achats',
            name='Solde',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
    ]
