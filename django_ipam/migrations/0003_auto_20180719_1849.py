# Generated by Django 2.0.5 on 2018-07-19 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_ipam', '0002_auto_20180713_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subnet',
            name='name',
            field=models.CharField(blank=True, db_index=True, max_length=100),
        ),
    ]