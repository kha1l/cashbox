from dotenv import load_dotenv
import os
from apscheduler.schedulers.asyncio import AsyncIOScheduler


class Config:
    scheduler = AsyncIOScheduler({'apscheduler.timezone': 'Europe/Moscow'})

    def __init__(self,):
        load_dotenv()
        self.dbase = os.getenv('DBASE')
        self.host = os.getenv('HOST')
        self.password = os.getenv('PASSWORD')
        self.user = os.getenv('USER')
        self.id = os.getenv('ID')
        self.login = os.getenv('LOGIN')
        self.password_tax = os.getenv('PASSWORD_TAX')
        self.stationary = {
            'Таганрог-1': ['2023947174'],
            'Таганрог-2': ['1559931033'],
            'Ростов-на-Дону-1': ['1966469589'],
            'Ростов-на-Дону-2': ['55310690'],
            'Ростов-на-Дону-3': ['1436295338'],
            'Ростов-на-Дону-4': ['321867200'],
            'Ростов-на-Дону-5': ['105376487'],
            'Ростов-на-Дону-6': ['1397094942'],
            'Ростов-на-Дону-7': ['2094433420'],
            'Сочи-1': ['1071695380'],
            'Сочи-2': ['1169862323'],
            'Сочи-3': ['1761251058'],
            'Воронеж-1': ['1138327160'],
            'Воронеж-2': ['494599500'],
            'Воронеж-3': ['1983398205'],
            'Воронеж-4': ['1726553549'],
            'Воронеж-5': ['2066066102'],
            'Воронеж-6': ['893445096']
        }
