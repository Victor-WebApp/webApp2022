# Generated by Django 3.2.3 on 2022-04-14 02:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('acknowledgementReceipt', '0002_alter_registration_usertype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='proponents',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='acknowledgementReceipt.application'),
        ),
    ]
