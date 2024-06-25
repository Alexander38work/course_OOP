from abc import ABC, abstractmethod
import json


class Fileworker(ABC):

    """����������� �����"""

    @abstractmethod
    def add_vacancy(self, *args):
        pass

    @abstractmethod
    def get_data(self, *args):
        pass

    @abstractmethod
    def delete_vacancy(self):
        pass

class ListVacancies(Fileworker):

    @staticmethod
    def save_vacancies(vacancies):

        """������ ������ �������� � ����"""

        with open("../data/vacancies.json", "w", encoding="utf8") as f:
            vacancies_json = json.dumps(vacancies, ensure_ascii=False)
            f.write(vacancies_json)

    def add_vacancy(self, name_vac):

        """����� ��� ���������� �������� � ����"""

        with open("../data/vacancies.json", "r", encoding="utf8") as f:
            list_vacancies = json.load(f)
        with open("../data/my_vacancies.json", "r", encoding="utf8") as f:
            list = json.load(f)
        for v in list_vacancies:
            if name_vac in v["name"]:
                list.append(v)
        list_vacancies_add = json.dumps(list, indent=4, ensure_ascii=False)

        with open("../data/my_vacancies.json", "w", encoding="utf8") as f:
            f.write(list_vacancies_add)
        return list_vacancies_add

    def get_data(self, criterion):

        """����� ��������� ������ �� ����� �� ��������� ���������"""

        with open("../data/vacancies.json", "r", encoding="utf8") as f:
            vacancies = json.load(f)
            criterion_vac = []
            for vac in vacancies:
                if not vac["snippet"]["requirement"]:
                    continue
                else:
                    if criterion in vac["snippet"]["requirement"]:
                        criterion_vac.append(vac)
        return criterion_vac

    def delete_vacancy(self):

        """����� �������� ������ �� �����"""

        list_vacancies_del = []
        list = json.dumps(list_vacancies_del, ensure_ascii=False)
        with open("../data/my_vacancies.json", "w", encoding="utf8") as f:
            f.write(list)
