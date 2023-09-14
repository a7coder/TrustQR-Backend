from brownie import (
    accounts,
    network,
    config,
  
)
from blockchain.scripts.helper import get_account


FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]


def add_newUser(user, passw, contract):
    account = get_account()
   
    if contract.isUserExists(user,{'from': account}):
        return {
            'success': False,
            'msg': 'User already exsist'
        }

    transation = contract.addUser(user, passw, {'from': account})
    transation.wait(1)
    return {
        'success': True,
        'msg': 'User Created'
    }


def validateUser(user, password, contract):
    account = get_account()
    if contract.isUserExists(user,{'from': account}):
        contract_password = contract.validateUser.call(user, {'from': account})
        if (contract_password == password):
            return {
                'success': True,
                'msg': 'Valid User'
            }

        return {
            'success': False,
            'msg': 'Password Missmatch'
        }

    return {
        'success': False,
        'msg': 'User does Not exsist'
    }


def isUser(user_id,contract):
  
    if contract.isUserExists(user_id,{'from':get_account()}) :
        return True
    return False


# Product *******************************************************

def add_product(email,product_id,product_name,product_description,product_category,country_of_origin,date_of_expiry,date_of_manufacturing,price,urls,key,contract):
   
    if contract.checkProductExist(key,{'from':get_account()}):
      
        return {
            "success":"false",
            'msg':'Product ID Already Present'
        }
    
    txs=contract.addProduct(email,product_id,product_name,product_description,product_category,country_of_origin,date_of_expiry,date_of_manufacturing,price,urls,key,{'from':get_account()})

    txs.wait(1)

    return {
            "success":"true",
            'msg':'Product Added'
        }

def list_all_products(email,contract):
    
    res=list(contract.listProducts(email,{'from':get_account()}))
    # print('ALL PRoduct si ',len(res))
    for i in range(len(res)):
        # print(res[i])
        res[i]=list(res[i])
        res[i][7]=res[i][7]/100
        res[i][2]=res[i][2][:10]
    
    return res


def get_detail_product(email,product_id,contract):

    res=list(contract.productDetail(email,product_id,{'from':get_account()}))
    res[7]=res[7]/100


    return res

