# Generated by Django 5.0.3 on 2024-07-19 03:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_tag_project_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='tag',
            new_name='tags',
        ),
    ]