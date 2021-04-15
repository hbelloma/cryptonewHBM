class Blockchain (object):  #The blockchain
	def __init__(self):
		self.chain = [self.addGenesisBlock()];
		self.pendingTransactions = []; #Transactions that are waiting to de adding to the blockchain
		self.difficulty = 2;     #dificultad
		self.minerRewards = 50;  #Recompensa de minado
		self.blockSize = 10;     #Tamaño de bloque
		self.nodes = set();
	
	def addTransaction(self, sender, reciever, amt, keyString, senderKey):
		keyByte = keyString.encode("ASCII");
		senderKeyByte = senderKey.encode("ASCII");

		#print(type(keyByte), keyByte);

		key = RSA.import_key(keyByte);
		senderKey = RSA.import_key(senderKeyByte);

		if not sender or not reciever or not amt:
			print("transaction error 1");
			return False;

		transaction = Transaction(sender, reciever, amt);

		transaction.signTransaction(key, senderKey);

		if not transaction.isValidTransaction():
			print("transaction error 2");
			return False;
		self.pendingTransactions.append(transaction);
		return len(self.chain) + 1;
		
	def getLastBlock(self):
        	return self.chain[-1];
    	def addBlock(self, block):
        	if(len(self.chain) > 0):
            		block.prev = self.getLastBlock().hash;
        	else:
            		block.prev = "none";
        	self.chain.append(block);
	
	def chainJSONencode(self): #envia la info a un archivo json

		blockArrJSON = [];
		for block in self.chain:
			blockJSON = {};
			blockJSON['hash'] = block.hash;
			blockJSON['index'] = block.index;
			blockJSON['prev'] = block.prev;
			blockJSON['time'] = block.time;
			blockJSON['nonse'] = block.nonse;
			#blockJSON['gym'] = block.gym;


			transactionsJSON = [];
			tJSON = {};
			for transaction in block.transactions:
				tJSON['time'] = transaction.time;
				tJSON['sender'] = transaction.sender;
				tJSON['reciever'] = transaction.reciever;
				tJSON['amt'] = transaction.amt;
				tJSON['hash'] = transaction.hash;
				transactionsJSON.append(tJSON);

			blockJSON['transactions'] = transactionsJSON;

			blockArrJSON.append(blockJSON);

		return blockArrJSON;
	
	def chainJSONdecode(self, chainJSON):  #decodifica archivo json
		chain=[];
		for blockJSON in chainJSON:

			tArr = [];
			for tJSON in blockJSON['transactions']:
				transaction = Transaction(tJSON['sender'], tJSON['reciever'], tJSON['amt']);
				transaction.time = tJSON['time'];
				transaction.hash = tJSON['hash'];
				tArr.append(transaction);


			block = Block(tArr, blockJSON['time'], blockJSON['index']);
			block.hash = blockJSON['hash'];
			block.prev =blockJSON['prev'];
			block.nonse = blockJSON['nonse'];
			#block.gym = blockJSON['gym'];

			chain.append(block);
		return chain;
	
	
class Block (object):     #The block
	def __init__(self, transactions, time, index):
		self.index = index; #Block number 
		self.transactions = transactions; #Transaction data
		self.time = time; #Time of the block is created
		self.prev = '';  #Hash of previous blocks
		self.nonse = 0;
		#self.gym = self.calculateGym();   #hash of gym
		self.hash = self.calculateHash(); #hash of block
    
	def calculateHash(self):

		hashTransactions = "";

		for transaction in self.transactions:
			hashTransactions += transaction.hash;
		hashString = str(self.time) + hashTransactions + self.prev + str(self.index);
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
