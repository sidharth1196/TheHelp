# Generated by Django 2.2.7 on 2019-12-09 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WorkOrder', '0002_order'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]
