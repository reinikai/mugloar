# Match knight's stats with dragon's stats.
STATS_MAP = {'attack': 'scaleThickness',
              'armor': 'clawSharpness',
              'agility': 'wingStrength',
              'endurance': 'fireBreath'}

# Total number of points that can be divided amongst a dragon's stats.
POINTS_AVAILABLE = 20

# Maximum number of points that can be given to a single stat.
# Otherwise, "Dragon died of performance enhancement drug overdose"
MAX_PER_STAT = 10

# The API does not allow one to assign negative points to a stat.
# Otherwise: "Dragon developed anorexia and went chasing after a career as a runway model"
MIN_PER_STAT = 0


class Dragon:

    def __init__(self):
        """ Initializes instance variables """
        self.dragon_stats = {}


    def set_relative_stats(self, dragon_stats, knight):
        """ Sets the dragon's stats relative to the knight's corresponding stats """

        points_left = POINTS_AVAILABLE

        for i, (stat, value) in enumerate(knight):
            relative_points = value + dragon_stats[i]

            if relative_points < 0:
                points = 0
            elif points_left >= relative_points:
                points = relative_points
            else:
                points = points_left

            self.dragon_stats[STATS_MAP[stat]] = points
            points_left -= points

    def set_stats(self, scale_thickness, claw_sharpness, wing_strength, fire_breath):
        """ A shorthand method for setting all of the dragon's stats in one go """

        if max(scale_thickness, claw_sharpness, wing_strength, fire_breath) > MAX_PER_STAT:
            raise ValueError("Max " + MAX_PER_STAT + " points/stat allowed.")

        self.dragon_stats = {'scaleThickness': scale_thickness,
                             'clawSharpness': claw_sharpness,
                             'wingStrength': wing_strength,
                             'fireBreath': fire_breath}

    def get_json(self):
        """ Returns a dict that corresponds to the API's expected JSON format """
        return {"dragon": self.dragon_stats }


def possible_solutions():
    """ Generate all possible distributions of available points """
    return partition(POINTS_AVAILABLE, len(STATS_MAP), MIN_PER_STAT, MAX_PER_STAT)

def partition(integer, partition_length, min_size, max_size):
    """ Invoke positive integer partitioning with minimum and maximum element limits """
    if partition_length < 1 or integer < 0:
        return

    if partition_length == 1:
        if integer <= max_size >= min_size:
            yield (integer,)
        return
    for i in range(min_size, max_size + 1):
        for result in partition(integer - i, partition_length - 1, i, max_size):
            yield result+(i,)
