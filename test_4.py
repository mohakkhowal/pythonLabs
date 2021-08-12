'''Write a python function exclamation() that takes input as a string and returns it with this modification:
Every vowel is replaced by four consecutive copies of itself and an exclamation mark (!) is added at the
end.
>>> exclamation('argh')
'aaaargh!'
>>> exclamation('hello')
'heeeelloooo!'
'''

def exclamation(word):
    for x in 'aeiouAEIOU':
        word = word.replace(x,x*4)
    return word+'!'

print(exclamation('argh'))
print(exclamation('hello'))
