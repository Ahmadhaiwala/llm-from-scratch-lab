# So these is for learning purpose its just 
# a naive algo just for learning in future I will
# surely implement the rust base updated scalable code

#this is basic implementation of bpe algorithm

class Tokenizer:
    def __init__(self):
        self.vocab = {}
        self.inverse_vocab = {}

    def train(self, text,num_merges=10):
        tokens=list(text)
        for _ in range(num_merges):
            pair_frequecny=self.get_pair_frequency(tokens)
            most_frequent_pair=self.get_most_frequent_pair(pair_frequecny)
            print("Merging:", most_frequent_pair)
            tokens=self.merge_pair(tokens,most_frequent_pair)
            print("Tokens:", tokens)

        counter=0
        for token in tokens:
            if token not in self.vocab:
                self.vocab[token]=counter
                counter+=1
        for token in self.vocab:
            self.inverse_vocab[self.vocab[token]] = token



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
   
    def get_pair_frequency(self, tokens):
        pair_frequency = {}

        for i in range(len(tokens) - 1):
            pair = (tokens[i], tokens[i + 1])

            if pair not in pair_frequency:
                pair_frequency[pair] = 0

            pair_frequency[pair] += 1

        return pair_frequency
   

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
print("for hello hello hello ")
tokenizer.train("hello hello hello", num_merges=5)
print(tokenizer.vocab)
print(tokenizer.inverse_vocab)

