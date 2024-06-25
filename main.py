# -*- coding: utf-8 -*-
from src.hh_api import HHAPI


if __name__ == "__main__":
#    user_interation()

    apireq = HHAPI()
    print(apireq.get_vacancies("слесарь"))