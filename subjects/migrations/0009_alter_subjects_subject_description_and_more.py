# Generated by Django 5.1.1 on 2024-09-26 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0008_alter_subjects_subject_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjects',
            name='subject_description',
            field=models.TextField(help_text='max 60 character', max_length=60),
        ),
        migrations.AlterField(
            model_name='subjects',
            name='subject_name',
            field=models.CharField(help_text='max 10 character', max_length=10),
        ),
    ]
