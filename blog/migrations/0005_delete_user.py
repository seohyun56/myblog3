# Generated by Django 3.0.8 on 2020-07-02 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200703_0011'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]