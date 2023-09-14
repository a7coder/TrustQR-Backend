from fastapi import APIRouter
from fastapi import Request
from routes.encoding import encrypt, is_valid_email
from helper import validateUser


# APIRouter creates path operations for user module

login_router = APIRouter(prefix='/api/users',)


@login_router.post('/login')
async def Signup(request: Request):
    credentials = await request.json()
    user = credentials['Email']
    password = credentials['Password']

    if is_valid_email(user) == False:
        return ({'id': 'Invalid Username or Password'})


    encoded_user = encrypt(user)
    encoded_password = encrypt(password)

    user_contract = request.app.state.Authentication
   
    contract_response = validateUser(encoded_user, encoded_password, user_contract)
    response = {'id': False}
    if contract_response['success']:
        response['id'] = encoded_user


    return (response)

