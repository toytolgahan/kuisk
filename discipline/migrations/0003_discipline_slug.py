# Generated by Django 4.2 on 2023-04-11 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "discipline",
            "0002_alter_discipline_key_figures_alter_discipline_works_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="discipline",
            name="slug",
            field=models.SlugField(default=1, unique=True),
            preserve_default=False,
        ),
    ]
