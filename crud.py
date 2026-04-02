from sqlalchemy.orm import Session
from sqlalchemy import func
import models, schemas, auth

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_pw = auth.hash_password(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_pw, role=user.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_record(db: Session, record: schemas.RecordCreate, user_id: int):
    db_record = models.FinancialRecord(**record.model_dump(), owner_id=user_id)
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record

def get_records(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.FinancialRecord).offset(skip).limit(limit).all()

def get_dashboard_summary(db: Session):
    income = db.query(func.sum(models.FinancialRecord.amount)).filter(models.FinancialRecord.type == models.RecordType.INCOME).scalar() or 0.0
    expense = db.query(func.sum(models.FinancialRecord.amount)).filter(models.FinancialRecord.type == models.RecordType.EXPENSE).scalar() or 0.0
    category_data = db.query(models.FinancialRecord.category, func.sum(models.FinancialRecord.amount)).group_by(models.FinancialRecord.category).all()
    
    return {
        "total_income": income,
        "total_expense": expense,
        "net_balance": income - expense,
        "category_totals": {cat: amt for cat, amt in category_data}
    }