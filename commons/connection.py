from orator import DatabaseManager, Model


config = {
    'default': 'postgres',
    'postgres': {
        'driver': 'postgres',
        'host': 'isilo.db.elephantsql.com',
        'port': 5432,
        'database': 'ojipbcuc',
        'user': 'ojipbcuc',
        'password': 'nTG4JLTPxbOJDwn-l2o7yMEDFG9pX-XQ',
        'prefix': ''
    },
    'mysql': {
        'driver': 'mysql',
        'host': '',
        'database': '',
        'user': '',
        'password': '',
        'prefix': ''
    }
}
db = DatabaseManager(config)
Model.set_connection_resolver(db)
