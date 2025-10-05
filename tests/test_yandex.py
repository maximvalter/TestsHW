from yandex import *

# Положительный сценарий
def test_create_folder_success():
    folder_name = "test_folder"
    response = create_folder(folder_name)
    assert response.status_code in (200, 201, 409)
    # 200/201 — папка создана, 409 — уже есть

    # Проверяем метаданные созданной папки
    meta = get_metadata(folder_name)
    assert meta.status_code == 200
    assert meta.json()["type"] == "dir"


# Отрицательные сценарии
def test_create_folder_invalid_token():
    # Неверный токен - 401 Unauthorized
    bad_headers = {"Authorization": "OAuth invalid_token"}
    response = requests.put(API_URL, headers=bad_headers, params={"path": "bad_folder"})
    assert response.status_code == 401


def test_create_folder_invalid_name():
    # Кривое имя - 400 Bad request или 409 Conflict
    response = create_folder("bad/folder?name")
    assert response.status_code in (400, 409)


def test_create_folder_empty_name():
    # Пустое имя - 400 Bad request
    response = create_folder("")
    assert response.status_code == 400
