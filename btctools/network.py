import os
from enum import Enum, unique


@unique
class NETWORK(Enum):
    MAIN = 'main'
    TEST = 'test'


current_network = NETWORK(os.environ.get('CRYPTOTOOLS_NETWORK', 'main'))

main = {
    'hrp': 'bc',
    'keyhash': b'\x00',
    'scripthash': b'\x05',
    'wif': b'\x80',
    'xprv': b'\x04\x88\xb2\x1e',
    'xpub': b'\x04\x88\xad\xe4',
    'utxo_url': 'https://blockchain.info/unspent?active={address}',
    'rawtx_url': 'https://blockchain.info/rawtx/{txid}?format=hex',
    'broadcast_url': 'https://blockchain.info/pushtx'

}

test = {
    'hrp': 'tb',
    'keyhash': b'\x6f',
    'scripthash': b'\xc4',
    'wif': b'\xef',
    'xprv': b'\x04\x35\x87\xcf',
    'xpub': b'\x04\x35\x83\x94',
    'utxo_url': 'https://testnet.blockchain.info/unspent?active={address}',
    'rawtx_url': 'https://testnet.blockchain.info/rawtx/{txid}?format=hex',
    'broadcast_url': 'https://testnet.blockchain.info/pushtx'
}

networks = {
    NETWORK.MAIN: main,
    NETWORK.TEST: test
}


def network(attr):
    net = networks[current_network]
    return net[attr]
