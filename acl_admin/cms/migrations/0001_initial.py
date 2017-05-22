# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ACL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('vlan', models.IntegerField(verbose_name='vlan番号', blank=True, default=0)),
                ('protocol', models.CharField(max_length=15, verbose_name='プロトコル')),
                ('src_ip', models.CharField(max_length=64, verbose_name='送信元IP')),
                ('src_wc', models.CharField(max_length=64, verbose_name='送信元ワイルドカード')),
                ('src_port', models.CharField(max_length=64, verbose_name='送信元ポート番号')),
                ('dst_ip', models.CharField(max_length=64, verbose_name='宛先IP')),
                ('dst_wc', models.CharField(max_length=64, verbose_name='宛先ワイルドカード')),
                ('dst_port', models.CharField(max_length=64, verbose_name='宛先ポート番号')),
            ],
        ),
    ]
