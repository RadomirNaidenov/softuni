class Player:
    DEFAULT_GUILD = "Unaffiliated"

    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills: dict[str: int] = {}
        self.guild = Player.DEFAULT_GUILD

    def add_skill(self, skill_name, mana_cost) -> str or None:
        if skill_name in self.skills:
            return "Skill already added"

        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self) -> str:
        info_output = [f"Name: {self.name}",
                       f"Guild: {self.guild}",
                       f"HP: {self.hp}",
                       f"MP: {self.mp}"]

        [info_output.append(f"==={skill} - {mana}") for skill, mana in self.skills.items()]

        return "\n".join(info_output)




