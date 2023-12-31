# Generated by Django 5.0 on 2023-12-23 10:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0002_questionnaire_questionnairename'),
    ]

    operations = [
        migrations.AlterField(
            model_name='option',
            name='id_Question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Options', to='Quiz.question'),
        ),
        migrations.AlterField(
            model_name='question',
            name='id_Questionnaire',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Questions', to='Quiz.questionnaire'),
        ),
    ]
