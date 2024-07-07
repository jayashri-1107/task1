import random
import hangman_stages
import word
# w_list=["apple","patato","cool"]
l=6
c_word=random.choice(word.words)
print(c_word)
display=[]
for i in range(len(c_word)):
    display += '_'
print(display)
g_over=False
while not g_over:
    g_letter=input("Guess a letter :").lower()
    for pos in range (len(c_word)):
        letter=c_word[pos]
        if letter == g_letter:
            display[pos] = g_letter
    print(display)
    if g_letter not in c_word:
        l-=1
        if l==0:
            g_over=True
            print("You lose !")
    if '_' not in display:
        g_over=True
        print("You win !")
    print(hangman_stages.stages[l])
    

