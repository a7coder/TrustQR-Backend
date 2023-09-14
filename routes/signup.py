from fastapi import APIRouter
from fastapi import Request
from routes.encoding import encrypt, is_strong_password, is_valid_email
from helper import add_newUser


user_router = APIRouter(prefix='/api/users',)


@user_router.post('/signup')
async def Signup(request: Request):
  credentials = await request.json()
  user = credentials['Email']
  password = credentials['Password']
  if is_valid_email(user) == False or is_strong_password(password) == False:
    return ({'id': 'Invalid Username or Password'})
  # print(f"user : {user}  Password : {password}")
  encoded_user = encrypt(user)
  encoded_password = encrypt(password)
  user_contract = request.app.state.Authentication
  # print(user_contract)
  # print('isUser : ',isUser(user_contract, encoded_user))
  contract_response = add_newUser(
      encoded_user, encoded_password, user_contract)
  response = {'id': contract_response['msg']}
  if contract_response['success']:
      response['id'] = encoded_user
  # print(response)
  return (response)

