from dataclasses import dataclass


@dataclass
class UserRegister:
    email: str
    password: str
    username: str = ""
    phone_number: str = ""
    first_name: str = ""
    last_name: str = ""
    birth_date: str = None
    is_active: bool = True
    is_superuser: bool = False
    is_staff: bool = False


@dataclass
class UserUpdateParams:
    email: str = None
    password: str = None
    phone_number: str = None
    username: str = None
    first_name: str = None
    last_name: str = None
    is_active: bool = None
    is_superuser: bool = None
    is_staff: bool = None


@dataclass
class UserLoginParams:
    email: str
    password: str


@dataclass
class UserChangePasswordParams:
    old_password: str
    new_password: str
    confirm_password: str
