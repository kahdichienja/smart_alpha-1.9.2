# Generated by Django 3.0.1 on 2020-01-18 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libraryasset',
            name='subject',
            field=models.CharField(max_length=191),
        ),
    ]