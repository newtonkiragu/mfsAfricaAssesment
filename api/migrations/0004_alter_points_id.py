# Generated by Django 3.2.5 on 2021-08-01 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_points_closest_point'),
    ]

    operations = [
        migrations.AlterField(
            model_name='points',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]