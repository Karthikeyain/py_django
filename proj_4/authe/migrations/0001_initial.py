# Generated by Django 4.2.6 on 2023-10-20 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=50)),
                ('cage', models.PositiveIntegerField(verbose_name=3)),
                ('cphone', models.PositiveBigIntegerField()),
                ('cadd', models.CharField(max_length=100)),
                ('cfees', models.PositiveBigIntegerField()),
            ],
        ),
    ]
