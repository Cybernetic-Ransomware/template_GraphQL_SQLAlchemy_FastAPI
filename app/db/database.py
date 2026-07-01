from sqlalchemy import create_engine
from sqlalchemy.engine import make_url
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.core.config import settings


def build_connect_args() -> dict:
    """Build driver-specific connect_args for the configured DATABASE_URL.

    Supported drivernames (see .env.template for the matching modes):
    - "sqlite"          -> stdlib sqlite3 (plain SQLite)
    - "sqlite+libsql"   -> sqlalchemy-libsql (local / Turso remote / embedded replica)
    - "sqlite+turso"    -> pyturso (bonus, experimental native Turso engine)
    """
    engine_instance = make_url(settings.database_url)

    match engine_instance.drivername:
        case "sqlite":
            return {"check_same_thread": False}
        case "sqlite+libsql":
            is_remote = bool(engine_instance.host) or bool(settings.turso_sync_url)
            if is_remote and not settings.turso_auth_token:
                raise ValueError("TURSO_AUTH_TOKEN is required for Turso remote/embedded-replica mode")

            args: dict = {}
            if settings.turso_auth_token:
                args["auth_token"] = settings.turso_auth_token
            if settings.turso_sync_url:
                args["sync_url"] = settings.turso_sync_url
            return args
        case "sqlite+turso":
            return {}
        case _:
            raise NotImplementedError()


connect_args = build_connect_args()
engine = create_engine(settings.database_url, connect_args=connect_args)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
