import pytest
from unittest.mock import MagicMock
from src.controllers.CategoryController import CategoryController


def test_verify_category_success(mocker):
    mock_category_model = mocker.patch('src.controllers.CategoryController.CategoryModel')
    mock_category_model_instance = mock_category_model.return_value
    mock_category_model_instance.verify_category.return_value = {'category_id': 'Category_id',
                                                                 'category_name': 'Category Test'}

    category_controller = CategoryController()
    category_id = "Category_id"
    category_name = "Category Test"

    response = category_controller.verify_category(category_id, category_name)

    assert response == {
        'status_code': 200,
        'response': 'Verify category',
        'result': {'category_id': 'Category_id', 'category_name': 'Category Test'}
    }
    mock_category_model_instance.verify_category.assert_called_once_with(category_id, category_name)


def test_verify_data_not_found(mocker):
    mock_category_model = mocker.patch('src.controllers.CategoryController.CategoryModel')
    mock_category_model_instance = mock_category_model.return_value
    mock_category_model_instance.verify_category.return_value = None

    category_controller = CategoryController()
    category_id = "Category_id"
    category_name = "Category Test"

    response = category_controller.verify_category(category_id, category_name)

    assert response == {
        'status_code': 404,
        'response': 'Don’t Verify category'
    }


def test_verify_data_exception(mocker):
    mock_category_model = mocker.patch('src.controllers.CategoryController.CategoryModel')
    mock_category_model_instance = mock_category_model.return_value
    mock_category_model_instance.verify_category.side_effect = Exception("Mocked exception")

    category_controller = CategoryController()
    category_id = "Category_id"
    category_name = "Category Test"

    response = category_controller.verify_category(category_id, category_name)

    assert response == {
        'status_code': 500,
        'response': f'Error verifying category: Mocked exception'
    }


def test_create_category_success(mocker):
    mock_category_model = mocker.patch('src.controllers.CategoryController.CategoryModel')
    mock_category_model_instance = mock_category_model.return_value
    mock_category_model_instance.create_category.return_value = None

    category_controller = CategoryController()
    category_id = "Category_id"
    category_name = "Category Test"

    response = category_controller.create_category(category_id, category_name)

    expected_result = {
        'result': f'{'Category_id', 'Category Test'}'
    }
    assert response == expected_result
    mock_category_model_instance.create_category.assert_called_once_with(category_id, category_name)


def test_create_category_failed(mocker):
    mock_category_model = mocker.patch('src.controllers.CategoryController.CategoryModel')
    mock_category_model_instance = mock_category_model.return_value
    mock_category_model_instance.create_category.side_effect = Exception("Mocked exception")

    category_controller = CategoryController()
    category_id = "Category_id"
    category_name = "Category Test"

    response = category_controller.create_category(category_id, category_name)

    assert response == {
        'status_code': 500,
        'response': f'Error when creating the category: Mocked exception'
    }
    mock_category_model_instance.create_category.assert_called_once_with(category_id, category_name)


def test_get_category_by_id_success(mocker):
    mock_category_model = mocker.patch('src.controllers.CategoryController.CategoryModel')
    mock_category_model_instance = mock_category_model.return_value
    mock_category_model_instance.get_category_by_id.return_value = {'category_name': 'Category_name Test'}

    category_controller = CategoryController()
    category_controller.category_model = mock_category_model_instance
    category_id = "Category_id"

    response = category_controller.get_category_by_id(category_id)

    assert response == {
        'status_code': 200,
        'response': 'Category_id found',
        'result': {'category_name': 'Category_name Test'}
    }


def test_get_category_by_id_not_found(mocker):
    mock_category_model = mocker.patch('src.controllers.CategoryController.CategoryModel')
    mock_category_model_instance = mock_category_model.return_value
    mock_category_model_instance.get_category_by_id.return_value = None

    category_controller = CategoryController()
    category_controller.category_model = mock_category_model_instance
    category_id = "Category_id"

    response = category_controller.get_category_by_id(category_id)

    assert response == {
        'status_code': 404,
        'response': 'Category_id not found'
    }


def test_get_category_by_id_exception(mocker):
    mock_category_model = mocker.patch('src.controllers.CategoryController.CategoryModel')
    mock_category_model_instance = mock_category_model.return_value
    mock_category_model_instance.get_category_by_id.side_effect = Exception("Mocked exception")

    category_controller = CategoryController()
    category_controller.category_model = mock_category_model_instance
    category_id = "Category_id"

    response = category_controller.get_category_by_id(category_id)
    assert response == {
        'status_code': 500,
        'response': f'Error finding category_id: Mocked exception'
    }


