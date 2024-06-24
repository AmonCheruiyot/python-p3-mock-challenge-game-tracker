class Game:
    def __init__(self, title):
        if not isinstance(title, str):
            raise TypeError("Title must be a string")
        if len(title) == 0:
            raise ValueError("Title must be longer than 0 characters")
        self._title = title
        self._results = []

    @property
    def title(self):
        return self._title

    def results(self):
        return self._results

    def players(self):
        return list(set(result.player for result in self._results))

    def average_score(self, player):
        player_scores = [result.score for result in self._results if result.player == player]
        return sum(player_scores) / len(player_scores) if player_scores else 0

class Player:
    def __init__(self, username):
        if not isinstance(username, str):
            raise TypeError("Username must be a string")
        if not 2 <= len(username) <= 16:
            raise ValueError("Username must be between 2 and 16 characters, inclusive")
        self._username = username
        self._results = []

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if not isinstance(value, str):
            raise TypeError("Username must be a string")
        if not 2 <= len(value) <= 16:
            raise ValueError("Username must be between 2 and 16 characters, inclusive")
        self._username = value

    def results(self):
        return self._results

    def games_played(self):
        return list(set(result.game for result in self._results))

    def played_game(self, game):
        return any(result.game == game for result in self._results)

    def num_times_played(self, game):
        return sum(1 for result in self._results if result.game == game)

    @classmethod
    def highest_scored(cls, game):
        players = game.players()
        if not players:
            return None
        highest_player = max(players, key=lambda player: game.average_score(player))
        return highest_player

class Result:
    all = []
    def __init__(self, player, game, score):
        if not isinstance(score, int):
            raise TypeError("Score must be an integer")
        if score < 1 or score > 5000:
            raise ValueError("Score must be between 1 and 5000, inclusive")
        self._player = player
        self._game = game
        self._score = score
        player.results().append(self)
        game.results().append(self)
        Result.all.append(self)
        

    @property
    def player(self):
        return self._player

    @property
    def game(self):
        return self._game

    @property
    def score(self):
        return self._score
