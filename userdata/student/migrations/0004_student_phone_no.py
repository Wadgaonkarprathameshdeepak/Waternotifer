# Generated by Django 4.1.7 on 2023-02-18 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_remove_student_phone_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='phone_no',
            field=models.IntegerField(default=0),
        ),
    ]
