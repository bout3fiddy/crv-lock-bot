import os

import web3
from etherscan.contracts import Contract as EtherscanContract


w3_infura = web3.Web3(
    web3.Web3.HTTPProvider(
        f"https://mainnet.infura.io/v3/{os.environ['WEB3_INFURA_PROJECT_ID']}",
    ),
)


def init_contract(address: str):

    address = web3.Web3.toChecksumAddress(address)
    contract_abi = EtherscanContract(
        address=address,
        api_key=os.environ["ETHERSCAN_API_KEY"],
    ).get_abi()
    contract = w3_infura.eth.contract(address=address, abi=contract_abi)
    return contract
