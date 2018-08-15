# Generated by Django 2.0 on 2018-08-15 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_page',
            name='image',
            field=models.ImageField(blank=True, upload_to='blog_image/'),
        ),
        migrations.AlterField(
            model_name='blog_page',
            name='title',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='blogsite',
            name='background_image',
            field=models.ImageField(blank=True, upload_to='blogger_image/'),
        ),
        migrations.AlterField(
            model_name='blogsite',
            name='discription',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='blogsite',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='blogsite',
            name='quotes',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
