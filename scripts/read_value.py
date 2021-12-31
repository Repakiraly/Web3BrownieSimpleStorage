from brownie import SimpleStorage, accounts, config


def read_contract():
    # print(SimpleStorage[0])
    # most recent deployment SimpleStorage[-1]
    simple_storage = SimpleStorage[-1]
    #   ABI
    #   ADDRESS
    print("[INFO] Retrieve from Contract...")
    print(simple_storage.retrieve())


def main():
    read_contract()
