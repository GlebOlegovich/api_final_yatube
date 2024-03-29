# Generated by Django 2.2.16 on 2021-10-19 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20211019_1210'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='group',
            field=models.ForeignKey(blank=True, help_text='Группа, в которой будет пост', null=True, on_delete=django.db.models.deletion.SET_NULL, to='posts.Group', verbose_name='Группа'),
        ),
    ]
