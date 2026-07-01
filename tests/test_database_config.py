import pytest

from app.db.database import build_connect_args


def test_plain_sqlite():
    assert build_connect_args("sqlite:///./test.db") == {"check_same_thread": False}


def test_local_libsql_needs_no_credentials():
    assert build_connect_args("sqlite+libsql:///local.db") == {}


def test_libsql_remote_with_token():
    args = build_connect_args("sqlite+libsql://mydb.turso.io?secure=true", auth_token="tok")

    assert args == {"auth_token": "tok"}


def test_libsql_remote_without_token_raises():
    with pytest.raises(ValueError, match="TURSO_AUTH_TOKEN"):
        build_connect_args("sqlite+libsql://mydb.turso.io?secure=true")


def test_libsql_embedded_replica():
    args = build_connect_args(
        "sqlite+libsql:///embedded.db",
        auth_token="tok",
        sync_url="libsql://mydb.turso.io",
    )

    assert args == {"auth_token": "tok", "sync_url": "libsql://mydb.turso.io"}


def test_libsql_embedded_replica_without_token_raises():
    with pytest.raises(ValueError, match="TURSO_AUTH_TOKEN"):
        build_connect_args("sqlite+libsql:///embedded.db", sync_url="libsql://mydb.turso.io")


def test_native_turso_needs_no_credentials():
    assert build_connect_args("sqlite+turso:///local_native.db") == {}


def test_unsupported_driver_raises_with_message():
    with pytest.raises(NotImplementedError, match="postgresql"):
        build_connect_args("postgresql://user:pass@localhost/db")
