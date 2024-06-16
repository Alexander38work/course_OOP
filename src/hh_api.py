# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
import requests


class FromAPI(ABC):

    """Абстрактный класс"""

    @abstractmethod
    def get_vacancies(self, *args, **kwargs):
        pass


class HHAPI(FromAPI):

    """Класс для работы с api HH.ru и получения вакансий"""

    def __init__(self):
        self.base_url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []

    def get_vacancies(self, keyword):

        """Получение вакансий по ключевому слову в формате json"""
        self.params.update(({'text': keyword}))
        response = requests.get(self.base_url, params=self.params)
        return response.json()['items']


