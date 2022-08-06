from ape import project
from ape.cli import get_user_selected_account


def main():
    # The CLI will ask which account to use
    dev_account = get_user_selected_account()
    print(f'The account balance is: {dev_account.balance / 1e18} Goerli ETH') 

    # Deploy the smart contract and print a message
    dev_account.deploy(project.SimpleStorage)
    print("Contract deployed!")