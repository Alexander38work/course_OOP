class Vacancies:
    """����� ��� ������ � ����������"""
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
            self.salary_to = '���������� �� �������'


    def __repr__(self):
        return (f'�������� ��������: {self.name}\n'
                f'��������: {self.salary} {self.currency}\n'
                f'����������: {self.requirement}\n'
                f'������ �� ��������: <{self.url}>\n')


