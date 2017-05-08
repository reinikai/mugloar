
class Dragon:

    # By default, stay home.
    scaleThickness = 0
    clawSharpness = 0
    wingStrength = 0
    fireBreath = 0

    def __init__(self, weather_code):
        if weather_code == 'T E':
            # Draught requires a 'balanced' dragon, ha ha
            self.scaleThickness = 5
            self.clawSharpness = 5
            self.wingStrength = 5
            self.fireBreath = 5
        elif weather_code == 'FUNDEFINEDG':
            # Fog means we're unseen, no need to fly
            self.scaleThickness = 8
            self.clawSharpness = 8
            self.wingStrength = 0
            self.fireBreath = 4
        elif weather_code == 'NMR':
            self.scaleThickness = 3
            self.clawSharpness = 6
            self.wingStrength = 5
            self.fireBreath = 6
        elif weather_code == 'SRO':
            # Stay at home if there's a storm.
            pass
        else:
            # Fire is useless in the rain. Additional claw-sharpening is needed to destroy the umbrellaboats
            self.scaleThickness = 5
            self.clawSharpness = 10
            self.wingStrength = 5
            self.fireBreath = 0

    def get_json(self):
        return {"dragon": {
                    "scaleThickness": self.scaleThickness,
                    "clawSharpness": self.clawSharpness,
                    "wingStrength": self.wingStrength,
                    "fireBreath": self.fireBreath}}
