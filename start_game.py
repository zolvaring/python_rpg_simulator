#!/usr/bin/env python3


from core.Game import Game


if __name__ == '__main__':
  Game.flask.app.run(host='0.0.0.0', debug=True)
