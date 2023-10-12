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
            'Таганрог-1': ['2023947174', 'CD-17/107674', '445fbcca-2d0b-4455-a0ea-fe2482081da9'],
            'Таганрог-2': ['1559931033', 'CD-17/107674', '54b671d5-bd15-4f1a-88e1-92a7d468567b'],
            'Ростов-на-Дону-1': ['1966469589', 'CD-17/97714', 'db8764a1-7204-411a-9049-0e5d5978aebf'],
            'Ростов-на-Дону-2': ['55310690', 'CD-17/97714', 'f0d2b29a-8e55-4d9d-9269-2ae159a59486'],
            'Ростов-на-Дону-3': ['1436295338', 'CD-17/64113', 'b2d64b63-3033-4648-9e23-e666a6f6c99c'],
            'Ростов-на-Дону-4': ['321867200', 'CD-19/224098', 'd0ffb8dc-b9a4-4789-a9d2-6168849d2b84'],
            'Ростов-на-Дону-5': ['105376487', 'CD-17/64113', '41d8b527-f0e9-4811-b024-3d59738bc063'],
            'Ростов-на-Дону-6': ['1397094942', 'CD-20/268733', '1ef27212-2554-4b50-b21e-78520d3e401a'],
            'Ростов-на-Дону-7': ['2094433420', 'CD-17/97714', '835a1a00-7b71-44d4-9a06-ad9a9d018e89'],
            'Сочи-1': ['1071695380', 'CD-21/315949', '0c107efb-8e04-4e42-9950-e1fe468ce81a'],
            'Сочи-2': ['1169862323', 'CD-19/224098', 'ed9d7bc7-5ddd-4658-a92c-e0592ea7bf50'],
            'Сочи-3': ['1761251058', 'CD-22/363578', 'e82d9e36-d8b9-46be-ab35-dc82a9839c35'],
            'Воронеж-1': ['1138327160', 'CD-21/332201', '46d79d45-e327-498e-b919-0010b0f5e3f8'],
            'Воронеж-2': ['494599500', 'CD-21/332206', '90984b98-82e0-48ed-9b3c-3595a168707a'],
            'Воронеж-3': ['1983398205', 'CD-20/268733', 'f4336ad3-310a-4f44-8b1d-4dc5aa835924'],
            'Воронеж-4': ['1726553549', 'CD-22/363578', '1f610384-c056-49d3-863a-3ef8369987ac'],
            'Воронеж-5': ['2066066102', 'CD-22/363578', '63889ec2-67ba-41de-b5e2-dcfb08ad54d0'],
            'Воронеж-6': ['893445096', 'CD-22/363578', 'e8bed08b-ee4b-4fc9-80f0-5dd93372efd0']
        }
