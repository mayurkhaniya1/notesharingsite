# Generated by Django 5.0.6 on 2024-08-13 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_alter_notes_uploadingdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='uploadingdate',
            field=models.DateField(auto_now_add=True),
        ),
    ]