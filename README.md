# Web 3 Transactions Fetcher

This is a simple Python script to fetch an array of transactions from a particular wallet on any Ethereum or Ethereum-compatible blockchain networks. You can modify the `transaction_finder.py` script to add additional filters or change the request model.

## Installing

1. Clone the repository and navigate into the cloned folder:
```shell
git clone https://github.com/znx-x/web3-transactions-fetcher && cd web3-transactions-fetcher
```

2. Install the dependencies:
```shell
python3 -m pip install web3
```

All done!

## Running

1. Run the `transaction_finder.py` script:
```shell
python3 transaction_finder.py
```

2. If the operation succeeds, you should see a `transactions.pkl` file being created. This file stores the RPC response to the request sent through by the `transaction_finder.py` script. To read it, you can run the `output_reader.py` script:
```shell
python3 output_reader.py
```