from sqlalchemy.orm import Session
from Repository import FakeRepository
from Models.User import User  # Импортируем модель User

class UserRepository(FakeRepository.FakeRepository):

    def __init__(self, session: Session = None):
        self.session = session
        self.users = []  # Список для хранения пользователей, если сессия не используется

    def add(self, user: User):
        if self.session:
            self.session.add(user)
            self.session.commit()
        else:
            self.users.append(user)

    def add_multiple(self, users):
        for user in users:
            # Проверяем, существует ли пользователь с таким же id
            if not self.session.query(User).filter(User.id == user.id).first():
                # Если пользователь с таким id не существует, добавляем его
                self.session.add(user)
        # Завершаем транзакцию
        self.session.commit()

    def remove(self, user: User):
        if self.session:
            self.session.delete(user)
            self.session.commit()
        else:
            self.users = [u for u in self.users if u.name != user.name]

    def get_all(self):
        if self.session:
            return self.session.query(User).all()
        return self.users

    def get_by_name(self, name: str):
        if self.session:
            return self.session.query(User).filter(User.name == name).first()
        if self.users:
            for u in self.users:
                if u.name == name:
                    return u
        return None

    def get_by_id(self, id: int):
        if self.session:
            return self.session.query(User).filter(User.id == id).first()
        if self.users:
            for u in self.users:
                if u.id == id:
                    return u
        return None  # Возвращаем None, если пользователь не найден
