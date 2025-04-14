
from web3 import Web3
from config import INFURA_URL, CONTRACT_ADDRESS, ABI

web3 = Web3(Web3.HTTPProvider(INFURA_URL))
contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=ABI)
sender_address = "0x9123317C21c16801123BAD11F7e9fe1D5769CBd5"
private_key = "0x84354beca42fdcb10c8b41c4d995a5310040a29beae7f30f607a4ee5b597ea23"

def record_invoice_on_chain(data):
    nonce = web3.eth.get_transaction_count(sender_address)
    txn = contract.functions.recordInvoice(
        data['invoice_number'],
        data['client_name'],
        int(data['amount']),
        data['phone_number']
    ).build_transaction({
        'chainId': 5,
        'gas': 200000,
        'gasPrice': web3.to_wei('20', 'gwei'),
        'nonce': nonce
    })

    signed_txn = web3.eth.account.sign_transaction(txn, private_key=private_key)
    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    return web3.to_hex(tx_hash)
