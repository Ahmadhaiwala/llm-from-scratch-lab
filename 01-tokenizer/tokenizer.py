class Tokenizer:
    def __init__(self):
        self.vocab = {}
        self.inverse_vocab = {}

    def train(self, text):
        counter = 0

        for char in text:
            if char not in self.vocab:
                self.vocab[char] = counter
                counter += 1

        for char in self.vocab:
            self.inverse_vocab[self.vocab[char]] = char

    def encode(self, text):
        ids=[]
        for i in text:
            ids.append(self.vocab[i])
        return ids



    def decode(self, ids):
        chars = []

        for id in ids:
            chars.append(self.inverse_vocab[id])

        return "".join(chars)
    
    def get_pair_frequency(self,tokens):

        for i in token:
            for j in i:
                


    

#testing
tokenizer=Tokenizer()
tokenizer.train("hello world")
print(tokenizer.vocab)
print(tokenizer.inverse_vocab)
encoded = tokenizer.encode("hello world")

print(encoded)
print(tokenizer.decode(encoded))