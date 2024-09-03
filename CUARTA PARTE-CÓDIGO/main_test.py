import os
import re
import pytest
import webtest


@pytest.fixture
def main(monkeypatch):
    monkeypatch.setenv("CLOUDSQL_USER", "root")
    monkeypatch.setenv("CLOUDSQL_PASSWORD", "")
    import main

    return main


@pytest.mark.skipif(
    not os.path.exists("/var/run/mysqld/mysqld.sock"),
    reason="Local MySQL server not available.",
)
def test_app(main):
    app = webtest.TestApp(main.app)
    response = app.get("/")

    assert response.status_int == 200
    assert re.search(re.compile(r".*version.*", re.DOTALL), response.body)