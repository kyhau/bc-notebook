import random

from bc_simple.blockchain import *
from bc_simple.node import *

random.seed(0)


def make_sample_transaction(max_value=3):
    # This will create valid transactions in the range of (1, max_value)

    sign = int(random.getrandbits(1)) * 2 - 1   # This will randomly choose -1 or 1
    amount = random.randint(1, max_value)
    alice_pays = sign * amount
    bobby_pays = -1 * alice_pays

    # By construction, this will always return transactions that respect the conservation of tokens.
    # However, note that we have not done anything to check whether these overdraft an account
    return {
        "Alice": alice_pays,
        "Bobby": bobby_pays
    }


def main():
    """Sample run"""

    # Define the initial state
    # Create accounts for our two users (Alice and Bobby) and give them 50 coins each.
    state = {"Alice": 50, "Bobby": 50}

    # Create the "genesis block" (the first block in the system).
    chain = init_blockchain(initial_state=state)

    # Create some transactions
    transaction_buffer = [make_sample_transaction() for i in range(30)]

    chain = make_blocks(chain, state, transaction_buffer)

    # Create the first node
    node_a = Node(chain)

    # Create new transactions and pass to node_a
    node_b_transactions = [make_sample_transaction() for i in range(5)]
    new_block = make_block(node_b_transactions, parent_block=chain[-1])

    node_a.process_new_block(new_block, state)

    for c in node_a.chain:
        print(c["contents"])


if __name__ == "__main__":
    main()