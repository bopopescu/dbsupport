# -*- coding: UTF-8 -*- 

"""
Django settings for dbsupport project.

Generated by 'django-admin startproject' using Django 1.8.17.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import pymysql
pymysql.install_as_MySQLdb()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hfusaf2m4ot#7)fkw#di2bu6(cv0@opwmafx5n#6=3d%x^hpl6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
#     'django_admin_bootstrapped.bootstrap3',
#     'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'inception',
    'user',
    'cmdb',
)

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.UnsaltedMD5PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
]

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'user.check_login_middleware.CheckLoginMiddleware',
)

ROOT_URLCONF = 'dbsupport.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'user.processor.global_info',
            ],
        },
    },
]

WSGI_APPLICATION = 'dbsupport.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'
# LANGUAGE_CODE = 'zh-cn'
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_L10N = False
DATETIME_FORMAT = 'Y-m-d H:i:s'
DATE_FORMAT = 'Y-m-d'
USE_TZ = False


STATIC_URL = '/static/'  # 别名
# STATIC_ROOT = os.path.join(BASE_DIR, 'statics')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "statics"), # 具体路径，可设置多个
]

#扩展django admin里users字段用到，指定了sql/models.py里的class users
AUTH_USER_MODEL="user.users"

# 设置session失效时间，60*30 为30分钟
SESSION_COOKIE_AGE=60*30

############以下部分需要用户根据自己环境自行修改###################

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

### dev
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dbsupport_db',
        'USER': 'dbsupportwebuser',
        'PASSWORD': 'dbsupport#2017',
        'HOST': '10.3.2.86',
        'PORT': '3306'
    }
}

#inception组件所在的地址
INCEPTION_HOST = '10.3.2.98'
INCEPTION_PORT = '6666'

#查看回滚SQL时候会用到，这里要告诉dbsupport去哪个mysql里读取inception备份的回滚信息和SQL.
#注意这里要和inception组件的inception.conf里的inception_remote_XX部分保持一致.
## dev
INCEPTION_REMOTE_BACKUP_HOST='10.3.2.86'
INCEPTION_REMOTE_BACKUP_PORT=3306
INCEPTION_REMOTE_BACKUP_USER='system'
INCEPTION_REMOTE_BACKUP_PASSWORD='111111'

#是否开启邮件提醒功能：发起SQL上线后会发送邮件提醒审核人审核，执行完毕会发送给DBA. on是开，off是关，配置为其他值均会被dbsupport认为不开启邮件功能
MAIL_ON_OFF='on'

MAIL_REVIEW_SMTP_SERVER='smtp.xxx.com'
MAIL_REVIEW_SMTP_PORT=25
MAIL_REVIEW_FROM_ADDR='db-support@xxx.com'                                               #发件人，也是登录SMTP server需要提供的用户名                                         #发件人，也是登录SMTP server需要提供的用户名
MAIL_REVIEW_FROM_PASSWORD='xxx'                                                         #发件人邮箱密码，如果为空则不需要login SMTP server
MAIL_REVIEW_DBA_ADDR=['xinpeng@xxx.com']        #DBA地址，执行完毕会发邮件给DBA，以list形式保存

#是否过滤【DROP DATABASE】|【DROP TABLE】|【TRUNCATE PARTITION】|【TRUNCATE TABLE】等高危DDL操作：
#on是开，会首先用正则表达式匹配sqlContent，如果匹配到高危DDL操作，则判断为“自动审核不通过”；off是关，直接将所有的SQL语句提交给inception，对于上述高危DDL操作，只备份元数据
CRITICAL_DDL_ON_OFF='on'
