# Generated by Django 2.2.3 on 2020-03-03 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200303_0256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_img',
            field=models.ImageField(default='20190624_185414.jpg', upload_to='profile_pics'),
        ),
    ]
