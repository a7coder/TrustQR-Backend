from brownie import (
    accounts,
    network,
    config,
    # Authentication,
)
# from brownie import Products


FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]


def get_account(index=None, id=None):
    if index != None:
        return accounts[index]
    if id != None:
        return accounts.load(id).address
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts.add(config["wallets"]["dummy_key"])


    return accounts.add(config["wallets"]["from_key"])


# def deploy_user():
#     account = get_account()
#     if len(Authentication)==0:
#         contract = Authentication.deploy(
#         {'from': account}, publish_source=config['networks'][network.show_active()].get('verify'))
#     else:
#         contract=Authentication[-1]
#     # inser_dummy_users(account, contract)
#     print('User ',contract)
#     return contract


# def deploy_products():

#     account=get_account()
#     if len(Products)==0:
#         contract=Products.deploy({'from':account},publish_source=config["networks"][network.show_active()].get("verify", False))
#     else:
#         contract=Products[-1]
#     print('Product ',contract)
#     return contract


# def main():
#     deploy_products()
#     deploy_user()