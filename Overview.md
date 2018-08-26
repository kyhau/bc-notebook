# Overview

**Blockchain technology**, which uses math and cryptography, provides a open decentralised database of every
transaction involving value; e.g. money, goods, property or work. 
The authenticity of records can be verified by the entire community.

The blockchain network is made out of interconnected **nodes**. 
Every node owns a copy of blockchain, which is public and accessible to anyone in the network.
The nodes are in charge of validating any transactions received. Once validated, the nodes broadcast the new block transaction to neighbouring until each one in the network has a copy of it.

Like the name indicates, **Blockchain** is a chain of block containing information. Each block contains:
1. data about the transaction, 
1. the hash of the block, and
1. the hash of the previous block.

Each block is then linked to the previous block, creating a chain that can be traced to the first block ever created,
 that is, the **Genesis block**.


## What makes blockchain so secure?

The approach of using hash, Proof of Work and peer-to-peer verification makes it mathematically impossible to fake
transactions in blockchain. 

1. Hash

    A hash is a long string of numbers that identifies each block.
    The hash is created by encrypting the data within the block.
    If the data is altered, the hash will therefore change too.
    This would invalidate the block, as each contains the hash of the previous block too.
    So one incorrect hash in the chain will cause all future hashes to become invalid and therefore will be rejected
    by the network.

1. Proof of work (PoW)

    Each new block must complete a Proof of Work, which is a small mathematical problem that is hard to solve but is
    easy to verify. 
    The protocol requires each new block to encrypt the message, create a unique and valid hash, and embed the hash of
    the previous block. For Bitcoin, this is about 10 minutes.
    
    The Proof of Work is then verified by other nodes in the network before it is added to the block. 
    
    If the process of Proof of Work takes longer than the agreed amount of time, it will be rejected by everyone in the network.
    
    If the hash is found to not match other blocks in that blockchain it will also be rejected by the network.

1. Peer-to-peer verification

    The most powerful protection provided by blockchain is the peer-to-peer consensus that verifies each block. 

    1. When a new node joins, they receive their own copy of the blockchain. 
    1. When a new block attempts to be added, it’s PoW must be verified by each node in the network. 
    1. A consensus (51%) of the network must agree that the new block is valid. 
    1. If the hash is found to not match other blocks in that blockchain it will be rejected by the network.

### Genesis block

A genesis block is the first block of a blockchain. Modern versions of Bitcoin number it as block 0, though very early versions counted it as block 1. The genesis block is almost always hardcoded into the software of the applications that utilize its blockchain. It is a special case in that it does not reference a previous block, and for Bitcoin and almost all of its derivatives, it produces an unspendable subsidy.

[[Source]](https://en.bitcoin.it/wiki/Genesis_block)


### How many transactions in one block (E.g. Bitcoin)?

Transactions are broadcasted by anyone in the system and at random intervals. 
Which transactions, of all the ones broadcasted, are included is very dependent on the miner, as he/she is the one who
groups them up and includes them in the block.

There is also a 1MB block size limit which limits how many transactions can be included in a block. 
This limit is to prevent huge blocks that clog the network and may be removed if the number of transactions in the
network ever grows such that the limit is a serious factor.

Good miners accept all transactions with the standard 0.0001 BTC fee (which is mainly a spam prevention measure).
Bad miners are selfish and avoid including transactions to decrease their propagation time. For example, look at 
[this block](https://blockchain.info/block-height/315076) to see an example where a miner didn't include any
transactions except for their own reward transaction.

If you look at https://blockchain.info then you can see how many transactions are included in each block.

As far as priority goes, again it depends on the miner, but in general miners like bigger fees and smaller transactions
and may prioritize them that way.

[[Source]](https://bitcoin.stackexchange.com/questions/30019/how-many-transactions-in-one-block)

