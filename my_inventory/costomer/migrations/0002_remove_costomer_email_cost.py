# Generated by Django 4.1.2 on 2022-10-31 23:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('costomer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='costomer',
            name='email_cost',
        ),
    ]
