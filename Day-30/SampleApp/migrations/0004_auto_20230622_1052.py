# Generated by Django 3.0 on 2023-06-22 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SampleApp', '0003_auto_20230619_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='sage',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='sbranch',
            field=models.CharField(choices=[('0', 'Select Branch'), ('CSE', 'Computer Science and Engineering'), ('ECE', 'Electrical and Communication Engineering')], default='0', max_length=5),
        ),
        migrations.AlterField(
            model_name='student',
            name='syear',
            field=models.IntegerField(choices=[(1, '1st Year'), (2, '2nd Year'), (3, '3rd Year'), (4, '4th Year')], default=1, max_length=2),
        ),
    ]