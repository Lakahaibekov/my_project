# Generated by Django 2.2.7 on 2019-12-08 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myFirstApp', '0003_auto_20191209_0437'),
    ]

    operations = [
        migrations.AddField(
            model_name='send',
            name='name_course',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
