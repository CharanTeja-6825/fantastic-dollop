# Generated by Django 5.1.2 on 2024-10-28 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0009_alter_course_trainer_trainer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='trainer',
        ),
        migrations.DeleteModel(
            name='Trainer',
        ),
    ]
