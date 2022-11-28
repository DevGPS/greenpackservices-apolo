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
        'NAME': 'd32l4k43t7i16f',
        'USER': 'vrkgkreqnqsypj',
        'PASSWORD': '15694e42e5f7a5d0851d8d09b40aab32ec71ffec5168c2fc3f443f3c704a3de2',
        'HOST': 'ec2-52-1-17-228.compute-1.amazonaws.com',
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
