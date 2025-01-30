import pytest
from utilities.driver_factory import get_driver

@pytest.fixture(scope="class")
def init_driver(request):
    driver=get_driver()
    request.cls.driver=driver
    yield
    driver.quit()
    