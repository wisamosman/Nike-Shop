# Generated by Django 4.2.7 on 2023-11-09 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='image',
            field=models.ImageField(default=1, upload_to='orders'),
            preserve_default=False,
        ),
    ]