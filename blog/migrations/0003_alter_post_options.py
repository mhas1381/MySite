# Generated by Django 3.2.11 on 2022-02-06 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20220205_2102'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_date']},
        ),
    ]