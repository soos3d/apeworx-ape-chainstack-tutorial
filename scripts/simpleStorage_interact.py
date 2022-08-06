
from ape import project
from ape.cli import get_user_selected_account

def simpleStorage_interact():
    # The CLI will ask which account to use
    dev_account = get_user_selected_account()
    print(f'The account balance is: {dev_account.balance / 1e18} Goerli ETH') 

    # Initialize latest deployed contract
    simple_storage= project.SimpleStorage.deployments[-1]    
    print(f'The latest SimpleStorage contract is deployed at: {simple_storage.address}')

    # Prompt the user to input a string to save 
    string_to_save = input("Type the string to save: ")
    
    print("Saving the string, please sign the transaction when prompted.")
    simple_storage.setWord(string_to_save, sender=dev_account)

    # Retrive and display the saved string 
    print(f'The saved string is: {simple_storage.getWord()}')

def main():
    simpleStorage_interact()