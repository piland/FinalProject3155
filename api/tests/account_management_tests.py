import pytest
import requests_mock
from pytest_mock import mocker
from api.account_management.account_management import AccountManagement
from api.requests import accounts, payment_information
from api.controllers import roles
from api.dependencies.database import SessionLocal
import api.schemas
from api.account_management import account_management


@pytest.fixture
def account_management():
    return AccountManagement()


def test_login_menu(account_management, mocker):
    mocker.patch('builtins.input', side_effect=['1', 'user@example.com', 'password'])
    mocker.patch.object(account_management, 'login', return_value=None)
    mocker.patch.object(account_management, 'register_account', return_value=None)
    mocker.patch.object(account_management, 'guest_login', return_value=None)

    account_management.login_menu()
    assert account_management.login.call_count == 1


# def test_login(account_management, requests_mock):
#     requests_mock.get('http://127.0.0.1:8000/accounts/email/user@example.com',
#                       json={'id': 1, 'password': 'password', 'name': 'Test User'})
#     account_management.login()
#
#     mocker.patch('builtins.input', side_effect=['user@example.com', 'password'])
#
#     assert requests_mock.called_once


# def test_register_account(account_management, requests_mock, mocker):
#     roles_data = [{'id': 1, 'name': 'Admin', 'description': 'Administrator'}]
#     requests_mock.get('http://127.0.0.1:8000/roles', json=roles_data)
#     requests_mock.post('http://127.0.0.1:8000/accounts/', json={'id': 1, 'name': 'Test User'})
#
#     mocker.patch('builtins.input', side_effect=[
#         'Test User', '30', '1234567890', 'test@example.com', 'password', '1', 'n'
#     ])
#     account_management.register_account()
#     assert requests_mock.called


# def test_create_payment_information(account_management, requests_mock):
#     requests_mock.post('http://127.0.0.1:8000/payment_information/',
#                        json={'id': 1, 'balance_on_account': 100, 'card_information': '1234-5678-9876-5432',
#                              'payment_type': 'Credit Card'})
#
#     response = account_management.create_payment_information(100, '1234-5678-9876-5432', 'Credit Card')
#
#     assert response is not None
#     assert response['id'] == 1


# def test_update_payment_information(account_management, requests_mock):
#     requests_mock.put('http://127.0.0.1:8000/payment_information/1',
#                       json={'id': 1, 'balance_on_account': 150, 'card_information': '1234-5678-9876-5432',
#                             'payment_type': 'Credit Card'})
#
#     response = account_management.update_payment_information(1, 150, '1234-5678-9876-5432', 'Credit Card')
#
#     assert response is not None
#     assert response['balance_on_account'] == 150
