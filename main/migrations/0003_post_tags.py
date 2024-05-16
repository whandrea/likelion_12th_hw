# Generated by Django 5.0.3 on 2024-05-16 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_tag_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='blogs', to='main.tag'),
        ),
    ]
