from brownie import accounts
import os

def deploy_simple_storage():
 # account = accounts[0]
 # account = accounts.load("freecodecamp-account")
 account = accounts.add(os.getenv("PRIVATE_KEY"))
 print("account: ", account)

def main():
 deploy_simple_storage()