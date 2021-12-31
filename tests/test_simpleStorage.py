from brownie import SimpleStorage, accounts


def test_deploy():
    # Arrange
    expected = 0
    account = accounts[0]
    # Act
    simple_storage = SimpleStorage.deploy({"from": account})
    actual = simple_storage.retrieve()
    # Assert
    assert actual == expected


def test_update():
    # Arrange
    expected = 15
    account = accounts[0]
    # Act
    simple_storage = SimpleStorage.deploy({"from": account})
    tx = simple_storage.store(15, {"from": account})
    tx.wait(1)
    actual = simple_storage.retrieve()
    # Assert
    assert actual == expected
