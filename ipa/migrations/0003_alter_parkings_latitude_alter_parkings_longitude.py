# Generated by Django 4.2.3 on 2023-10-08 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipa', '0002_remove_parkings_cordinate_parkings_latitude_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parkings',
            name='latitude',
            field=models.DecimalField(decimal_places=6, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='parkings',
            name='longitude',
            field=models.DecimalField(decimal_places=6, max_digits=10, null=True),
        ),
    ]
