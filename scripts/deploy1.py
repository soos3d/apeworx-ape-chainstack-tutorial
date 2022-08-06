# rename this to deploy.py and rename the other filed to something else in case you want to use this one. 

from ape import accounts, project


def main():

    # Initialize deployer account and print balance
    dev_account = accounts.load("chainstack")
    print(f'The account balance is: {dev_account.balance / 1e18} Goerli ETH') # Just for information/example

    # Deploy the smart contract and print a message
    dev_account.deploy(project.SimpleStorage)
    print("Contract deployed!")



