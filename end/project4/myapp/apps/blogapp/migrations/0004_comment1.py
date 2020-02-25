# Generated by Django 3.0.3 on 2020-02-25 04:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_remove_comment_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='评论人')),
                ('url', models.URLField(default='http://www.rcc.com', verbose_name='个人主页')),
                ('email', models.EmailField(default='1326729135@qq.com', max_length=254, verbose_name='邮箱')),
                ('num', models.PositiveIntegerField(default=3214, verbose_name='验证码')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='评论时间')),
                ('body', models.CharField(max_length=100, verbose_name='内容')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.Article', verbose_name='所属文章')),
            ],
        ),
    ]