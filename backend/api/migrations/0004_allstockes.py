# Generated by Django 3.1.7 on 2021-05-30 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api', '0003_delete_blogpost'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllStockes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]