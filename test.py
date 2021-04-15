from  SimpleBlockchainexample import*
#from  SimpleBlockchainexamplePoW import Blockchain, Transaction, Block;
from time import time;
import pprint

pp=pprint.PrettyPrinter(indent=4)

SimpleBlockchainexample=Blockchain();
transaction=Transaction[];
#transaction=Transaction("Hue G. Rection", "Moe Lester", 10); #forsecond example

#comment this when transaction, mining and PoW is added into the SimpleBlockchainexample,py
block=Block(transactions,time(),0);
SimpleBlockchainexample.addBlock(block);
block=Block(transactions,time(),1);
SimpleBlockchainexample.addBlock(block);
block=Block(transactions,time(),2);
SimpleBlockchainexample.addBlock(block);

#uncomment for example with pending transaction, mining and PoW is added
#SimpleBlockchainexamplePoW.pendingTransactions.append(transaction);
#SimpleBlockchainexamplePow.minePendingTransactions("Nang");

pp.print(SimpleBlockchainexample.chainJSONencode());
print("Length:", len(SimpleBlockchainexample.chain));
