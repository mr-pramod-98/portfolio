# Generated by Django 3.0.8 on 2020-07-19 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0008_groupprojects_personalprojects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupprojects',
            name='duration',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]