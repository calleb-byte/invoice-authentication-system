
from web3 import Web3
import json

with open("compiled_contract.json", "r") as file:
    compiled = json.load(file)

abi = compiled["contracts"]["InvoiceAuth.sol"]["InvoiceAuth"]["abi"]
bytecode = compiled["contracts"]["InvoiceAuth.sol"]["InvoiceAuth"]["evm"]["bytecode"]["object"]

web3 = Web3(Web3.HTTPProvider("https://goerli.infura.io/v3/YOUR_INFURA_PROJECT_ID"))
account = "YOUR_WALLET_ADDRESS"
private_key = "YOUR_PRIVATE_KEY"
nonce = web3.eth.get_transaction_count(account)

contract = web3.eth.contract(abi=abi, bytecode=bytecode)

txn = contract.constructor().build_transaction({
    "from": account,
    "nonce": nonce,
    "gas": 2000000,
    "gasPrice": web3.to_wei("20", "gwei")
})

signed_txn = web3.eth.account.sign_transaction(txn, private_key=private_key)
tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
print("Contract deployed at:", web3.to_hex(tx_hash))
