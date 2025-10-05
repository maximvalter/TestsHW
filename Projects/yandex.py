import requests
import pytest

TOKEN = "y0__xC-jvjgAxih2jog0771zRQwl5ywhQggc3OId8wEqcrH0HFqCE47JlvVNQ"
API_URL = "https://cloud-api.yandex.net/v1/disk/resources"

headers = {
    "Authorization": f"OAuth {TOKEN}"
}

def create_folder(folder_name):
    return requests.put(API_URL, headers=headers, params={"path": folder_name})

def get_metadata(path):
    return requests.get(API_URL, headers=headers, params={"path": path})



