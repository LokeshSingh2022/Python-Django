# Generated by Django 4.0.6 on 2022-07-30 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geolocation', '0003_remove_userdetail_id_userdetail_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='Id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]