import re

from app.auth.schemas import LoginBody, RegisterBody
from app.models import get_session
from datetime import datetime
from fastapi import Depends
from passlib.context import CryptContext
from sqlmodel import select, Session

from app.models.user import User


pass_ctx = CryptContext(schemes=['bcrypt'], deprecated='auto')
HASH_SECRET = 'qhlHwy8W8eu0S80hxq2h382cTQrJyqyDJiJlCVRBh'

RE_DATE = re.compile("^[0-9]{4}/[0-9]{2}/[0-9]{2}$")

def list_users(session: Session = Depends(get_session)):
    users = session.exec(select(User)).all()
    return [user.model_dump() for user in users]

def login(body: LoginBody, session: Session = Depends(get_session)):
    return {'success': False}

def register(body: RegisterBody, session: Session = Depends(get_session)):
    # Verify email is valid
    if not re.match(r'^.{2,}?@.{2,}?\..{2,}$', body.email):
        return {
            'success': False,
            'error': 'invalid-email',
            'message': 'The email does not follow a valid format.',
        }

    # Validate length of some values
    if len(body.name) < 3:
        return {
            'success': False,
            'error': 'name-length',
            'message': 'Name should be at least 3 characters.',
        }

    if len(body.password) < 8:
        return {
            'success': False,
            'error': 'password-length',
            'message': 'Password should be at least 8 characters.',
        }

    # Validate passwords match
    if body.password != body.confirmPassword:
        return {
            'success': False,
            'error': 'password-mismatch',
            'message': 'The provided passwords do not match.',
        }

    # Check if email is already taken
    query = select(User).where(User.email == body.email)
    existing_user = session.exec(query).first()
    if existing_user is not None:
        return {
            'success': False,
            'error': 'user-exists',
            'message': 'There is already an account associated with that email.',
        }

    # Check birth date
    if not RE_DATE.match(body.birthDate):
        return {
            'success': False,
            'error': 'invalid-birth-date',
            'message': 'Invalid format provided for the birth date.',
        }
    
    birth_date = datetime.strptime(body.birthDate, '%Y/%m/%d').date()
    user = User(email=body.email,
                name=body.name,
                password=pass_ctx.hash(body.password),
                birth_date=birth_date)
    session.add(user)
    session.commit()

    return {'success': True, 'user': user.model_dump()}

