# Generated by Django 5.0.6 on 2024-08-13 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_remove_notes_filetype_remove_notes_notesfile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='uploadingdate',
            field=models.DateField(max_length=30),
        ),
    ]
