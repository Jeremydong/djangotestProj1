# Generated by Django 2.0 on 2018-05-13 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='姓名')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('address', models.CharField(max_length=50, verbose_name='联系地址')),
                ('message', models.CharField(max_length=200, verbose_name='留言')),
            ],
            options={
                'verbose_name_plural': '用户留言信息',
            },
        ),
    ]