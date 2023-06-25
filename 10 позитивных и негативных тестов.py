import requests

base_url = 'https://petfriends.skillfactory.ru/api/'

# Тест 1: Получение списка пользователей
def test_get_user_list():
    response = requests.get(base_url + 'users')
    assert response.status_code == 200
    assert len(response.json()) > 0

# Тест 2: Получение информации о конкретном пользователе
def test_get_user_info():
    user_id = 1  # Идентификатор пользователя для теста
    response = requests.get(base_url + f'users/{user_id}')
    assert response.status_code == 200
    assert response.json()['id'] == user_id

# Тест 3: Создание нового пользователя
def test_create_user():
    data = {
        'email': 'test@example.com',
        'password': 'password123'
    }
    response = requests.post(base_url + 'users', json=data)
    assert response.status_code == 201
    assert 'id' in response.json()

# Тест 4: Обновление информации о пользователе
def test_update_user():
    user_id = 1
    data = {
        'email': 'new_email@example.com',
        'password': 'newpassword123'
    }
    response = requests.put(base_url + f'users/{user_id}', json=data)
    assert response.status_code == 200
    assert response.json()['email'] == data['email']

# Тест 5: Удаление пользователя
def test_delete_user():
    user_id = 1 
    response = requests.delete(base_url + f'users/{user_id}')
    assert response.status_code == 204

# Тест 6: Получение списка питомцев
def test_get_pet_list():
    response = requests.get(base_url + 'pets')
    assert response.status_code == 200
    assert len(response.json()) > 0

# Тест 7: Получение информации о конкретном питомце
def test_get_pet_info():
    pet_id = 1
    response = requests.get(base_url + f'pets/{pet_id}')
    assert response.status_code == 200
    assert response.json()['id'] == pet_id

# Тест 8: Создание нового питомца
def test_create_pet():
    data = {
        'name': 'Major',
        'animal_type': 'cat',
        'age': 7
    }
    response = requests.post(base_url + 'pets', json=data)
    assert response.status_code == 201
    assert 'id' in response.json()

# Тест 9: Обновление информации о питомце
def test_update_pet():
    pet_id = 1
    data = {
        'name': 'Max',
        'animal_type': 'dog',
        'age': 5
    }
    response = requests.put(base_url + f'pets/{pet_id}', json=data)
    assert response.status_code == 200
    assert response.json()['name'] == data['name']

# Тест 10: Удаление питомца
def test_delete_pet():
    pet_id = 1
    response = requests.delete(base_url + f'pets/{pet_id}')
    assert response.status_code == 204

def run_tests():
    test_get_user_list()
    test_get_user_info()
    test_create_user()
    test_update_user()
    test_delete_user()
    test_get_pet_list()
    test_get_pet_info()
    test_create_pet()
    test_update_pet()
    test_delete_pet()

run_tests()
