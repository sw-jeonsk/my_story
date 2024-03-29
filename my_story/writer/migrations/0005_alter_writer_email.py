# Generated by Django 3.2.4 on 2021-08-09 06:24

from django.db import migrations
import utils.custom_field


class Migration(migrations.Migration):

    dependencies = [
        ('writer', '0004_alter_writer_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='writer',
            name='email',
            field=utils.custom_field.CaseLowerEmailField(help_text='writer login ID', max_length=64, unique=True, verbose_name='이메일'),
        ),
    ]
