import random

articles = ["the", "a", "an"]
nouns = ["cat", "dog", "man", "woman"]
prepositions = ["on", "in", "under", "over"]

def nounPhrase():
    """Returns a noun phrase, which is an article followed by a noun, and an optional prepositional phrase."""
    phrase = random.choice(articles) + " " + random.choice(nouns)
    prob = random.randint(1, 4) # 25% probability
    if prob == 1:
        return phrase + " " + prepositionalPhrase()
    else:
        return phrase

def prepositionalPhrase():
    """Builds and returns a prepositional phrase."""
    return random.choice(prepositions) + " " + nounPhrase()

# Gọi hàm và in ra kết quả
print(nounPhrase())
