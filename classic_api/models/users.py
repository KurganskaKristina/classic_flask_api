from dataclasses import dataclass
from typing import Optional, List

from peewee import AutoField, TextField, IntegrityError, DataError, BinaryUUIDField

from classic_api.models.base import BaseModel, db


@dataclass(frozen=True)
class UserData:
    id: int
    username: str
    firstname: str
    lastname: str
    birthdate: str
    description: str
    profile_photo: bytearray


class UsersModel(BaseModel):
    class Meta:
        table_name = "users"

    id = AutoField()
    username = TextField()
    firstname = TextField()
    lastname = TextField()
    birthdate = TextField()
    description = TextField()
    profile_photo = BinaryUUIDField()

    @classmethod
    def get_length(cls) -> int:
        return cls.select().count()

    @classmethod
    def get_user(cls, user_id: int) -> Optional[UserData]:
        data = cls.select().where(cls.id == user_id).first()

        if data:
            result_data = UserData(
                id=data.id,
                username=data.username,
                firstname=data.firstname,
                lastname=data.lastname,
                birthdate=data.birthdate,
                description=data.description,
                profile_photo=data.profile_photo
            )

            return result_data

    @classmethod
    def get_users_page(cls, page_num=1, page_size=20) -> List[UserData]:
        if page_num <= 0:
            page_num = 1

        offset = (page_size * page_num) - page_size

        data = UsersModel.select().limit(page_size).offset(offset)

        res_data = []
        for el in data:
            res_data.append(UserData(
                id=el.id,
                username=el.username,
                firstname=el.firstname,
                lastname=el.lastname,
                birthdate=el.birthdate,
                description=el.description,
                profile_photo=el.profile_photo
            ))

        return res_data

    @classmethod
    @db.atomic()
    def add_user(cls, username: str, firstname: str, lastname: str, birthdate: str, description: str,
                 profile_photo: bytearray) -> Optional[int]:
        try:
            lastrowid = cls.insert(
                username=username,
                firstname=firstname,
                lastname=lastname,
                birthdate=birthdate,
                description=description,
                profile_photo=profile_photo,
            ).execute()
            return lastrowid
        except DataError:
            pass
        except IntegrityError:
            pass

    @classmethod
    @db.atomic()
    def remove_user(cls, user_id: int) -> bool:
        data = cls.select().where(cls.id == user_id).first()

        if data is None:
            return False

        cls.get(cls.id == user_id).delete_instance()

        return True

    @classmethod
    def modify(cls, user_id: int, username: str, firstname: str, lastname: str, birthdate: str, description: str,
               profile_photo: bytearray) -> bool:
        data = cls.select().where(cls.id == user_id).first()

        if data is None:
            return False

        data.username = username,
        data.firstname = firstname,
        data.lastname = lastname,
        data.birthdate = birthdate,
        data.description = description,
        data.profile_photo = profile_photo,
        data.save()

        return True
