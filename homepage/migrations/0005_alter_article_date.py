# Generated by Django 5.1.7 on 2025-04-10 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_rename_artikel_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateField(),
        ),
    ]
