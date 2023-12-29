import pytest


@pytest.fixture()       # действие выполняемое до теста
def set_up():
    print("Вход в систему выполнен")
    yield
    print("Выход из системы")


@pytest.fixture(scope="function")       # действие выполняемое до теста
def some():
    print("Begin")
    yield
    print("End")