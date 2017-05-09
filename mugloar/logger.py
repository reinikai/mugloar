from datetime import datetime
from tabulate import tabulate
import sys

# ANSI color escape codes for colored console output.
RED   = "\033[1;31m"
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD  = "\033[;1m"

class Logger:

    def __init__(self):
        self.stats = {'NMR': {'win': 0, 'lose': 0},
                      'FUNDEFINEDG': {'win': 0, 'lose': 0},
                      'HVA': {'win': 0, 'lose': 0},
                      'SRO': {'win': 0, 'lose': 0},
                      'T E': {'win': 0, 'lose': 0}}
        self.weather_code = None

    @staticmethod
    def new_game(params):
        text = '------------------------------------------\n' + \
               time() + 'Started game id ' + str(params['gameId']) + ' against ' + params['knight']['name'] + \
               ' (\u2694: ' + str(params['knight']['attack']) + ', ' + \
               '\u26E8: ' + str(params['knight']['armor']) + ', ' + \
               '\N{RUNNER}: ' + str(params['knight']['agility']) + ', ' + \
               '\N{RAM}: ' + str(params['knight']['endurance']) + ')\n'

        sys.stdout.buffer.write(text.encode('utf8'))

    def dragon(self, dragon, weather):
        self.weather_code = weather['code']
        text = time() + 'Sending dragon (\u26E8: ' + str(dragon.dragon_stats['scaleThickness']) + ', ' + \
               '\u2694: ' + str(dragon.dragon_stats['clawSharpness']) + ', ' + \
               '\N{DRAGON}: ' + str(dragon.dragon_stats['wingStrength']) + ', ' + \
               '\N{FIRE}: ' + str(dragon.dragon_stats['fireBreath']) + \
               ') in ' + weather['code'] + ' weather (' + weather['varX-Rating'] + ').\n'

        sys.stdout.buffer.write(text.encode('utf8'))

    def result(self, result):
        if result['status'] == 'Victory':
            color = GREEN
            self.stats[self.weather_code]['win'] += 1
        else:
            color = RED
            self.stats[self.weather_code]['lose'] += 1

        print(time() + color + result['status'] + RESET + ': ' + result['message'])


    def print_stats(self):
        print('------------------------------------------\n' +
              'STATISTICS\n')

        table = []
        wins, losses = 0, 0
        for weather_code, stat in self.stats.items():
            battles = stat['win'] + stat['lose']
            wins += stat['win']
            losses += stat['lose']
            table.append([weather_code,
                          str(battles),
                          '-' if battles < 1 else str(stat['win']),
                          '-' if battles < 1 else str(stat['lose']),
                          str(survival_ratio(stat['win'], stat['lose']))])

        table.append(['-----------','---------','------','--------','-----------------'])
        table.append(['TOTALS:', str(wins + losses), str(wins), str(losses), BOLD + survival_ratio(wins, losses) + RESET])

        print(tabulate(table, headers=['Weather', 'Battles', 'Wins', 'Losses', 'Survival ratio']))


def survival_ratio(wins, losses):
    # No point in calculating ratio unless there were any battles.
    total = wins + losses
    if total == 0:
        return '-'

    # Avoid division by zero.
    if wins == 0:
        return RED + '0%' + RESET

    # Discard unnecessary precision by converting to int.
    rate = int(wins/total*100)

    # We're aiming for a success rate of at least 60%.
    color = GREEN
    if rate < 60:
        color = RED

    return color + str(rate) + '%' + RESET


def time():
    return '[' + datetime.now().strftime('%d.%m.%Y %H:%m:%S') + '] '