#2.1
ensemble_phrase = set("Je suis un as en programmation.")
ensemble_chiffre = {n for n in range(1001) if n%3 == 0 and n%13 == 0}
ensemble_voyelle = {l for l in "Maitriser les listes est crucial!" if l in "aeiou"}
        

#2.2
def set2list(A : set):
    res = []
    for char in A:
        res.append(char)
    
    return res


#2.3
def common(A: set, B: set) -> int:
    
    nb1 = 0
    for elem in A:
        if elem in B:
            nb += 1
            
    nb2 = len(A & B)
    
    return nb, nb2


#2.4
def xor(A: set, B: set) -> set:
    return A ^ B


#2.5
dictio_pairs = {n : n-1 for n in range(2, 21, 2)}
dictio_impairs = {2 * n + 1 : (2 * n + 1) % 3 == 0 for n in range(1,11)}
dictio_fruit = {mot : sum(1 for lettre in mot if lettre in 'aeiou') for mot in ['lemon','apple','banana','watermelon']}


#2.6
def hasKey_for(key : hash, dico: dict) -> bool:
    for k in dico:
        if k == key:
            return True
    return False

def hasKey_in(key : hash, dico: dict) -> bool:
    return key in dico


#3
def computeFreq(votes: list[str]) -> dict[str, int]:
    freq = {}
    for vote in votes:
        if vote in freq:
            freq[vote] += 1
        else:
            freq[vote] = 1
    return freq

def maxFreq(frequencies: dict[str, int]) -> str:
    return max(frequencies, key=frequencies.get)

votes = [
  "tomate",
  "cerfeuil",
  "tomate",
  "potiron",
  "tomate",
  "cerfeuil",
  "poulet"
]
frequencies = computeFreq(votes)
soup = maxFreq(frequencies)
print(f"La soupe la plus populaire est {soup} avec {frequencies[soup]} votes.")

