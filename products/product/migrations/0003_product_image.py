# Generated by Django 2.2.2 on 2019-06-10 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20190606_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='products/'),
        ),
    ]
