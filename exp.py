import asyncio

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
import settings
from db.dals import UserDAL

engine = create_async_engine(settings.REAL_DATABASE_URL, future=True, echo=True)


async def attempt():
    async with AsyncSession(engine) as session:
        user_dal = UserDAL(session)
        return await user_dal.create_user("Fedor", "Lapshin", "example@mail.com")


async def main():
    result = await attempt()
    print(result)


# Запустите асинхронный код внутри цикла событий
if __name__ == "__main__":
    asyncio.run(main())
