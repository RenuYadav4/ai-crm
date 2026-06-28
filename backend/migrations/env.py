<<<<<<< HEAD
import os
import sys
from pathlib import Path
from logging.config import fileConfig
from sqlalchemy import create_engine
from core.config import settings
from sqlalchemy import pool

from alembic import context
=======
import sys
from logging.config import fileConfig
from pathlib import Path

from alembic import context
from sqlalchemy import create_engine, pool

project_root = Path(__file__).resolve().parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))
>>>>>>> 10b1d0a (fixed migration issue)

# ✅ Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Import Base after path is set
from core.database import Base
import models  # noqa: F401

# this is the Alembic Config object
config = context.config

# Interpret the config file for Python logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

<<<<<<< HEAD
# add your model's MetaData object here
=======
config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)

print("ALEMBIC TABLES:", Base.metadata.tables.keys())

>>>>>>> 10b1d0a (fixed migration issue)
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


<<<<<<< HEAD
def run_migrations_online():
=======
def run_migrations_online() -> None:
>>>>>>> 10b1d0a (fixed migration issue)
    connectable = create_engine(
        settings.DATABASE_URL,
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()