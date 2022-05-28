# Generated by Django 4.0.4 on 2022-05-28 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posting', '0002_alter_like_reaction_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='reaction_type',
            field=models.SmallIntegerField(blank=True, choices=[(1, 'Like'), (2, 'Heart'), (3, 'Angry'), (4, 'Haha')], null=True),
        ),
    ]
