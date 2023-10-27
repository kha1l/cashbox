import asyncio
from configurations.conf import Config
from functions.worker import work


Config.scheduler.add_job(work, 'cron', hour=13, minute=42)

async def main():
    cfg = Config()
    cfg.scheduler.start()
    while True:
        await asyncio.sleep(1)


if __name__ == '__main__':
    asyncio.run(main())
