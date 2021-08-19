# Generated by Django 3.2.5 on 2021-08-18 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='branch',
            field=models.ForeignKey(blank=True, limit_choices_to={'colleges': 'self.college'}, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='students', to='college.branch'),
        ),
        migrations.AlterField(
            model_name='user',
            name='college',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='students', to='college.college'),
        ),
        migrations.AlterField(
            model_name='user',
            name='year',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='students', to='college.year'),
        ),
    ]
