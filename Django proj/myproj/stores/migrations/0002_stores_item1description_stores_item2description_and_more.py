# Generated by Django 5.0.6 on 2024-07-04 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stores',
            name='item1description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stores',
            name='item2description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stores',
            name='item3description',
            field=models.TextField(blank=True, null=True),
        ),
    ]