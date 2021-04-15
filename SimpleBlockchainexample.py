class Blockchain (object):  #The blockchain
	def __init__(self):
		self.chain = [];
class Block (object):     #The block
	def __init__(self, transactions, time, index):
		self.index = index; #Block number 
		self.transactions = transactions; #Transaction data
		self.time = time; #Time of the block is created
		self.prev = '';  #Hash of previous blocks
		#self.nonse = 0;
		#self.gym = self.calculateGym();   #hash of gym
		self.hash = self.calculateHash(); #hash of block
    
   
  def calculateHash(self):

		hashTransactions = "";

		for transaction in self.transactions:
			hashTransactions += transaction.hash;
		hashString = str(self.time) + hashTransactions + self.gym + self.prev + str(self.nonse);
		hashEncoded = json.dumps(hashString, sort_keys=True).encode();
		return hashlib.sha256(hashEncoded).hexdigest();  #SHA256 Hash encoding -same as bitcoin
  
class Transaction (object):
	def __init__(self, sender, reciever, amt):
		self.sender = sender;
		self.reciever = reciever;
		self.amt = amt;
		self.time = time(); #time of transacction is created
		self.hash = self.calculateHash();  #Hash of transaction
    
  def calculateHash(self):
		hashString = self.sender + self.reciever + str(self.amt) + str(self.time);
		hashEncoded = json.dumps(hashString, sort_keys=True).encode();
		return hashlib.sha256(hashEncoded).hexdigest();  #SHA256 Hash encoding -same as bitcoin
