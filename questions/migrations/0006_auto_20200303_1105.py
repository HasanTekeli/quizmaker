# Generated by Django 3.0.2 on 2020-03-03 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0005_remove_question_spacer_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='ydl',
            field=models.CharField(choices=[('183', '183'), ('184', '184'), ('185', '185 Önlisans'), ('185L', '185 Lisans'), ('186', '186 Önlisans'), ('186L', '186 Lisans')], max_length=4, null=True, verbose_name='YDL183,184,etc.'),
        ),
    ]
