# Generated by Django 3.1.6 on 2021-02-12 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=26)),
                ('Email', models.EmailField(max_length=254)),
                ('HomeTowm', models.CharField(max_length=29)),
                ('profile_pic', models.ImageField(blank=True, upload_to='profile_pic')),
            ],
        ),
    ]
