# Generated by Django 3.1.7 on 2021-03-22 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artworks', '0009_auto_20210322_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]