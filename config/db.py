import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# psycopg2

POSTGRESQL = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dcj14bm8nuuvrt',
        'USER': 'mhfowjhcniekvh',
        'PASSWORD': '956f24b228d2c464a8036a83fd046a39b70715629c873b2e5ad93ec6bb9c8ad7',
        'HOST': 'ec2-54-86-106-48.compute-1.amazonaws.com',
        'DATABASE_PORT': '5432',
    }
}

# mysqlclient

MYSQL = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'sql_mode': 'traditional',
        }
    }
}
