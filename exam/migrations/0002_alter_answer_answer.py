# Generated by Django 3.2.3 on 2021-09-11 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer',
            field=models.TextField(blank=True, null=True),
        ),
    ]
