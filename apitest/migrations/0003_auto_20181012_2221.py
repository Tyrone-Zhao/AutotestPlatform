# Generated by Django 2.0.7 on 2018-10-12 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apitest', '0002_auto_20181012_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apistep',
            name='apiresponse',
            field=models.CharField(blank=True, max_length=5000, verbose_name='响应数据'),
        ),
        migrations.AlterField(
            model_name='apistep',
            name='apistep',
            field=models.CharField(blank=True, max_length=100, verbose_name='测试步骤'),
        ),
    ]
