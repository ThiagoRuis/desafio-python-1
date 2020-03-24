import pytest
from server.instance import server

@pytest.fixture
def app():
    app = server.app
    app.config["PROPAGATE_EXCEPTIONS"] = False
    return app