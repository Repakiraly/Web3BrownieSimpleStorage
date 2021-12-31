from brownie import SimpleStorage, accounts

#   Tips:
#   1. brownie test -k FUNCTION --> only one function is tested
#   2. brownie test --pdb --> similar to gdb (AWESOME)
#   3. brownie test -s --> printlines and PASSED


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
