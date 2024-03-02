# Generated by Django 3.2 on 2024-02-17 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='streg',
            name='sbranch',
            field=models.CharField(choices=[('0', '--Select Branch--'), ('1', 'CSE'), ('2', 'CSM'), ('3', 'CSO'), ('4', 'IT'), ('5', 'Other')], default='0', max_length=5),
        ),
    ]
