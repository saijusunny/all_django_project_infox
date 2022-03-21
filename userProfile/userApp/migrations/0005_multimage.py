# Generated by Django 4.0.1 on 2022-03-06 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0004_title_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='multimage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('multimage', models.ImageField(blank=True, null=True, upload_to='multi/image')),
                ('price', models.IntegerField()),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userApp.category')),
            ],
        ),
    ]