# Generated by Django 4.2.9 on 2024-01-15 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='dfd', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
