# Generated by Django 3.2.5 on 2021-08-26 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0009_auto_20210826_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='importance',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.importance'),
        ),
    ]
