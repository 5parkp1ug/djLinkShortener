# Generated by Django 2.2.14 on 2020-07-21 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='link',
            name='title',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='link',
            name='description',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
