# Generated by Django 4.1.1 on 2023-03-03 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buyurtma',
            old_name='name_ru',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='buyurtma',
            name='name_uz',
        ),
    ]
