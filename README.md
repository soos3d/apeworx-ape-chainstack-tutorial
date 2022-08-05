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

