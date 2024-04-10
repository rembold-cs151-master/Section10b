
"""
Creating a LLM and predictive text generator.
"""

import random

macbeth = """
          Tomorrow, and tomorrow, and tomorrow
          Creeps in this petty pace from day to day
          To the last syllable of recorded time;
          """


def create_model(text):
   """Creates a dictionary model of each subsequent word in the text.

   Returns a dictionary with words as keys and a corresponding list of
   words as values, where the words in the list are each words that came 
   after the key.
   """





def generate_text(model, start, max_words=100):
   """Predicts a string of text based on the provided model and starting word.

   Returns a string of words separated by spaces, which do not exceed the
   max number of words.
   """







if __name__ == '__main__':
   model = create_model(macbeth)
   print(model)
   #print(generate_text(model, 'tomorrow'))
