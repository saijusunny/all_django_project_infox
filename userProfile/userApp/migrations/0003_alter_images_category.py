# Generated by Django 4.0.1 on 2022-03-06 06:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0002_category_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userApp.category'),
        ),
    ]
