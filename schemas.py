from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime
from models import UserRole, RecordType

class UserBase(BaseModel):
    email: EmailStr
    role: UserRole = UserRole.VIEWER

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int
    is_active: int
    class Config:
        from_attributes = True

class RecordBase(BaseModel):
    amount: float
    type: RecordType
    category: str
    description: Optional[str] = None

class RecordCreate(RecordBase):
    pass

class RecordOut(RecordBase):
    id: int
    date: datetime
    owner_id: int
    class Config:
        from_attributes = True

class DashboardSummary(BaseModel):
    total_income: float
    total_expense: float
    net_balance: float
    category_totals: dict