# Generated by Django 2.2.14 on 2020-08-05 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileUploader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('name', models.CharField(max_length=100)),
                ('upload_date', models.DateTimeField(auto_now=True, db_index=True)),
                ('file_type', models.CharField(blank=True, max_length=50, null=True)),
                ('file_path', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
