import pytest

from api.account_management.account_management import AccountManagement


@pytest.fixture
def account_management():
    return AccountManagement()


def test_login_success(account_management, mocker):
    # Arrange
    mocker.patch('api.requests.accounts.read_by_email',
                 return_value={'id': 1, 'password': 'password', 'name': 'Test User'})

    # Mock user inputs
    mocker.patch('builtins.input', side_effect=['user@example.com', 'password'])

    # Act
    account_id = account_management.login()

    # Assert
    assert account_id == 1


def test_login_failure(account_management, mocker):
    # Arrange
    mocker.patch('api.requests.accounts.read_by_email', return_value=None)

    # Mock user inputs
    mocker.patch('builtins.input', side_effect=['user@example.com', 'password'])

    # Act
    account_id = account_management.login()

    # Assert
    assert account_id is None


def test_register_account(account_management, mocker):
    # Arrange
    mocker.patch('api.controllers.roles.read_all',
                 return_value=[{'id': 1, 'name': 'Admin', 'description': 'Administrator'}])
    mocker.patch('api.requests.accounts.create', return_value={'id': 1, 'name': 'Test User'})
    mocker.patch('api.requests.payment_information.create', return_value={'id': 1})

    # Mock user inputs
    mocker.patch('builtins.input', side_effect=[
        'Test User', '30', '1234567890', 'test@example.com', 'password', '1', 'n'
    ])

    # Act
    account_id = account_management.register_account()

    # Assert
    assert account_id == 1


def test_create_payment_information(account_management, mocker):
    # Arrange
    mocker.patch('api.requests.payment_information.create', return_value={'id': 1, 'balance_on_account': 100})

    # Act
    response = account_management.create_payment_information(100, '1234-5678-9876-5432', 'Credit Card')

    # Assert
    assert response is not None
    assert response['id'] == 1


def test_update_payment_information(account_management, mocker):
    # Arrange
    mocker.patch('api.requests.payment_information.update', return_value={'id': 1, 'balance_on_account': 150})

    # Act
    response = account_management.update_payment_information(1, 150, '1234-5678-9876-5432', 'Credit Card')

    # Assert
    assert response is not None
    assert response['balance_on_account'] == 150
