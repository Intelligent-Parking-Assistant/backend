# Generated by Django 4.2.3 on 2023-10-28 03:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ipa', '0003_alter_parkings_latitude_alter_parkings_longitude'),
    ]

    operations = [
        migrations.CreateModel(
            name='Free',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('free', models.IntegerField()),
                ('parking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ipa.parkings')),
            ],
        ),
    ]
