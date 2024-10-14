from dataclasses import dataclass


@dataclass
class UserRegisterParams:
    email: str = None
    password: str = None
    phone_number: str = None
    first_name: str = None
    last_name: str = None
    birth_date: str = None
    is_active: bool = True
    is_superuser: bool = False
    is_staff: bool = False


@dataclass
class UserUpdateParams:
    email: str = None
    password: str = None
    phone_number: str = None
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


@dataclass
class PhoneNumberRegistrationParams:
    phone_number: str


@dataclass
class EmailRegistrationParams:
    email: str


@dataclass
class CredentialsVerificationParams:
    otp: str
    target_value: str


@dataclass
class OAuth2Params:
    token: str
