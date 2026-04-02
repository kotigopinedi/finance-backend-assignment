from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from fastapi.security import OAuth2PasswordRequestForm
import models, schemas, crud, auth, database

# Initialize Database
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Finance Dashboard API")

@app.post("/register", response_model=schemas.UserOut)
def register(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    if crud.get_user_by_email(db, email=user.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = crud.get_user_by_email(db, email=form_data.username)
    if not user or not auth.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    access_token = auth.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/records", response_model=List[schemas.RecordOut])
def read_records(db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    return crud.get_records(db)

@app.post("/records", response_model=schemas.RecordOut)
def create_new_record(
    record: schemas.RecordCreate, 
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(auth.check_role(["Admin"]))
):
    return crud.create_record(db=db, record=record, user_id=current_user.id)

@app.get("/dashboard/summary", response_model=schemas.DashboardSummary)
def get_summary(
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(auth.check_role(["Admin", "Analyst"]))
):
    return crud.get_dashboard_summary(db)

@app.get("/")
def home():
    return {"message": "Finance API is Live!", "docs": "/docs"}