# Generated by Django 4.2.3 on 2023-10-07 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipa', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parkings',
            name='cordinate',
        ),
        migrations.AddField(
            model_name='parkings',
            name='latitude',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='parkings',
            name='longitude',
            field=models.IntegerField(null=True),
        ),
    ]
