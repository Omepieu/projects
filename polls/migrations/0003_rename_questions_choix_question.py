# Generated by Django 4.0 on 2023-08-15 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_rename_question_choix_questions'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choix',
            old_name='questions',
            new_name='question',
        ),
    ]