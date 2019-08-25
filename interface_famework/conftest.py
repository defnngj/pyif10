import pytest


@pytest.fixture
def base_url():
    """定义接口的基础URL"""
    return "http://127.0.0.1:8000/api"
