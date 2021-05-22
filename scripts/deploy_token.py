from brownie import web3, CoffeeCoin, accounts
import json
import os

def main():
    priv_key = web3.eth.account.decrypt(
        json.loads(os.environ["DEPLOY_ACCOUNT"]), os.environ["DEPLOY_ACCOUNT_PASSWORD"])
    acct = accounts.add(private_key=priv_key)
    tx = acct.deploy(CoffeeCoin)