#!/usr/bin/env python3
import random

print("===== Welcome to pretty shop =====")
print("Can you help me beautify these sentences?")
print("Rule 1 : change all ' -_' to ' '")
print("Rule 2 : change all alphabet to lower case")

print("----- Example -----")
print("sentence : ThiS-iS_tEst tRY to BeautIfY_mE")
print("answer : this is test try to beautify me")

words = ['perceive', 'pen', 'contempt', 'payment', 'admiration', 'neck', 'miss', 'defeat', 'hand', 'gift', 'owe', 'referee', 'trap', 'quaint', 'cigarette', 'confrontation', 'innocent', 'hunter', 'school', 'dip']

print("----- Now You Turn -----")

random.shuffle(words)
sentence = ''
ans = ' '.join(words[:15])
for word in words[:15]:
    if sentence:
        sentence += random.choice([' ', '_', '-'])
    for c in word:
        if random.randint(0, 1) == 1:
            sentence += c.upper()
        else:
            sentence += c

print(f"sentence : {sentence}")
answer = input('answer : ').strip()
if answer == ans:
    print('Accepted')
    with open('./flag') as f:
        flag = f.read().strip()
        print(f'Here is your flag : {flag}')
else:
    print('Wrong Answer')
