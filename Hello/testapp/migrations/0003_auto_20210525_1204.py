# Generated by Django 3.2.3 on 2021-05-25 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_auto_20210525_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='desc',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(max_length=65),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=10),
        ),
    ]