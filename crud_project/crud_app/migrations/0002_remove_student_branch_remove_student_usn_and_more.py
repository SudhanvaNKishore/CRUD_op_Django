# Generated by Django 5.0.6 on 2024-08-30 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='branch',
        ),
        migrations.RemoveField(
            model_name='student',
            name='usn',
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=277, verbose_name='Student Email'),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Student name'),
        ),
    ]
