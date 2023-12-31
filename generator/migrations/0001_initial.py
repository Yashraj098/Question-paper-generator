# Generated by Django 4.1.7 on 2023-11-23 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField()),
                ('subject', models.CharField(max_length=255)),
                ('topic', models.CharField(max_length=255)),
                ('difficulty', models.CharField(max_length=10)),
                ('marks', models.IntegerField()),
            ],
        ),
    ]
