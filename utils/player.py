


class Player:
    """A player."""

    name = None

    def __init__(self, name, player_id, team, league) -> None:
        self.name = name
        self.player_id = player_id
        self.team = team
        self.league = league

    