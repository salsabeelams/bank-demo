# Generated by Django 4.1.7 on 2023-09-04 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='account_type',
            field=models.CharField(default='Savings', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='person',
            name='branch',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='district',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone',
            field=models.CharField(max_length=150),
        ),
    ]
