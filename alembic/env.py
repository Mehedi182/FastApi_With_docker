from logging.config import fileConfig
import os
from sqlalchemy import engine_from_config, create_engine
from sqlalchemy import pool
from pydantic import BaseSettings
from alembic import context
from app.db.base_class import Base
from app.address.models import Districts


# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

config.set_main_option(
    "sqlalchemy.url",
    f'postgresql+psycopg2://postgres:1234@127.0.0.1:5432/test_db')
if os.getenv('TESTING'):
    config.set_main_option(
        "sqlalchemy.url",
        f'postgresql+psycopg2://postgres:1234@127.0.0.1:5432/test_db_test')

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = Base.metadata


# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    # url = config.get_main_option("sqlalchemy.url")
    url = get_url()
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """

    # handle testing config for migrations
    db_url = f'postgresql+psycopg2://postgres:1234@127.0.0.1:5432/test_db'
    if os.getenv('TESTING'):
        db_url = f'postgresql+psycopg2://postgres:1234@127.0.0.1:5432/test_db_test'
    if os.environ.get("TESTING"):
        # connect to primary db
        default_engine = create_engine(db_url, isolation_level="AUTOCOMMIT")
        # drop testing db if it exists and create a fresh one
        with default_engine.connect() as default_conn:
            default_conn.execute(
                f"select pg_terminate_backend(pid) from pg_stat_activity where datname='test_db_test'")
            default_conn.execute(f"DROP DATABASE IF EXISTS test_db_test")
            default_conn.execute(f"CREATE DATABASE test_db_test")
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata, compare_type=True
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
