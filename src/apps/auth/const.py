import enum


class FieldsBusyExceptionMessages(enum.Enum):
    USER_USERNAME: str = "Данное имя пользователя занято"
    USER_PHONE_NUMBER: str = "Данный номер телефона занят"
    USER_EMAIL: str = "Данный email занят"
