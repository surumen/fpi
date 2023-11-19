

class League:

    def __init__(self, league_id: int, league_name: str):
        self.league_id = league_id
        self.league_name = league_name
        self.slug = league_name.lower().replace(' ', '_')

