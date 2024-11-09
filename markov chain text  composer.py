import random
from collections import defaultdict

class MarkovChainTextComposer:
    def __init__(self):
        self.model = defaultdict(list)
    
    def build_model(self, text, k=1):
        """Builds the Markov chain model with order `k` from the given text."""
        words = text.split()
        for i in range(len(words) - k):
            prefix = tuple(words[i:i+k])
            suffix = words[i+k]
            self.model[prefix].append(suffix)
    
    def generate_text(self, length=50, k=1):
        """Generates text of the given length using the Markov chain model."""
        start_index = random.randint(0, len(self.model) - 1)
        prefix = list(self.model.keys())[start_index]
        generated = list(prefix)
        
        for _ in range(length - k):
            suffixes = self.model[tuple(prefix)]
            if not suffixes:
                break
            next_word = random.choice(suffixes)
            generated.append(next_word)
            prefix = generated[-k:]
        
        return ' '.join(generated)

def main():
    print("Welcome to the Markov Chain Text Composer!")
    
    input_text = input("Please enter the input text to build the model: ")
    order = int(input("Please enter the order of the Markov chain (e.g., 1 for unigram, 2 for bigram): "))
    length = int(input("Please enter the length of the generated text: "))
    
    composer = MarkovChainTextComposer()
    composer.build_model(input_text, order)
    
    print("\nGenerated Text:")
    print(composer.generate_text(length, order))

if __name__ == "__main__":
    main()
