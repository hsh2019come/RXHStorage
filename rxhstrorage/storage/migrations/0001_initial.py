# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-07-07 06:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='原材料名称')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='数量')),
                ('update_data', models.DateTimeField(auto_now=True, null=True, verbose_name='数据变更时间')),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='位置')),
            ],
        ),
        migrations.CreateModel(
            name='StorageRack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(verbose_name='货架号')),
            ],
        ),
        migrations.AddField(
            model_name='material',
            name='pos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storage.Position', verbose_name='位置'),
        ),
        migrations.AddField(
            model_name='material',
            name='storage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storage.StorageRack', verbose_name='货架'),
        ),
    ]