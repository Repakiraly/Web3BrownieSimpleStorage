from brownie import accounts, config, SimpleStorage, network


def deploy_simpleStorage():
    # account = accounts[0]
    # account = accounts.load("test_brownie")
    # account = accounts.add(config["wallets"]["from_key"])
    # print(account)
    account = get_account()
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
    updated_value = simple_storage.retrieve()
    print(updated_value)


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        if network.show_active() == "ftm-test":
            return accounts.add(config["wallets"]["from_key_ftm"])
        else:
            return accounts.add(config["wallets"]["from_key"])


def main():

    deploy_simpleStorage()
