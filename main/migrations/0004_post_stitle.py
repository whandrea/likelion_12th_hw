# Generated by Django 5.0.3 on 2024-04-29 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_blog_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='stitle',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]