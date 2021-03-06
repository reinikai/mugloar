from typing import Dict, Generator

# Match knight's stats with dragon's stats.
STATS_MAP = {'attack': 'scaleThickness',
             'armor': 'clawSharpness',
             'agility': 'wingStrength',
             'endurance': 'fireBreath'}

# Total number of points that can be divided amongst a dragon's stats.
POINTS_AVAILABLE: int = 20

# Maximum number of points that can be given to a single stat.
# Otherwise, "Dragon died of performance enhancement drug overdose"
MAX_PER_STAT: int = 10

# The API does not allow one to assign negative points to a stat.
# Otherwise: "Dragon developed anorexia and went chasing after a career as a runway model"
MIN_PER_STAT: int = 0


class Dragon:

    def __init__(self):
        """ Initializes instance variables. """
        self.dragon_stats: Dict[str, int] = {}
        self.stays_home = False

    def set_relative_stats(self, dragon_stats: tuple, knight: dict) -> None:
        """ Sets the dragon's stats relative to the knight's corresponding stats. """

        points_left = POINTS_AVAILABLE

        for i, (stat, value) in enumerate(knight):
            relative_points = value + dragon_stats[i]

            if relative_points < MIN_PER_STAT:
                points = MIN_PER_STAT
            elif points_left >= relative_points:
                points = relative_points
            else:
                points = points_left

            self.dragon_stats[STATS_MAP[stat]] = points
            points_left -= points

        self.stays_home = False

    def set_stats(self, scale_thickness: int, claw_sharpness: int, wing_strength: int, fire_breath: int) -> None:
        """ A shorthand method for setting all of the dragon's stats in one go. """

        if max(scale_thickness, claw_sharpness, wing_strength, fire_breath) > MAX_PER_STAT:
            raise ValueError("Max " + str(MAX_PER_STAT) + " points/stat allowed.")

        self.dragon_stats = {'scaleThickness': scale_thickness,
                             'clawSharpness': claw_sharpness,
                             'wingStrength': wing_strength,
                             'fireBreath': fire_breath}
        self.stays_home = False

    def set_dragon_stays_home(self):
        self.stays_home = True


    def get_json(self) -> dict:
        """ Returns dragon's stats in a format that corresponds to the API's expected JSON format. """
        if self.stays_home:
            return {}
        return {"dragon": self.dragon_stats}
