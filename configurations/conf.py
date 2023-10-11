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
            'Таганрог-1': ['2023947174', '', ''],
            'Таганрог-2': ['1559931033', '', ''],
            'Ростов-на-Дону-1': ['1966469589', 'CD-17/97714', ''],
            'Ростов-на-Дону-2': ['55310690', 'CD-17/97714', ''],
            'Ростов-на-Дону-3': ['1436295338', 'CD-17/64113', ''],
            'Ростов-на-Дону-4': ['321867200', 'CD-19/224098', ''],
            'Ростов-на-Дону-5': ['105376487', 'CD-17/64113', ''],
            'Ростов-на-Дону-6': ['1397094942', 'CD-20/268733', ''],
            'Ростов-на-Дону-7': ['2094433420', 'CD-17/97714', ''],
            'Сочи-1': ['1071695380', 'CD-21/315949', ''],
            'Сочи-2': ['1169862323', 'CD-19/224098', ''],
            'Сочи-3': ['1761251058', 'CD-22/363578', ''],
            'Воронеж-1': ['1138327160', 'CD-21/332201', ''],
            'Воронеж-2': ['494599500', 'CD-21/332206', ''],
            'Воронеж-3': ['1983398205', 'CD-20/268733', ''],
            'Воронеж-4': ['1726553549', 'CD-22/363578', ''],
            'Воронеж-5': ['2066066102', 'CD-22/363578', ''],
            'Воронеж-6': ['893445096', 'CD-22/363578', '']
        }
