# Generated by Django 4.2.5 on 2023-09-26 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Craftapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='brewery',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
