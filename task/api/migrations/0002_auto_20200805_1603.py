# Generated by Django 2.2.14 on 2020-08-05 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileuploader',
            name='file',
            field=models.FileField(upload_to='files/'),
        ),
    ]
