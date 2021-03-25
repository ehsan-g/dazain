# Generated by Django 3.1.7 on 2021-03-22 21:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('artworks', '0004_auto_20210322_2044'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='shippigPrice',
            new_name='taxPrice',
        ),
        migrations.RemoveField(
            model_name='artwork',
            name='description',
        ),
        migrations.AddField(
            model_name='artwork',
            name='aboutWork',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='artwork',
            name='image',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='artwork',
            name='provenance',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='artwork',
            name='workName',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='artwork',
            name='frame',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('postalcode', models.CharField(blank=True, max_length=200, null=True)),
                ('country', models.CharField(blank=True, max_length=200, null=True)),
                ('shippingPrice', models.DecimalField(blank=True, decimal_places=0, max_digits=7, null=True)),
                ('order', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='artworks.order')),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('artwork', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='artworks.artwork')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]