def test_get_category_by_name_success(mocker):
    mock_category_model = mocker.patch('src.controllers.CategoryController.CategoryModel')
    mock_category_model_instance = mock_category_model.return_value
    mock_category_model_instance.get_category_by_name.return_value = {'category_name': 'Category_name Test'}

    category_controller = CategoryController()
    category_controller.category_model = mock_category_model_instance
    category_name = "Category_name"

    response = category_controller.get_category_by_name(category_name)

    assert response == {
        'status_code': 200,
        'response': 'Category  found',
        'result': {'category_name': 'Category_name Test'}
    }


def test_get_category_by_name_not_found(mocker):
    mock_category_model = mocker.patch('src.controllers.CategoryController.CategoryModel')
    mock_category_model_instance = mock_category_model.return_value
    mock_category_model_instance.get_category_by_name.return_value = None

    category_controller = CategoryController()
    category_controller.category_model = mock_category_model_instance
    category_name = "Category_name"

    response = category_controller.get_category_by_name(category_name)

    assert response == {
        'status_code': 404,
        'response': 'Category not found'
    }


def test_get_category_by_name_exception(mocker):
    mock_category_model = mocker.patch('src.controllers.CategoryController.CategoryModel')
    mock_category_model_instance = mock_category_model.return_value
    mock_category_model_instance.get_category_by_name.side_effect = Exception("Mocked exception")

    category_controller = CategoryController()
    category_controller.category_model = mock_category_model_instance
    category_name = "Category_name"

    response = category_controller.get_category_by_name(category_name)
    assert response == {
        'status_code': 500,
        'response': f'Error finding the category: Mocked exception'
    }


def test_update_category_success(mocker):
    mock_category_model = mocker.patch('src.controllers.CategoryController.CategoryModel')
    mock_category_model_instance = mock_category_model.return_value
    mock_category_model_instance.update_category_id.return_value = {'category_id': 'Category_id',
                                                                    'category_name': 'Category Test'}

    category_controller = CategoryController()
    category_controller.category_model = mock_category_model_instance
    category_id = "Category_id"
    category_name = "Category Test"

    response = category_controller.update_category(category_id, category_name)
    assert response == {
        'status_code': 200,
        'response': 'Update completed successfully',
    }

    mock_category_model_instance.update_category.assert_called_once_with(category_name, category_id)


def test_update_category_failed(mocker):
    mock_category_model = mocker.patch('src.controllers.CategoryController.CategoryModel')
    mock_category_model_instance = mock_category_model.return_value
    mock_category_model_instance.update_category.side_effect = Exception("Mocked exception")

    category_controller = CategoryController()
    category_controller.category_model = mock_category_model_instance
    category_id = "Category_id"
    category_name = "Category Test"

    response = category_controller.update_category(category_id, category_name)
    assert response == {
        'status_code': 500,
        'response': f'Error updating the category: Mocked exception'
    }
    mock_category_model_instance.update_category.assert_called_once_with(category_name, category_id)


def test_delete_category_success(mocker):
    mock_category_model = mocker.patch('src.controllers.CategoryController.CategoryModel')
    mock_category_model_instance = mock_category_model.return_value

    mock_category_model_instance.get_by_category_id.return_value = {
        'status_code': 200,
        'response': 'Category_id found',
        'result': {
            'category_id': 'Category_id',
            'category_name': 'Category_name Test'
        }
    }

    mock_category_model_instance.delete_category.return_value = True

    category_controller = CategoryController()
    category_controller.category_model = mock_category_model_instance

    category_id = "Category_id"
    response = category_controller.delete_category(category_id, confirm=True)

    assert response == {
        'status_code': 200,
        'response': 'The category was deleted'
    }


def test_delete_category_exception(mocker):
    mock_category_model = mocker.patch('src.controllers.CategoryController.CategoryModel')
    mock_category_model_instance = mock_category_model.return_value
    mock_category_model_instance.delete_category.side_effect = Exception("Mocked exception")

    mock_category_model_instance.get_by_category_id.return_value = {
        'status_code': 200,
        'response': 'Category_id found',
        'result': {
            'category_id': 'Category_id',
            'category_name': 'Category_name Test'

        }
    }

    category_controller = CategoryController()
    category_controller.category_model = mock_category_model_instance
    category_id = "Category_id"

    response = category_controller.delete_category(category_id, True)

    assert response == {
        'status_code': 500,
        'response': 'Error deleting category: Mocked exception'
    }
