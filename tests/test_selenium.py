from selenium_yandex import try_login

def test_invalid_login():
    error = try_login("fake_user", "fake_password").lower()
    possible_errors = [
        "нет такого аккаунта",
        "такой логин не подойдет"
    ]
    assert any(msg in error for msg in possible_errors)
