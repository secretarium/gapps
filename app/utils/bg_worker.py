from config import config
from typing import Type
import procrastinate
import os
from procrastinate.contrib.aiopg import AiopgConnector

app = config.get(os.getenv('FLASK_CONFIG') or 'default')

connector_class: Type[procrastinate.BaseConnector]
connector_class = AiopgConnector

bg_app = procrastinate.App(
    connector=connector_class(
        host=app.POSTGRES_HOST,
        user=app.POSTGRES_USER,
        password=app.POSTGRES_PASSWORD
    ),
    import_paths=app.INTEGRATION_IMPORT_PATHS)
