import json
import os

# необходимо установить через: pip install google-api-python-client
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        # YT_API_KEY скопирован из гугла и вставлен в переменные окружения
        self.__api_key = os.getenv('YT_API_KEY')

        # создать специальный объект для работы с API
        self.__youtube = build('youtube', 'v3', developerKey=self.__api_key)

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале.
        Выводит словарь в json-подобном удобном формате с отступами"""

        channel_id = 'UC-OVMPlMA3-YCIeg4z5z23A'  # MoscowPython
        #channel_id = 'UCwHL6WHUarjGfUM_586me8w'  # HighLoad Channel
        channel = self.__youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))

