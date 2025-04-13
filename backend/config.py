
INFURA_URL = "https://goerli.infura.io/v3/YOUR_INFURA_PROJECT_ID"
CONTRACT_ADDRESS = "YOUR_DEPLOYED_CONTRACT_ADDRESS"
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
