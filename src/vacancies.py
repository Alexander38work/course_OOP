class Vacancies:
    """Класс для работы с вакансиями"""
    def __init__(self, name, salary, currency,period, url, area):
        self.name = name
        self.salary = salary
        self.currency = currency
        self.period = period
        self.url = url
        self.area = area

        self.validate()

    def validate(self):
        if self.salary == None:
            self.salary = 0
        if self.salary_to == None:
            self.salary_to = 'информация не указана'


    def __repr__(self):
        return (f'Название вакансии: {self.name}\n'
                f'Зарплата: {self.salary} {self.currency}\n'
                f'Требования: {self.requirement}\n'
                f'Ссылка на вакансию: <{self.url}>\n')


