# Generated by Django 2.0.1 on 2018-01-19 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='preview',
            field=models.TextField(default='t'),
            preserve_default=False,
        ),
    ]
