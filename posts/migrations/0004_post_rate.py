# Generated by Django 5.0.6 on 2024-07-09 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='rate',
            field=models.IntegerField(default=0),
        ),
    ]
