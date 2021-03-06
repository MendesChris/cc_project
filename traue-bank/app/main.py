from typing import List

from fastapi import Depends, FastAPI, HTTPException, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.mount("/static", StaticFiles(directory="static/"), name="static")
template = Jinja2Templates(directory='templates/')


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/form')
def read_form(request: Request):
    result = 'type a type'
    return template.TemplateResponse('form.html', context={'request': request, 'result': result})

@app.post('/form')
def post_form(request: Request, num: int = Form(...)):
    result = num*2
    print(num)
    return template.TemplateResponse('form.html', context={'request': request, 'result': result, 'num':num})

@app.post('/')
def post_index(request: Request, cpf: str = Form(...), password: str = Form(...)):
    print(cpf, password)
    test = "abwp[oerjwpkortp[werkt[pwerkt[wepk"
    return template.TemplateResponse('index.html', context={'request': request, 'test': test, 'cpf': cpf})

@app.get('/')
def get_index(request: Request):
    test = "abwp[oerjwpkortp[werkt[pwerkt[wepk"
    return template.TemplateResponse('index.html', context={'request': request, 'test': test})

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/transactions/", response_model=schemas.Transaction)
def create_transaction_for_user(
    user_id: int, transaction: schemas.TransactionCreate, db: Session = Depends(get_db)
):
    return crud.create_user_transaction(db=db, transaction=transaction,
                                        user_from_id=transaction.user_from_id,
                                       user_to_id=transaction.user_to_id)


@app.get("/transactions/", response_model=List[schemas.Transaction])
def read_transactions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    transactions = crud.get_transactions(db, skip=skip, limit=limit)
    return transactions
