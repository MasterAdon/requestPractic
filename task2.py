import requests
from pprint import pprint

class YaUploader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def upload(self, token):
        """Метод загруджает файлы по списку file_list на яндекс диск"""

        url = "https://cloud-api.yandex.net:443/v1/disk/resources/upload"
        get_headers = {'Content-Type ': 'application/json',
                       'Authorization': 'OAuth {}'.format(token)}
        params = {'path': self.file_path, 'overwrite': 'true'}
        respose = requests.get(url, headers=get_headers, params=params)
        a = respose.json()  # Получаем ссылку на закрузку от Яндекса, согласно инструкции
        href = a.get('href', '')  # Ссылка на загрузку лежит тут
        response = requests.put(href, data=open(self.file_path, 'rb'))
        if response.status_code == 201:
            print("Загрузка выполнена")






if __name__ == '__main__':
    uploader = YaUploader('')
    result = uploader.upload('') # Вставить OAuth токен
