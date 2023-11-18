from .utils import change_values


class Team:
    """A team."""

    name = None

    def __init__(self, name, team_id, league) -> None:
        self.name = name
        self.team_id = team_id
        self.league = league

    