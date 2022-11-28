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
        'NAME': 'de8sc60cg54664',
        'USER': 'qihtfwffrbngpb',
        'PASSWORD': 'bd065f230d72e8cf4ce9593bb3b3eb0d9d5890c22234685ec1ba43f87ff77d4a',
        'HOST': 'ec2-3-229-161-70.compute-1.amazonaws.com',
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
