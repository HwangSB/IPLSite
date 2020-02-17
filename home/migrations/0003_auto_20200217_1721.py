# Generated by Django 3.0.2 on 2020-02-17 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200217_1719'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_image', models.ImageField(upload_to='project/project_image')),
                ('title', models.CharField(max_length=32)),
                ('detail', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Projected',
        ),
    ]