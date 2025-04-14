
from web3 import Web3
import json

with open("compiled_contract.json", "r") as file:
    compiled = json.load(file)

abi = compiled["contracts"]["InvoiceAuth.sol"]["InvoiceAuth"]["abi"]
bytecode = compiled["contracts"]["InvoiceAuth.sol"]["InvoiceAuth"]["evm"]["bytecode"]["object"]

web3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/1bf182181f0147939b58df2012ffc249"))
account = "0x9123317C21c16801123BAD11F7e9fe1D5769CBd5"
private_key = "0x84354beca42fdcb10c8b41c4d995a5310040a29beae7f30f607a4ee5b597ea23"
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
