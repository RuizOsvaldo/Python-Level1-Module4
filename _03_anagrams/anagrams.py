"""
Create an anagram game!
"""
import random
import tkinter as tk

# TODO Use this dictionary of anagrams to create an anagrams GUI word game.
#  Look at 'anagrams_game_example.png' in this folder for an example.
word_anagrams = {
    "action": ["cation"],
    "agree": ["eager"],
    "calm": ["clam"],
    "charming": ["marching"],
    "clean": ["lance"],
    "cool": ["loco"],
    "creative": ["reactive"],
    "delight": ["lighted"],
    "earnest": ["eastern", "nearest"],
    "easy": ["ayes", "yeas"],
    "free": ["reef"],
    "great": ["grate"],
    "green": ["genre"],
    "grin": ["ring"],
    "hearty": ["earthy"],
    "idea": ["aide"],
    "ideal": ["ailed"],
    "keen": ["knee"],
    "lively": ["evilly", "vilely"],
    "lovely": ["volley"],
    "merit": ["miter", "remit", "timer"],
    "open": ["nope", "peon", "pone"],
    "prepared": ["dapperer"],
    "quiet": ["quite"],
    "refined": ["definer"],
    "restored": ["resorted", "rostered"],
    "reward": ["drawer", "redraw", "warder", "warred"],
    "rewarding": ["redrawing", "wardering"],
    "right": ["girth"],
    "secure": ["rescue"],
    "simple": ["impels"],
    "smile": ["limes", "miles", "slime"],
    "super": ["puers", "purse"],
    "tops": ["opts", "post", "pots", "spot", "stop"],
    "unreal": ["neural"],
    "wonderful": ["underflow"],
    "zeal": ["laze"]}


class Anagram(tk.Tk):

    def __init__(self):
        super().__init__()

        '''
        Variables
        '''
        self.word_to_guess = random.choice(list(word_anagrams.keys()))
        self.num_of_anagrams = len(word_anagrams[self.word_to_guess])
        self.guess_remaining = 5
        self.anagram_solutions = word_anagrams[self.word_to_guess]
        self.words_used = list()
        self.words_used.append(self.word_to_guess)

        '''
        GUI Components that will placed in a grid.
        '''
        self.word_label = tk.Label(self, text=f"Guess the {self.num_of_anagrams} anagram for the word: {self.word_to_guess}")
        self.word_label.grid(row=0, column=0)

        self.new_word_button = tk.Button(self, text="Get New Word")
        self.new_word_button.grid(row=0, column=1)
        self.new_word_button.bind('<ButtonPress>', self.get_new_word)

        self.guess_label = tk.Label(self, text=f"Guesses remaining {self.guess_remaining}")
        self.guess_label.grid(row=1, column=0)

        self.entry = tk.Entry(self, width=10)
        self.entry.grid(row=1, column=1)

        self.solution_button = tk.Button(self, text='Check Answer')
        self.solution_button.grid(row=2, column=0)
        self.solution_button.bind('<ButtonPress>', self.check_answer)

        self.solution_label = tk.Label(self, text='')
        self.solution_label.grid(row=2, column=1)

    '''
    Function to get new word when button is clicked
    '''
    def get_new_word(self, event):
        if self.new_word_button == event.widget:
            self.word_to_guess = random.choice(list(word_anagrams.keys()))
            if self.word_to_guess in self.words_used:
                self.word_to_guess = random.choice(list(word_anagrams.keys()))
            
            self.num_of_anagrams = len(word_anagrams[self.word_to_guess])
            self.guess_remaining = 5
            self.anagram_solutions = word_anagrams[self.word_to_guess]
            self.words_used = list()
            self.words_used.append(self.word_to_guess)

            self.word_label.config(text=f"Guess the {self.num_of_anagrams} anagram for the word: {self.word_to_guess}")
            self.guess_label.config(text=f"Guesses remaining {self.guess_remaining}")
            self.entry.delete(0, tk.END)
            self.solution_label.config(text='')

    '''
    Function to check if the answer is correct
    '''
    def check_answer(self, event):
        if self.solution_button == event.widget:
            answer = self.entry.get()
            if answer in self.anagram_solutions:
                self.solution_label.config(text="Correct!")
                self.num_of_anagrams-=1
                if self.num_of_anagrams > 0:
                    self.word_label.config(text=f"Guess the {self.num_of_anagrams} anagram for the word: {self.word_to_guess}")
                else:
                    self.word_label.config(text="No more anagrams.")
            else:
                if self.guess_remaining > 0:
                    self.guess_remaining-=1
                    self.guess_label.config(text=f"Guesses remaining {self.guess_remaining}")
                else:
                    self.solution_label.config(text="Game over.")

if __name__ == '__main__':
    app = Anagram()
    app.mainloop()




        
