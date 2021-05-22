from brownie import CoffeeCoin, accounts

def main():
    acct = accounts.load('deploy_account')
    tx = acct.deploy(CoffeeCoin)