from typing import List, Optional

from pydantic import BaseModel


class TransactionBase(BaseModel):
    value: float
    user_from_id: int
    user_to_id: int
    description: Optional[str] = None


class TransactionCreate(TransactionBase):
    pass


class Transaction(TransactionBase):
    id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str
    account_balance: float


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    transaction: List[Transaction] = []

    class Config:
        orm_mode = True
