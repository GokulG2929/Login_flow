# Generated by Django 4.2.7 on 2023-12-10 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_alter_register_date_alter_register_modified_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='age',
            new_name='user_id',
        ),
    ]