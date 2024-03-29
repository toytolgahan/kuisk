# Generated by Django 4.2 on 2023-04-12 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("discipline", "0008_news_discipline_research_teams_discipline_news"),
    ]

    operations = [
        migrations.CreateModel(
            name="EdSource",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("link", models.URLField()),
                ("body", models.TextField(blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name="discipline",
            name="key_figures",
            field=models.ManyToManyField(
                blank=True, related_name="disciplines", to="discipline.person"
            ),
        ),
        migrations.AlterField(
            model_name="discipline",
            name="parents",
            field=models.ManyToManyField(
                blank=True, related_name="disciplines", to="discipline.discipline"
            ),
        ),
        migrations.AddField(
            model_name="discipline",
            name="sources",
            field=models.ManyToManyField(
                blank=True, related_name="disciplines", to="discipline.edsource"
            ),
        ),
    ]
