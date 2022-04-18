from game import Game
g = Game()
while True:
    guess = input('Make a guess')
    dist = g.make_guess(guess)
    if dist == None:
        print('Not valid language')
        continue
    if dist == 0:
        print('Congratulations!')
        break
    if dist > 1000:
        print('Cold')
    if dist <= 1000:
        print('Hot!')
