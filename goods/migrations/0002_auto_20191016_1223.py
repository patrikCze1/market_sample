# Generated by Django 2.2.6 on 2019-10-16 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='offer_id',
            new_name='offer',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='product_id',
            new_name='offer',
        ),
        migrations.RenameField(
            model_name='offer',
            old_name='user_id',
            new_name='user',
        ),
    ]
