# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-16 11:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import utils.AesCharField


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dbinstance',
            name='host',
            field=models.ForeignKey(db_column='host', db_index=False, help_text='请选择主机', on_delete=django.db.models.deletion.DO_NOTHING, to='cmdb.host', verbose_name='主机'),
        ),
        migrations.AlterField(
            model_name='host',
            name='hostRole',
            field=models.CharField(choices=[('GENERAL', 'GENERAL'), ('MASTER', 'MASTER'), ('SLAVE', 'SLAVE')], db_column='host_role', default='GENERAL', help_text='请输入服务器角色!', max_length=32, verbose_name='服务器角色'),
        ),
        migrations.AlterField(
            model_name='host',
            name='hostType',
            field=models.CharField(choices=[('DB', 'DB'), ('WEB', 'WEB'), ('REDIS', 'REDIS'), ('NGINX', 'NGINX')], db_column='host_type', default='WEB', help_text='请输入服务器类型!', max_length=32, verbose_name='服务器类型'),
        ),
        migrations.AlterField(
            model_name='hostuser',
            name='host',
            field=models.ForeignKey(db_column='host', db_index=False, help_text='请选择主机！', on_delete=django.db.models.deletion.DO_NOTHING, to='cmdb.host', verbose_name='主机'),
        ),
        migrations.AlterField(
            model_name='hostuser',
            name='hostPasswd',
            field=utils.AesCharField.AesCharField(db_column='host_passwd', max_length=300, verbose_name='操作系统密码'),
        ),
    ]
