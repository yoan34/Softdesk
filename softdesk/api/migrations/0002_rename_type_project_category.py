# Generated by Django 3.2.4 on 2021-06-13 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='type',
            new_name='category',
        ),
    ]
