from  SimpleBlockchainexample import*
#from  SimpleBlockchainexample import Blockchain, Transaction, Block;
from time import time;
import pprint

pp=pprint.PrettyPrinter(indent=4)

SimpleBlockchainexample=Blockchain();
transaction=Transaction[];
#transaction=Transaction("Hue G. Rection", "Moe Lester", 10); #forsecond example

block=Block(transactions,time(),0);
SimpleBlockchainexample.addBlock(block);
block=Block(transactions,time(),1);
SimpleBlockchainexample.addBlock(block);
block=Block(transactions,time(),2);
SimpleBlockchainexample.addBlock(block);

pp.print(SimpleBlockchainexample.chainJSONencode());
print("Length:", len(SimpleBlockchainexample.chain));
