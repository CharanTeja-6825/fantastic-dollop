# Generated by Django 5.1.2 on 2024-10-26 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0004_remove_course_title_remove_course_updated_at_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Course',
        ),
    ]