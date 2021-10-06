from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):

    __tablename__ = "users"


    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    account_balance = Column(Float)

    in_transactions = relationship("Transaction", back_populates="user_from")
    out_transactions = relationship("Transaction", back_populates="user_to")



class Transaction(Base):

    __tablename__ = "transactions"


    id = Column(Integer, primary_key=True, index=True)
    value = Column(Float)
    description = Column(String, index=True)
    user_from_id = Column(Integer, ForeignKey("users.id"))
    user_to_id = Column(Integer)

    user_from = relationship("User", back_populates="in_transactions")
    user_to = relationship("User", back_populates="out_transactions")
