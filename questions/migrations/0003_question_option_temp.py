# Generated by Django 3.0.2 on 2020-02-21 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_auto_20200220_2344'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='option_temp',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='GeçiciSeçenek'),
        ),
    ]
