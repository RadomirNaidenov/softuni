from project.player import Player
# from player import Player


class Guild:

    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player: Player) -> str:
        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."

        if player.guild != player.DEFAULT_GUILD:
            return f"Player {player.name} is in another guild."

        self.players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str) -> str:
        for player in self.players:
            if player.name == player_name:
                player.guild = "Unaffiliated"
                self.players.remove(player)

                return f"Player {player_name} has been removed from the guild."

        return f"Player {player_name} is not in the guild."

    def guild_info(self) -> str:
        output = [f"Guild: {self.name}"]

        [output.append(p.player_info()) for p in self.players]

        return "\n".join(output)


