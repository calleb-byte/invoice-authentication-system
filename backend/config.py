
INFURA_URL = "https://mainnet.infura.io/v3/1bf182181f0147939b58df2012ffc249"
CONTRACT_ADDRESS = "0x5c4B3fC5B79c6cfeD886bc8BD0b6Fd72DA4165CF"
ABI = [
    {
        "inputs": [
            {"internalType": "string", "name": "invoiceNumber", "type": "string"},
            {"internalType": "string", "name": "clientName", "type": "string"},
            {"internalType": "uint256", "name": "amount", "type": "uint256"},
            {"internalType": "string", "name": "phoneNumber", "type": "string"}
        ],
        "name": "recordInvoice",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    }
]
