# Generated by Django 3.0 on 2020-02-14 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bug', '0004_delete_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug',
            name='bug_status',
            field=models.CharField(default='Pending', max_length=50),
        ),
    ]
