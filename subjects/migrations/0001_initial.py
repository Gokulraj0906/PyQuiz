# Generated by Django 4.0.1 on 2022-03-09 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chemistry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter', models.CharField(max_length=700)),
            ],
        ),
        migrations.CreateModel(
            name='ChemistryEasy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=2083)),
                ('chemistry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subjects.chemistry')),
            ],
        ),
        migrations.CreateModel(
            name='ChemistryHard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=2083)),
                ('chemistry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subjects.chemistry')),
            ],
        ),
        migrations.CreateModel(
            name='ChemistryMedium',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=2083)),
                ('chemistry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subjects.chemistry')),
            ],
        ),
        migrations.CreateModel(
            name='ChemistryMediumOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('options', models.CharField(max_length=2083)),
                ('answer', models.BooleanField()),
                ('chemistry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subjects.chemistrymedium')),
            ],
        ),
        migrations.CreateModel(
            name='ChemistryHardOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('options', models.CharField(max_length=2083)),
                ('answer', models.BooleanField()),
                ('chemistry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subjects.chemistryhard')),
            ],
        ),
        migrations.CreateModel(
            name='ChemistryEasyOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('options', models.CharField(max_length=2083)),
                ('answer', models.BooleanField()),
                ('chemistry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subjects.chemistryeasy')),
            ],
        ),
    ]