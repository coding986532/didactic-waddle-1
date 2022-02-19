# Generated by Django 4.0.2 on 2022-02-19 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0012_driveuploader_dropbox_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driveuploader',
            name='Dropbox_Link',
            field=models.CharField(blank=True, choices=[('dropbox.com', 'dropbox.com')], help_text='If file is on Dropbox,select dropbox.com, otherwise leave blank.', max_length=25),
        ),
        migrations.AlterField(
            model_name='driveuploader',
            name='drive_file_link',
            field=models.URLField(blank=True, help_text='If file is on Dropbox, go to Dropbox Link and select dropbox.com. Otherwise, leave "Dropbox Link" blank.', max_length=1000),
        ),
    ]