# Generated by Django 4.0.4 on 2022-05-16 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SocialApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='userName',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
