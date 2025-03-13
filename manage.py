"""This file sets up a command line manager.
Use "python manage.py" for a list of available commands.
Use "python manage.py runserver" to start the development web server on localhost:5000.
Use "python manage.py runserver --help" for a list of runserver options.
"""

from flask_migrate import Migrate

from app import create_app
from app.commands import InitDbCommand, CreateDbCommand, MigrateDbCommand

app = create_app()
migrate = Migrate(app)

# Register custom commands
@app.cli.command("init_db")
def init_db_command():
    """Initialize the database."""
    InitDbCommand()
    print('[INFO] Database has been initialized.')

@app.cli.command("create_db")
def create_db_command():
    """Create the database."""
    CreateDbCommand()
    print('[INFO] Database has been created.')

@app.cli.command("migrate_db")
def migrate_db_command():
    """Migrate the database."""
    MigrateDbCommand()
    print('[INFO] Database has been migrated.')


cli = app.cli

if __name__ == "__main__":
    cli()
