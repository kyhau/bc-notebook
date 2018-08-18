"""
When we initially set up our node, we will download the full blockchain history.
After downloading the chain, we would need to run through the blockchain to compute the state of the system.
To protect against somebody inserting invalid transactions in the initial chain, we need to check the validity
of the entire chain in this initial download.

Once our node is synced with the network (has an up-to-date copy of the blockchain and a representation of
system state) it will need to check the validity of new blocks that are broadcast to the network.

In an actual blockchain network, new nodes would download a copy of the blockchain and verify it,
then announce their presence on the peer-to-peer network and start listening for transactions.

Bundling transactions into a block, they then pass their proposed block on to other nodes.

If we receive a block from somewhere else, verifying it and adding it to our blockchain is easy.
"""
import copy
from bc_simple.blockchain import *


class Node(object):
    def __init__(self, chain):
        print("Get a copy of the blockchain and verify it...")

        check_chain(chain)
        self.chain = copy.copy(chain)

        print(f"Blockchain on Node A is currently {len(self.chain)} blocks long")

    def process_new_block(self, new_block, state):
        print("New block received; checking validity...")
        try:
            # Update the state- this will throw an error if the block is invalid!
            state = check_block_validity(new_block, self.chain[-1], state)

            self.chain.append(new_block)
        except:
            print("Invalid block; ignoring and waiting for the next block...")

        print(f"Blockchain on Node A is currently {len(self.chain)} blocks long")
