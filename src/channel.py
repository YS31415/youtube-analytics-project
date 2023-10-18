import json
import os

# необходимо установить через: pip install google-api-python-client
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.channel_info = self.get_service().channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        self.title = self.channel_info["items"][0]['snippet']['title']
        self.channel_desc = self.channel_info["items"][0]['snippet']["description"]
        self.url = f'https://www.youtube.com/channel/{self.__channel_id}'
        self.subs_coutn = self.channel_info["items"][0]["statistics"]["subscriberCount"]
        self.video_count = self.channel_info["items"][0]["statistics"]['videoCount']
        self.channel_vives = self.channel_info["items"][0]["statistics"]["viewCount"]

    def __str__(self):
        return self.url #(https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A)'

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале.
        Выводит словарь в json-подобном удобном формате с отступами"""

        #channel_id = 'UCwHL6WHUarjGfUM_586me8w'  # HighLoad Channel
        channel = self.get_service().channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))

    @property
    def channel_id(self):
        return self.__channel_id

    @classmethod
    def get_service(cls):
        # создать специальный объект для работы с API
        api_key = os.getenv('YT_API_KEY')
        # YT_API_KEY скопирован из гугла и вставлен в переменные окружения
        return build('youtube', 'v3', developerKey=api_key)

    def to_json(self, file_name):
        # channel_id = 'UCwHL6WHUarjGfUM_586me8w'  # HighLoad Channel
        data = {'channel_id': self.channel_id,
                'channel_title': self.title,
                'channel_desc': self.channel_desc,
                'url': self.url,
                'subs_coutn': self.subs_coutn,
                'video_count': self.video_count,
                'channel_vives': self.channel_vives}
        with open(file_name, 'w', encoding='UTF-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def __add__(self, other):
        return int(self.subs_coutn) + int(other.subs_coutn)

    def __sub__(self, other):
        return int(self.subs_coutn) - int(other.subs_coutn)

    def __gt__(self, other):
        return int(self.subs_coutn) > int(other.subs_coutn)

    def __ge__(self, other):
        return int(self.subs_coutn) >= int(other.subs_coutn)

    def __lt__(self, other):
        return int(self.subs_coutn) < int(other.subs_coutn)

    def __le__(self, other):
        return int(self.subs_coutn) <= int(other.subs_coutn)

    def __eq__(self, other):
        return int(self.subs_coutn) == int(other.subs_coutn)




