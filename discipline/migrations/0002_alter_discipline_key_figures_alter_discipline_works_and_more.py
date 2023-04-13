# Generated by Django 4.2 on 2023-04-11 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("discipline", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="discipline",
            name="key_figures",
            field=models.ManyToManyField(
                blank=True, related_name="key_figures", to="discipline.person"
            ),
        ),
        migrations.AlterField(
            model_name="discipline",
            name="works",
            field=models.ManyToManyField(
                blank=True, related_name="disciplines", to="discipline.work"
            ),
        ),
        migrations.AlterField(
            model_name="team",
            name="members",
            field=models.ManyToManyField(
                blank=True, related_name="teams", to="discipline.person"
            ),
        ),
        migrations.AlterField(
            model_name="work",
            name="authors",
            field=models.ManyToManyField(
                blank=True, related_name="works", to="discipline.person"
            ),
        ),
    ]
