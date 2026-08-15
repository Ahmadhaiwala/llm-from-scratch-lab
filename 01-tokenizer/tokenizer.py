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
    #_________________________________________________________
    #you know what pair frequency is kind of autocompletion tool
    # which is again the most basic thing in the starting of our ai
    #___________________________________________________________
    #we will take the pair that appear most frequently and merge it
    #and repeat the process
    #
    
    #
    def get_pair_frequency(self,tokens):
      #tokens:["lower","lowest","low"]
      #"low" freq:3 and "er"freq:1
        pair_frequecny={}
        for token in tokens:
            for i in range(len(token)-1):
                pair=(token[i],token[i+1])
                if pair not in pair_frequecny:
                    pair_frequecny[pair]=0
                pair_frequecny[pair]+=1
        return pair_frequecny
    #now we will merge the pair that appear most frequently
    #

    def get_most_frequent_pair(self,pair_frequecny):
        max_freq=0
        most_frequent_pair=None
        for pair in pair_frequecny:
            if pair_frequecny[pair]>max_freq:
                max_freq=pair_frequecny[pair]
                most_frequent_pair=pair
        return most_frequent_pair
    
    def merge_pair(self, tokens, pair):
        i = 0
        res_pair = []

        while i < len(tokens) - 1:
            if tokens[i] == pair[0] and tokens[i + 1] == pair[1]:
                res_pair.append(pair[0] + pair[1])
                i += 2
            else:
                res_pair.append(tokens[i])
                i += 1

        if i < len(tokens):
            res_pair.append(tokens[i])

        return res_pair
            


    
    

        
                


    

#testing
tokenizer=Tokenizer()
tokenizer.train("hello world")
print(tokenizer.vocab)
print(tokenizer.inverse_vocab)
encoded = tokenizer.encode("hello world")

print(encoded)
print(tokenizer.decode(encoded))