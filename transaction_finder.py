# import dependencies
import pickle
from transaction_finder import Web3, HTTPProvider

# instantiate a web3 remote provider
# use any Ethereum or Ethereum-compatible provider
# it supports custom networks too
w3 = Web3(HTTPProvider('RPC_URL'))

# request the latest block number
ending_blocknumber = w3.eth.blockNumber

# set the starting block number to current block minus 100
# you can set starting_blocknumber to 0 if you want to query
# the entire blockchain history, but this may take a long
# time to process as it runs each block, one at a time
starting_blocknumber = ending_blocknumber - 100 

# filter through blocks and look for transactions involving this address
blockchain_address = "WALLET_ADDRESS"

# create an empty dictionary we will add transaction data to
tx_dictionary = {}

# check blocks and write output into a filed called 'transactions.pkl'
def getTransactions(start, end, address):
    print(f"Started filtering through block number {start} to {end} for transactions involving the address - {address}...")
    for x in range(start, end):
        block = w3.eth.getBlock(x, True)
        for transaction in block.transactions:
            if transaction['to'] == address or transaction['from'] == address:
                with open("transactions.pkl", "wb") as f:
                    hashStr = transaction['hash'].hex()
                    tx_dictionary[hashStr] = transaction
                    pickle.dump(tx_dictionary, f)
                f.close()
    print(f"Finished searching blocks {start} through {end} and found {len(tx_dictionary)} transactions")
    

getTransactions(starting_blocknumber, ending_blocknumber, blockchain_address)