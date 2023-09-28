import json
import os

# необходимо установить через: pip install google-api-python-client
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        # YT_API_KEY скопирован из гугла и вставлен в переменные окружения
        self.__api_key = os.getenv('YT_API_KEY')
        self.__title = None
        self.url = f'https://www.youtube.com/channel/{self.__channel_id}'

        # создать специальный объект для работы с API
        self.__youtube = build('youtube', 'v3', developerKey=self.__api_key)

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале.
        Выводит словарь в json-подобном удобном формате с отступами"""

        channel_id = 'UC-OVMPlMA3-YCIeg4z5z23A'  # MoscowPython
        #channel_id = 'UCwHL6WHUarjGfUM_586me8w'  # HighLoad Channel
        channel = self.__youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))

    @property
    def channel_id(self):
        return self.__channel_id

    @property
    def title(self):
        return self.__youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()["items"][0]['snippet']['title']

    @property
    def video_count(self):
        channel_id = 'UC-OVMPlMA3-YCIeg4z5z23A'  # MoscowPython
        return self.__youtube.channels().list(id=channel_id, part='snippet,statistics').execute()["items"][0]["statistics"]['videoCount']

    @classmethod
    def get_service(cls):
        return build('youtube', 'v3', developerKey=os.getenv('YT_API_KEY'))

    def to_json(self, path):
        channel_id = 'UC-OVMPlMA3-YCIeg4z5z23A'  # MoscowPython
        # channel_id = 'UCwHL6WHUarjGfUM_586me8w'  # HighLoad Channel
        channel = self.__youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        with open(path, 'w') as f:
            f.write(json.dumps(channel, indent=2, ensure_ascii=False))