from brownie import accounts, config, SimpleStorage


def deploy_simpleStorage():
    account = accounts[0]
    # account = accounts.load("test_brownie")
    # account = accounts.add(config["wallets"]["from_key"])
    # print(account)
    #   Brownie Is Intelligent: Knows when to make a call or transact
    print("[INFO] Deploying Contract...")
    simple_storage = SimpleStorage.deploy({"from": account})
    print("[INFO] Contract Deployed")
    print(simple_storage)
    stored_value = simple_storage.retrieve()
    print(stored_value)
    print("[INFO] Updating Contract...")
    tx = simple_storage.store(15, {"from": account})
    tx.wait(1)
    print("[INFO] Contract Updated")
    stored_value = simple_storage.retrieve()
    print(stored_value)


def main():
    deploy_simpleStorage()
