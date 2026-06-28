import random
import string
from collections import Counter
import json

class FrequencyAnalysisCTF:
    def __init__(self):
        self.substitution_map = {}
        self.reverse_map = {}
        self.frequency_map = {}
        
    def generate_substitution(self):
        alphabet = list(string.ascii_lowercase)
        shuffled = alphabet.copy()
        random.shuffle(shuffled)
        
        self.substitution_map = dict(zip(alphabet, shuffled))
        self.reverse_map = {v: k for k, v in self.substitution_map.items()}
        
        return self.substitution_map
    
    def encrypt(self, text):
        result = ""
        for char in text.lower():
            if char in self.substitution_map:
                result += self.substitution_map[char]
            else:
                result += char
        return result
    
    
def read_training_text(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

def generate_challenge():
    training_text = read_training_text('demo.txt')
    ctf = FrequencyAnalysisCTF()
    substitution_map = ctf.generate_substitution()
    flag = open('./flag', 'r').read()
    encrypted_flag = ctf.encrypt(flag)
    sample_text = training_text[:500]
    encrypted_sample = ctf.encrypt(sample_text)
    challenge_description = f"""
what are yall talking about ????

hehe Flag：
{encrypted_flag}

hehe sAmple：
{encrypted_sample}

"""
    return challenge_description

challenge_text = generate_challenge()
print(challenge_text)
