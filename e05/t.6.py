import random 
class WordGame():       
    def __init__(self, rounds: int): 
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds        
    
    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner 
        return random.randint(1, 2)        
        
    
    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")
            
            if self.round_winner(answer1, answer2) == 1: 
                self.wins1 += 1 
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2: 
                self.wins2 += 1 
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:") 
        print(f"player 1: {self.wins1}") 
        print(f"player 2: {self.wins2}")

class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        if len(player1_word) > len(player2_word):
            return 1
        elif len(player2_word) > len(player1_word):
            return 2
        else:
            return 0
        
class MostVowels(WordGame):
    def __init__(self, rounds: int):
        WordGame.__init__(self, rounds)
    
    def count_vowels(self, word: str):
        vowels = "aeiouAEIOU"
        return sum(1 for char in word if char in vowels)

    def round_winner(self, player1_word: str, player2_word: str):
        vowels1 = self.count_vowels(player1_word)
        vowels2 = self.count_vowels(player2_word)

        if vowels1 > vowels2:
            return 1
        elif vowels2 > vowels1:
            return 2
        else:
            return 0

class RPSLS(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)
    
    def round_winner(self, player1_word: str, player2_word: str):
        rules = {
            "scissors": ["paper", "lizard"],
            "paper": ["rock", "spock"],
            "rock": ["scissors", "lizard"],
            "lizard": ["spock", "paper"],
            "spock": ["scissors", "rock"]
        }
        
        if player1_word == player2_word:
            return 0 
        elif player2_word in rules.get(player1_word, []):
            return 1
        elif player1_word in rules.get(player2_word, []):
            return 2
        else:
            return 0 
p = WordGame(3)
p = RPSLS(3)
p.play()