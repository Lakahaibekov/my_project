# Generated by Django 2.2.7 on 2019-12-08 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myFirstApp', '0002_auto_20191209_0032'),
    ]

    operations = [
        migrations.CreateModel(
            name='Send',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_student', models.CharField(max_length=50)),
                ('name_teacher', models.CharField(max_length=50)),
                ('phone_student', models.CharField(max_length=50)),
                ('grade_student', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
