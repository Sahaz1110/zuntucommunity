# Generated by Django 5.0.6 on 2024-08-30 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_remove_student_address_remove_student_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='gender',
        ),
        migrations.AddField(
            model_name='student',
            name='address',
            field=models.CharField(default='Unknown Address', max_length=255),
        ),
        migrations.AddField(
            model_name='student',
            name='class_of_student',
            field=models.CharField(default='Class 1', max_length=50),
        ),
        migrations.AddField(
            model_name='student',
            name='local_government',
            field=models.CharField(default='Unknown LGA', max_length=100),
        ),
        migrations.AddField(
            model_name='student',
            name='nationality',
            field=models.CharField(default='Unknown', max_length=50),
        ),
        migrations.AddField(
            model_name='student',
            name='parent_phone_number',
            field=models.CharField(default='0000000000', max_length=15),
        ),
        migrations.AddField(
            model_name='student',
            name='phone_number',
            field=models.CharField(default='0000000000', max_length=15),
        ),
        migrations.AddField(
            model_name='student',
            name='religion',
            field=models.CharField(default='Unknown Religion', max_length=50),
        ),
        migrations.AddField(
            model_name='student',
            name='state',
            field=models.CharField(default='Unknown State', max_length=50),
        ),
    ]
