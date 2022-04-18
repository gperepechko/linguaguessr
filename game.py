import pandas as pd
import random
class Game:
    def __init__(self) -> None:
        self.guessed_langs = []
        df = pd.read_csv('Languages.csv')
        self.languages = set(df['ascii_name'])
        self.language = random.sample(self.languages, 1)[0]
        self.langloc = dict()
        for i in range(len(df)):
            row = df.iloc[i]
            self.langloc[row['ascii_name']] = (row['latitude'],row['longitude'])
        # print(self.langloc)

    def make_guess(self, lang):
        if lang not in self.langloc:
            return None
        return 1000
