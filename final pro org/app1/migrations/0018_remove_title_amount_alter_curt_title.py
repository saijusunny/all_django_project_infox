# Generated by Django 4.0.2 on 2022-03-17 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0017_merge_0007_title_amount_0016_alter_curt_itmes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='title',
            name='amount',
        ),
        migrations.AlterField(
            model_name='curt',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]