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

    def __init__(self, weather_code, knight):
        self.dragon_stats = {}

        if weather_code == 'T E':
            # Draught requires a 'balanced' dragon.
            self.set_stats(5, 5, 5, 5)
        elif weather_code == 'FUNDEFINEDG':
            # Fog means we're unseen, no need to fly.
            self.set_stats(8, 8, 0, 4)
        elif weather_code == 'NMR':
            # Remove name (string) so that sorting of integers works as expected.
            del knight['name']

            # Sort opponent's stats from high to low so that we can match points.
            knight = sorted(knight.items(), key=lambda x: x[1], reverse=True)

            # This algorithm typically delivers a success ratio of over 80%.
            points_left = POINTS_AVAILABLE
            for i, (stat, value) in enumerate(knight):
                points = 0

                if i == 0:
                    points = value + 2 if points_left >= value + 2 else points_left
                    self.dragon_stats[STATS_MAP[stat]] = points
                elif i == 1:
                    if value < 3:
                        self.dragon_stats[STATS_MAP[stat]] = 0
                    else:
                        points = value - 2 if points_left >= value - 2 else points_left
                        self.dragon_stats[STATS_MAP[stat]] = points
                elif i == 2:
                    points = value + 1 if points_left >= value + 1 else points_left
                    self.dragon_stats[STATS_MAP[stat]] = points
                else:
                    if value < 2:
                        self.dragon_stats[STATS_MAP[stat]] = 0
                    else:
                        points = value - 1 if points_left >= value - 1 else points_left
                        self.dragon_stats[STATS_MAP[stat]] = points
                points_left -= points

        elif weather_code == 'SRO':
            # Doesn't really matter what we do here - EVERYONE DIES!
            self.set_stats(10, 10, 0, 0)
        else:
            # Additional claw-sharpening is needed to destroy the umbrellaboats.
            # Fire is useless in the rain.
            self.set_stats(5, 10, 5, 0)

    def set_stats(self, scale_thickness, claw_sharpness, wing_strength, fire_breath):
        self.dragon_stats = {'scaleThickness': scale_thickness,
                             'clawSharpness': claw_sharpness,
                             'wingStrength': wing_strength,
                             'fireBreath': fire_breath}

    def get_json(self):
        return {"dragon": self.dragon_stats }


def possible_solutions():
    """ Generate all possible distributions of available points. """
    return partition(POINTS_AVAILABLE, len(STATS_MAP), MIN_PER_STAT, MAX_PER_STAT)

def partition(integer, partition_length, min_size, max_size):
    """ Invoke positive integer partitioning with minimum and maximum element limits. """
    if partition_length < 1 or integer < 0:
        return

    if partition_length == 1:
        if integer <= max_size >= min_size:
            yield (integer,)
        return
    for i in range(min_size, max_size + 1):
        for result in partition(integer - i, partition_length - 1, i, max_size):
            yield result+(i,)
