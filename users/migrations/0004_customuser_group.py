# Generated by Django 3.0 on 2020-02-15 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200206_1309'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='group',
            field=models.CharField(default='Developer', max_length=50),
        ),
    ]