# Generated by Django 2.2.3 on 2020-03-02 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200302_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_img',
            field=models.ImageField(upload_to='profile_pics'),
        ),
    ]
