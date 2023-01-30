# Generated by Django 3.2.5 on 2021-08-26 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0008_alter_importance_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='importance',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='task',
            name='importance',
            field=models.ForeignKey(default='normal', null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.importance'),
        ),
    ]