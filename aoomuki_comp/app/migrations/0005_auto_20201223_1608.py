# Generated by Django 2.1 on 2020-12-23 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20201223_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competence',
            name='commentary',
            field=models.CharField(max_length=250, verbose_name='commentaire'),
        ),
    ]