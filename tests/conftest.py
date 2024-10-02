"""Configuration for pytest fixtures and options."""

import pytest
from faker import Faker
from calculator import Calculator

fake = Faker()

def pytest_addoption(parser):
    """Add custom command line options for pytest."""
    parser.addoption("--num_records", action="store", default=10,
                     help="Number of records to generate for tests.")

@pytest.fixture
def calculator_instance():
    """Create a Calculator instance for use in tests."""
    return Calculator()

@pytest.fixture
def fake_data(request):
    """Generate fake test data for calculations."""
    num_records = int(request.config.getoption("--num_records"))
    test_data = []
    for _ in range(num_records):
        a = fake.random_int(min=1, max=100)
        b = fake.random_int(min=1, max=100)
        operation = fake.random_element(elements=('add', 'subtract', 'multiply'))
        test_data.append((a, b, operation))
    return test_data
