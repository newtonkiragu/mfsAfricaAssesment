# Generated by Django 3.2.5 on 2021-07-31 08:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='points',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='points',
            name='string_of_csv',
            field=models.TextField(max_length=500),
        ),
    ]
