# Generated by Django 4.2.6 on 2023-10-26 06:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authe', '0002_boolmodel_model_charfield_model_datafield_model_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='constraints',
            fields=[
                ('ID', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('phone', models.PositiveBigIntegerField(unique=True)),
                ('age', models.PositiveSmallIntegerField(null=True)),
                ('email', models.EmailField(max_length=30)),
                ('gender', models.CharField(default='MALE', max_length=10)),
                ('subject', models.CharField(choices=[['django', 'django'], ['python', 'python']], max_length=20)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authe.client')),
            ],
        ),
    ]
