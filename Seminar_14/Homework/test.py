import pytest
from aytorize import Loger
import create_db
import os


@pytest.fixture()
def data():
    path = 'my_user.json'
    user_db = create_db.load_json(path)
    new_user = create_db.User("Сергей", 1, 2)
    user_db = create_db.add_user(user_db, new_user)
    create_db.save_json(path, user_db)
    return path

def test1(data):
    assert Loger(data).authorize(1, 'Сергей') == 2

def test2(data):
    with pytest.raises(Exception, match='Пользователь с такими данными не найден'):
        Loger(data).authorize(5, 'Николай')

def test3(data):
    with pytest.raises(Exception, match='Пользователь с такими данными не найден'):
        Loger(data).authorize(1, 'Иван')

def test4(data):
    with pytest.raises(ValueError, match='Имя должно быть текстового вида'):
        user_db = create_db.load_json(data)
        new_user = create_db.User("С446ергей", 0.5, 2)

def test5(data):
    with pytest.raises(ValueError, match='Личный идентификатор должен быть целым числом'):
        user_db = create_db.load_json(data)
        new_user = create_db.User("Николай", 0.5, 3)

def test6(data):
    with pytest.raises(ValueError, match='Уровень доступа должен быть числом от 1 до 7'):
        user_db = create_db.load_json(data)
        new_user = create_db.User("Николай", 2, 10)


if __name__ == '__main__':
    pytest.main(['-v'])