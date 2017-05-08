
class Dragon:

    stats_map = {'attack': 'scaleThickness',
                 'armor': 'clawSharpness',
                 'agility': 'wingStrength',
                 'endurance': 'fireBreath'}

    def __init__(self, weather_code, knight):
        if weather_code == 'T E':
            # Draught requires a 'balanced' dragon.
            self.scaleThickness = 5
            self.clawSharpness = 5
            self.wingStrength = 5
            self.fireBreath = 5
        elif weather_code == 'FUNDEFINEDG':
            # Fog means we're unseen, no need to fly.
            self.scaleThickness = 8
            self.clawSharpness = 8
            self.wingStrength = 0
            self.fireBreath = 4
        elif weather_code == 'NMR':
            # Remove name (string) so that sorting of integers works as expected.
            del knight['name']
            knight = sorted(knight.items(), key=lambda x: x[1],
                            reverse=True)

            # This algorithm typically delivers a success ratio of over 80%.
            points_left = 20
            for i, (stat, value) in enumerate(knight):
                points = 0

                if i == 0:
                    points = value + 2 if points_left >= value + 2 else points_left
                    setattr(self, self.stats_map[stat], points)
                elif i == 1:
                    if value < 3:
                        setattr(self, self.stats_map[stat], 0)
                    else:
                        points = value - 2 if points_left >= value - 2 else points_left
                        setattr(self, self.stats_map[stat], points)
                elif i == 2:
                    points = value + 1 if points_left >= value + 1 else points_left
                    setattr(self, self.stats_map[stat], points)
                else:
                    if value < 2:
                        setattr(self, self.stats_map[stat], 0)
                    else:
                        points = value - 1 if points_left >= value - 1 else points_left
                        setattr(self, self.stats_map[stat], points)
                points_left -= points

        elif weather_code == 'SRO':
            # Doesn't really matter what we do here - EVERYONE DIES!
            self.scaleThickness = 20
            self.clawSharpness = 0
            self.wingStrength = 0
            self.fireBreath = 0
        else:
            self.scaleThickness = 5
            # Additional claw-sharpening is needed to destroy the umbrellaboats.
            self.clawSharpness = 10
            self.wingStrength = 5
            # Fire is useless in the rain.
            self.fireBreath = 0

    def get_json(self):
        return {"dragon": {
                    "scaleThickness": self.scaleThickness,
                    "clawSharpness": self.clawSharpness,
                    "wingStrength": self.wingStrength,
                    "fireBreath": self.fireBreath}}
