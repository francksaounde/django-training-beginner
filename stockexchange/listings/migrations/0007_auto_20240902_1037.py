# Generated by Django 3.1.7 on 2024-09-02 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0006_band_active_band_biography_band_genre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
