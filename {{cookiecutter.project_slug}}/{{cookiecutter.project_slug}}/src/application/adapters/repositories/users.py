import abc
from typing import List

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from application.domain import model


class AbstractUserRepository(abc.ABC):

    @abc.abstractmethod
    def add(self, user: model.User):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, id: int) -> model.User:
        raise NotImplementedError

    @abc.abstractmethod
    def list(self) -> List[model.User]:
        raise NotImplementedError


class FakeUserRepository(AbstractUserRepository):

    def __init__(self):
        self.users = list()    # type: List[model.User]
        self.add(
            model.User(
                id=None,
                username='johndoe',
                full_name='John Doe',
                email='johndoe@example.com',
            )
        )

    def add(self, user: model.User) -> model.User:
        self.users.append(user)
        return user

    def get(self, id: int) -> model.User:
        for i in self.users:
            if i.id == id:
                return i
        return None

    def list(self) -> List[model.User]:
        return self.users


class UserRepository(AbstractUserRepository):

    def __init__(self, session: AsyncSession):
        super().__init__()
        self.session: AsyncSession = session

    async def add(self, user: model.User) -> model.User:
        self.session.add(user)
        await self.session.flush()
        return user

    async def get(self, id: int) -> model.User:
        user = await self.session.execute(
            select(model.User).filter(model.User.id == id)
        )
        return user.scalars().first()

    async def list(self) -> List[model.User]:
        query = select(model.User)
        stmt = await self.session.execute(query)
        users = stmt.scalars().all()
        return users
