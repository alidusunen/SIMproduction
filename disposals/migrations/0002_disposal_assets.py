# Generated by Django 3.0.5 on 2020-04-23 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0009_auto_20200424_0012'),
        ('disposals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='disposal',
            name='assets',
            field=models.ManyToManyField(to='assets.Asset'),
        ),
    ]
