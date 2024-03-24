from flask import Flask, render_template, request

from game_of_life import GameOfLife

app = Flask(__name__)



@app.route('/')
def index():
    GameOfLife(width=10, height=10)

    return render_template('index.html')


@app.route('/live')
def live():
    game = GameOfLife()
    if game.counter > 0:
        game.form_new_generation()
        print(game.__dict__)
        print(game.counter)

    game.next_count()
    print()
    return render_template('live.html', game=game)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
