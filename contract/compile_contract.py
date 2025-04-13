
from solcx import compile_standard, install_solc
import json

install_solc("0.8.0")
with open("InvoiceAuth.sol", "r") as file:
    contract_source = file.read()

compiled = compile_standard({
    "language": "Solidity",
    "sources": {
        "InvoiceAuth.sol": {"content": contract_source}
    },
    "settings": {
        "outputSelection": {
            "*": {"*": ["abi", "metadata", "evm.bytecode"]}
        }
    }
}, solc_version="0.8.0")

with open("compiled_contract.json", "w") as out_file:
    json.dump(compiled, out_file)
