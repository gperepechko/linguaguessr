import pandas as pd
import random
from formula import distance

class Game:
    def __init__(self, debug=False) -> None:
        self.guessed_langs = []
        df = pd.read_csv('Languages.csv')
        self.languages = set(df['ascii_name'])
        self.language = random.sample(self.languages, 1)[0]
        self.langloc = dict()
        for i in range(len(df)):
            row = df.iloc[i]
            self.langloc[row['ascii_name']] = (row['latitude'],row['longitude'])
        self.shortestdist = None
        self.status = 'run'
        if debug:
            print(self.language, self.langloc[self.language])

    def make_guess(self, lang):
        if self.status != 'run':
            return 'Game finished'
        if lang not in self.langloc:
            return None
        if lang == self.language:
            self.guessed_langs.append(lang)
            self.status = 'win'
            return 'Congratulations!'
        x1, y1 = self.langloc[self.language]
        x2, y2 = self.langloc[lang]
        dist = distance(x1, x2, y1, y2)
        if not self.shortestdist:
            self.shortestdist = dist
            if dist < 30:
                return 'Warm'
            else:
                return 'Cold'
        else:
            if dist < self.shortestdist:
                self.shortestdist = dist
                return 'Warmer'
            else:
                return 'Colder'
