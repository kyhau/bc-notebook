import hashlib
import json
import sys


def init_blockchain(initial_state):
    """
    There is nothing on the blockchain.
    Get things started by defining the "genesis block" (the first block in the system).
    """
    genesis_block_transactions = [initial_state]
    genesis_block = make_block(genesis_block_transactions, parent_block=None)

    # genesis_block_str = json.dumps(genesis_block, sort_keys=True)
    chain = [genesis_block]
    return chain


def update_state(state, transaction):
    """
    Update state (does not validate the transaction).

    :param state: dict with account name as key, account balance as value
    :param transaction: dict with account name as key, transfer amount as value
    :return: Updated state, with additional users added to state if necessary
    """

    # As dictionaries are mutable, avoid any confusion by creating a working copy of the data.
    state = state.copy()
    for key in transaction:
        if key in state.keys():
            state[key] += transaction[key]
        else:
            state[key] = transaction[key]
    return state


def is_valid_transaction(transaction, state):
    """
    Check if a transacton is valid

    :param transaction:
    :param state:
    :return: True if the transaction is valid; False otherwise
    """
    # Assume that the transaction is a dictionary keyed by account names

    # Check that the sum of the deposits and withdrawals is 0
    if sum(transaction.values()) != 0:
        return False

    # Check that the transaction does not cause an overdraft
    for key in transaction.keys():
        if key in state.keys():
            acc_balance = state[key]
        else:
            acc_balance = 0
        if (acc_balance + transaction[key]) < 0:
            return False

    return True


def make_block(transactions, parent_block):
    """
    For each block, we want to collect a set of transactions, create a header, hash it, and add it to the chain
    
    :param transactions:
    :param parent_block: None if this is the first transaction of a new chain, so no parent
    :return:
    """
    parent_hash = None
    block_number = 0
    if parent_block:
        parent_hash = parent_block["hash"]
        block_number = parent_block["contents"]["block_number"] + 1

    block_contents = {
        "block_number": block_number,
        "parent_hash": parent_hash,
        "transaction_count": len(transactions),
        "transactions": transactions
    }
    return {
        "hash": hash_me(block_contents),
        "contents": block_contents
    }


def make_blocks(chain, state, transactions, block_size_limit=5):
    """
    Make some sample blocks

    :param chain:
    :param state:
    :param transactions:
    :param block_size_limit:
               Arbitrary number of transactions per block; this is chosen by the block miner, and can
               vary between blocks!
    :return:
    """
    while len(transactions) > 0:
        # Gather a set of valid transactions for inclusion
        transaction_list = []

        while (len(transactions) > 0) and (len(transaction_list) < block_size_limit):
            new_transaction = transactions.pop()

            if is_valid_transaction(new_transaction, state):
                transaction_list.append(new_transaction)
                state = update_state(state, new_transaction)
            else:
                # This was an invalid transaction; ignore it and move on
                print("Ignored transaction")
                sys.stdout.flush()
                continue

        # Make a block
        myBlock = make_block(transaction_list, parent_block=chain[-1])
        chain.append(myBlock)

    return chain


def check_chain(chain):
    """
    Work through the chain from the genesis block (which gets special treatment),
    checking that all transactions are internally valid,
    that the transactions do not cause an overdraft,
    and that the blocks are linked by their hashes.
    This returns the state as a dictionary of accounts and balances,
    or returns False if an error was detected

    :param chain:
    :return:
    """

    ## Data input processing: Make sure that our chain is a list of dicts
    if type(chain) == str:
        try:
            chain = json.loads(chain)
            assert (type(chain) == list)
        except:  # This is a catch-all, admittedly crude
            return False
    elif type(chain) != list:
        return False

    state = {}
    ## Prime the pump by checking the genesis block
    # We want to check the following conditions:
    # - Each of the transactions are valid updates to the system state
    # - Block hash is valid for the block contents

    for transaction in chain[0]["contents"]["transactions"]:
        state = update_state(state, transaction)

    check_block_hash(chain[0])
    parent = chain[0]

    ## Checking subsequent blocks: These additionally need to check
    #    - the reference to the parent block"s hash
    #    - the validity of the block number
    for block in chain[1:]:
        state = check_block_validity(block, parent, state)
        parent = block

    return state


def check_block_validity(block, parent, state):
    """
    Check the following conditions:
    - Each of the transactions are valid updates to the system state
    - Block hash is valid for the block contents
    - Block number increments the parent block number by 1
    - Accurately references the parent block"s hash

    :param block:
    :param parent:
    :param state:
    :return:
    """
    parent_number = parent["contents"]["block_number"]
    parent_hash = parent["hash"]
    block_number = block["contents"]["block_number"]

    # Check transaction validity; throw an error if an invalid transaction was found.
    for transaction in block["contents"]["transactions"]:
        if is_valid_transaction(transaction, state):
            state = update_state(transaction, state)
        else:
            raise Exception(f"Invalid transaction in block {block_number}: {transaction}")

    check_block_hash(block)  # Check hash integrity; raises error if inaccurate

    if block_number != (parent_number + 1):
        raise Exception(f"Hash does not match contents of block {block_number}")

    if block["contents"]["parent_hash"] != parent_hash:
        raise Exception(f"Parent hash not accurate at block {block_number}")

    return state


def check_block_hash(block):
    """
    Raise an exception if the hash does not match the block contents.

    :param block:
    :raise: Exception if the hash does not match the block contents.
    """
    expected_hash = hash_me(block["contents"])
    if block["hash"] != expected_hash:
        raise Exception(f"Hash does not match contents of block {block['contents']['block_number']}")


def hash_me(msg=""):
    """Helper function wrapping hashing algorithm
    """
    if type(msg) != str:
        # Sort keys to guarantee repeatability
        msg = json.dumps(msg, sort_keys=True)

    if sys.version_info.major == 2:
        return unicode(hashlib.sha256(msg).hexdigest(), "utf-8")
    else:
        return hashlib.sha256(str(msg).encode("utf-8")).hexdigest()
