from random import choice

class QuotePicker(object):

    def __init__(self, quotes_filename):
        """Initialize the QuotePicker class"""
        with open(quotes_filename) as quotes_file:
            self.quotes = quotes_file.readlines()

    def pick(self):
        """returns a random quote"""
        return choice(self.quotes).strip()