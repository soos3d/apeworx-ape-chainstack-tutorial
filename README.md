# ApeWorX Ape tutorial using the Chainstack plugin

This repo contains an Ape project and the tutorial shows you how to install the Ape framework, the Chainstack plugin, and how to deploy and interact with smart contracts. 

This tutorial is based on this [Ape tutorial from the Chainstack blog]().

## Install the Ape framework and dependencies 

### Requirements

- Linux or macOS
- Windows Subsystem Linux ([WSL](https://docs.microsoft.com/en-us/windows/wsl/install)) if operating on windows.

> **Note:** For this tutorial, I am installing and using Ape on Ubuntu 22.04 LTS. 

### Dependencies

- [python3](https://www.python.org/downloads) version 3.7.2 or greater
- python3-dev

  - MacOS. Should already have the [correct headers if Python is installed with `brew`](https://stackoverflow.com/questions/32578106/how-to-install-python-devel-in-mac-os)

  - Linux. Install python3-dev with:

  ```sh
  sudo apt-get install python3-dev
  ```

> **Note:** Always check the [Ape docs to find the updated requirements](https://docs.apeworx.io/ape/stable/userguides/quickstart.html#prerequisite).

### Installation

Verify the Python version installed:

```sh
Python3 --version
```

### Virtual environment

It is recommended to operate in a virtual environment; you will need to [install Ape](https://github.com/ApeWorX/ape#installation) in the virtual environment if you decide to use one.

Create a virtual environment.

```sh
python3 -m venv /path/to/new/environment
```

> Keep in mind that you can place the virtual environment where you prefer.

Then activate it.

```sh
source /bin/activate
```

### Install the Ape framework

We can use PIP to install Ape, and we can start by updating it. 

```bash
pip install -U pip 
```

Then install Ape. 

```bash
pip install eth-ape
```

**Note:** You might encounter some errors during the installation. 

For example, I got this error during the installation:

```bash
error: Setup script exited with error: command 'x86_64-linux-gnu-gcc' 
failed with exit status 1 
```

And I solved it by [installing python-dev and build-essential](https://stackoverflow.com/questions/26053982/setup-script-exited-with-error-command-x86-64-linux-gnu-gcc-failed-with-exit).

```bash
sudo apt-get install python3-dev 
sudo apt-get install build-essential 
```

### Install project's dependencies 

For this tutorial you'll need to install the [Chainstack](https://github.com/ApeWorX/ape-chainstack) and [Solidity](https://github.com/ApeWorX/ape-solidity) plugins. Install them by running:

```bash
ape plugins install chainstack solidity
```

## Getting familiar with the Ape console

The Ape framework comes with an interactive console that allows you to interact with the blockchain and your project.

First of all, let's get a [Chainstack](https://chainstack.com/) enpoint ready.

### Set up the endpoint URL 

1. [Sign up with Chainstack](https://console.chainstack.com/user/account/create).  
1. [Deploy a node](https://docs.chainstack.com/platform/join-a-public-network).  
1. [View node access and credentials](https://docs.chainstack.com/platform/view-node-access-and-credentials). 

The next step will be to tell the system the endpoint by creating an environment variable.   

```bash
export CHAINSTACK_GOERLI_URL=https://nd-11X-26X-16X.p2pify.com/YOUR_API_KEY 
```

```bash
Echo $ export CHAINSTACK_GOERLI_URL 
```

And it will return your endpoint URL if it is set up correctly. 

### Create and import accounts 

The `ape accounts generate “ACCOUNT_NAME”` command allows us to generate new accounts.

```bash
ape accounts generate "chainstack" 
```

> Make sure to keep your passphrase accessible since you will need it to sign the transactions later on, but for the purpose of this tutorial, I recommend only using it for testing purposes without real funds. 

Once you have created some accounts, use the `ape accounts list` command to see a list with the addresses and aliases. 
 
```bash
ape accounts list
``` 

```bash
Found 2 accounts: 
  0xB6a6b3096e2E90780b745c676b842b9D2F657540 (alias: 'chainstack') 
  0x82D78356b4D18e0f24D56bE752454728d80C9897 (alias: 'test') 
```

Now we can activate the console, query the balance, make transfers, and more.

> **Note:** You can use this [Goerli faucet](https://goerli-faucet.pk910.de/) to get some Goerli ETH.

At this point, we can start the console on the Chainstack Goerli endpoint. 

```bash
ape console --network ethereum:goerli:chainstack 
```

This will activate the console, where we can load and query our account.
First create a variable for the account to query by using the `accounts.load` method, then we can query the balance.

```bash
In [1]: chainstack_account = accounts.load('chainstack') 
In [2]: chainstack_account.balance / 1e18 
Out[2]: 0.25 
```

### Make transfers between accounts 

We can use the console to transfer tokens between accounts as well.  

In the console, initialize your second account and check its balance: 

```bash
In [4]: test_account = accounts.load("test") 
In [5]: test_account.balance /1e18 
Out[5]: 0.05 
```

Then input the transfer command: 

`SENDER_ACCOUNT.transfer(RECEIVER_ACCOUNT, WEI_AMOUNT)` 

You can use a [wei converter](https://eth-converter.com/) to convert the value that you want to send, or you can create a variable and use the `converter` function offered by Ape. 

```bash
In [14]: value = convert("0.1 ETH", int) 
In [15]: value 
Out[15]: 100000000000000000 
```

We are transferring 0.1 Goerli ETH between `chainstack_account`  and `test_account` in this example. The console will ask you to sign using your passphrase: 

```bash
In [6]: chainstack_account.transfer(test_account, 100000000000000000) 

DynamicFeeTransaction: 
  chainId: 5 
  to: 0x82D78356b4D18e0f24D56bE752454728d80C9897 
  from: 0xB6a6b3096e2E90780b745c676b842b9D2F657540 
  gas: 21000 
  nonce: 0 
  value: 100000000000000000 
  data: 0x 
  type: 0x02 
  maxFeePerGas: 1009999997 
  maxPriorityFeePerGas: 1009999988
  accessList: []   

Sign:  [y/N]: y 
Enter passphrase to unlock 'chainstack' []: 
```

Once the transaction is confirmed, we can verify if it worked.  

```bash
Out[6]: <Receipt 0x49da1da7e0368f35302a80791e8b965de26fa06e92a8919662a8bd8c1375b047> 
In [7]: test_account.balance /1e18 
Out[7]: 0.15 
In [8]: chainstack_account.balance / 1e18 
Out[8]: 0.149978790000063 
```

Ape also comes with a set of a set of pre-defined accounts in case you want to develop locally instead of on a testnet.   

Try the local developent environment by restasting the console with:

```bash
ape console
```

And we can see that we have 10 accounts available.

```bash
In [1]: len(accounts.test_accounts) 
Out[1]: 10 
```

We can associate these accounts to a variable and use them for our development and testing. 

```bash
In [2]: account_1 = accounts.test_accounts[0] 
In [3]: account_1.balance / 1e18 
Out[3]: 1000000.0 
```

## Create a project with Ape 

Now that we are familiar with the console let’s see how to create a project, deploy a contract and interact with it. We’ll work with a simple, smart contract written in Solidity for this tutorial. 

> Keep in mind that you will have to initialize the environment variables with the endpoints again every time you close the terminal unless you store the environment variable in the local file [`~/.bashrc`](https://www.freecodecamp.org/news/bashrc-customization-guide/) (Linux) or [`~/.zshrc`](https://toolspond.com/zshrc/#:~:text=.,interactive%20zsh%20session%20is%20launched.) (macOS) 

We can initialize the project:

Create a directory where you want your project to be in, then you can do: 

```bash
ape init
``` 

And your project will have this structure

```bash
Project root                        # The root project directory 
├── contracts/                      # Project source files, such as '.sol' or '.vy' files 
    └── smart_contract_example.sol  # Sample of a smart contract 
├── tests/                          # Project tests, ran using the 'ape test' command 
    └── test_sample.py              # Sample of a test to run against your sample contract 
├── scripts/                        # Project scripts, such as deploy scripts, ran using the 'ape run   <`name>' command 
    └── deploy.py                   # Sample script to automate a deployment of an ape project 
└── ape-config.yaml                 # The ape project configuration file 
```

Let’s use this simple smart contract, which allows you to save a string on chain (on Goerli in this example) and create a `SimpleStorage.sol` in the `contracts` folder of the project. 

```sol
// SPDX-License-Identifier: MIT 

pragma solidity ^0.8.0; 
 
contract SimpleStorage { 

    string storedWord; 


    function setWord(string memory _word) public { 
    storedWord = _word; 
    } 


    function getWord() public view returns (string memory) { 
    return storedWord; 
    } 

} 
```

### Deploy a smart contract from the console 

Now that we have a smart contract in the correct folder, we need to compile it: 

```bash
ape compile 
```

If everything goes well, there will be a `__local__.json` file in the `.build` directory containing the ABI, bytecode, and other information about the contract. 

Then we can deploy it directly from the Ape console: 

Start the console with the Goerli endpoint that we set up earlier 

```bash
ape console --network ethereum:goerli:chainstack 
```

Initialize the address you want to use to deploy (you need to re-initialize it every time you exit the Ape console), in our case, the address that we created earlier, and deploy from the project manager. Note that we create an instance called `contract` so that we can interact with the contract we deploy.   

```bash
In [1]: dev_account = accounts.load("chainstack") 
In [2]: contract = dev_account.deploy(project.SimpleStorage) 
```

Once we confirm the transaction, the smart contract will be deployed, and the console will show us the address.   

```bash
INFO: Confirmed 0x899009c30ee0ade521bb97cda00ff5b2a157d5fcb3dfcd14ac26755ef7d64237 (total fees paid = 255956003071472) 
SUCCESS: Contract 'SimpleStorage' deployed to: 0xC88bfF0F5e264F4652327010E8eB3ab9c9Cf0372 
```

### Use the console to interact with your smart contract  

At this point, we have already learned a lot about this framework, and we deployed a smart contract on Goerli; it’s time to interact with it.   
The contract we just deployed allows us to save a string on chain and retrieve its value. We can interact with it from the console easily. 

We can for example retrive the contract address like this: 

```bash
In [4]: contract.address 
Out[4]: '0xC88bfF0F5e264F4652327010E8eB3ab9c9Cf0372' 
```

Now, lets save a string on chain by calling the `setWord()` function, we have to specify which account send the transaction and pays for gas, the console will return the receipt as well: 

```bash
In [5]: contract.setWord("Web3 is cool",sender=dev_account) 
Out[5]: <Receipt 0x217cdd40fdfb6d9f47ccbab66bc62f00b3edf094608b3bdf622a36161e7067bd> 
``` 

At this point, calling the `getWord()` function should come easy to you. 

```bash
In [6]: contract.getWord() 
Out[6]: 'Web3 is cool' 
```
 
> Extra tip: the Ape console is a Python interactive environment, so you can create functions to better interact with the smart contract. For example, a function to retrieve and print the string saved In the smart contract directly.   

```bash
In [15]: def word(): 
    ...:     savedWord = contract.getWord() 
    ...:     return savedWord 
    ...:  
  
In [16]: print(word()) 
Web3 is cool 
```

Obviously, because this smart contract is so simple, it seems superfluous, but it can come in handy with more complex applications. 

You can find how to [deploy and interact with smart contracts](https://docs.apeworx.io/ape/stable/userguides/projects.html) in the ApeWorX docs.  

### Deploy a smart contract from a script 

Like in more traditional frameworks such as Brownie, we can deploy contracts and interact with them through a script.   

Follow the previous steps to: 

1 .initialize a new project and place the smart contract file in the contracts folder again; I will use the same contract.   
1. Set the terminal in the project root folder and run 

```bash
ape compile 
```

Now we can create a new file in the scripts folder inside our project and call it `deploy.py`   

We first import the ape modules: `accounts` and `project`. 

Now, we have two options to pick the account we want to use to deploy and sign the transaction. The first is to hardcode it into the script. The following code shows a deploy script with a hardcoded account.   

```python
from ape import accounts, project  

def main(): 
       # Initialize deployer account and print balance 
      dev_account = accounts.load("chainstack") 
      print(f'The account balance is: {dev_account.balance / 1e18} Goerli ETH')  

      # Deploy the smart contract and print a message 
     dev_account.deploy(project.SimpleStorage) 
     print("Contract deployed!") 
```

Note that we also added a few extra print statements to give some extra information. Also, the script must be structured like this with a main() function to work.  

> The `dev_account.deploy(project.SimpleStorage)` line deploys the smart contract; note that the name SimpleStorage, in this case, must be the name of the smart contract, not the `.sol` file. 

Now go back to the terminal (always in the project root folder) and run: 

```bash
ape run deploy --network ethereum:goerli:chainstack 
```

This will prompt you to sign the transaction. 

```bash
The account balance is: 0.3986564444825816 Goerli ETH 

DynamicFeeTransaction: 
  chainId: 5 
  from: 0xB6a6b3096e2E90780b745c676b842b9D2F657540 
  gas: 255956 
  nonce: 9 
  value: 0 
  data: 0x608060...0f0033 
  type: 0x02 
  maxFeePerGas: 1000000016 
  maxPriorityFeePerGas: 1000000001 
  accessList: []   

Sign:  [y/N]: 
```

Once the steps are completed, it will give you a success message and show the contract address. 

```bash
Confirmations (2/2): 100%|████████████████████████████████████████████████████████████████████████████████████| 2/2 [00:29<00:00, 14.77s/it] 
INFO: Confirmed 0xa88e5b15cbad7ce1c8466baff0c21e9ea2e8be606b9a08fb14d30c528ee1e71d (total fees paid = 255956003839340) 
SUCCESS: Contract 'SimpleStorage' deployed to: 0xa15fddEE05b12804797B16345F8d8DeaF7d285A1 
Contract deployed! 
```
And here you go, you just deployed a smart contract using the Ape framework from a script.  

The following script does the same thing, but it gives the option to pick which account you want to use to deploy when you run it. This is suitable if you have multiple accounts and don’t want to hardcode a specific one in the script. 

```py
from ape import project 
from ape.cli import get_user_selected_account  

def main(): 
    # The CLI will ask which account to use 
    dev_account = get_user_selected_account() 
    print(f'The account balance is: {dev_account.balance / 1e18} Goerli ETH')   

    # Deploy the smart contract and print a message 
    dev_account.deploy(project.SimpleStorage) 
    print("Contract deployed!") 
```

Then you run it the same way with `ape run deploy --network ethereum:goerli:chainstack` 

The only difference is that it will prompt you to pick an account to use. 

```bash
0. chainstack 
1. test   

Select an account: 0 
The account balance is: 0.39861173848186626 Goerli ETH 

DynamicFeeTransaction: 
  chainId: 5 
  from: 0xB6a6b3096e2E90780b745c676b842b9D2F657540 
  gas: 255956 
  nonce: 10 
  value: 0 
  data: 0x608060...0f0033 
  type: 0x02 
  maxFeePerGas: 1000000021 
  maxPriorityFeePerGas: 1000000001 
  accessList: []   

Sign:  [y/N]: y 
```

### Interact with a deployed contract 
