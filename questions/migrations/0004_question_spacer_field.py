# Generated by Django 3.0.2 on 2020-02-25 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_question_option_temp'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='spacer_field',
            field=models.CharField(default=10, max_length=10, verbose_name='Ara boşluk'),
        ),
    ]
