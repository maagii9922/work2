# Generated by Django 3.1.7 on 2021-03-12 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work1', '0003_auto_20210228_1501'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tohirgoo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=300)),
            ],
        ),
    ]