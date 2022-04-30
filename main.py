from game import Game
g = Game(debug=True)
while True:
    guess = input('Make a guess\n')
    if guess == '':
        print('Game has stopped')
        break
    status = g.make_guess(guess)
    if not status:
        print('This language does not exist')
        continue
    print(status)
    