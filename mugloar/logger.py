from datetime import datetime
from tabulate import tabulate
import sys

RED   = "\033[1;31m"
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD  = "\033[;1m"

class Logger:

    stats = {'NMR': {'win': 0, 'lose': 0},
             'FUNDEFINEDG': {'win': 0, 'lose': 0},
             'HVA': {'win': 0, 'lose': 0},
             'SRO': {'win': 0, 'lose': 0},
             'T E': {'win': 0, 'lose': 0}}

    weather_code = ""

    def new_game(self, params):
        text = '------------------------------------------\n' + \
               time() + 'Started game id ' + str(params['gameId']) + ' against ' + params['knight']['name'] + \
               ' (\u2694: ' + str(params['knight']['attack']) + ', ' + \
               '\u26E8: ' + str(params['knight']['armor']) + ', ' + \
               '\N{RUNNER}: ' + str(params['knight']['agility']) + ', ' + \
               '\N{RAM}: ' + str(params['knight']['endurance']) + ')\n'

        sys.stdout.buffer.write(text.encode('utf8'))

    def dragon(self, dragon, weather):
        self.weather_code = weather['code']
        text = time() + 'Sending dragon (\u26E8: ' + str(dragon.scaleThickness) + ', ' + \
               '\u2694: ' + str(dragon.clawSharpness) + ', ' + \
               '\N{DRAGON}: ' + str(dragon.wingStrength) + ', ' + \
               '\N{FIRE}: ' + str(dragon.fireBreath) + \
               ') in ' + weather['code'] + ' weather.\n'

        sys.stdout.buffer.write(text.encode('utf8'))

    def result(self, result):
        print(time(), end='')

        if result['status'] == 'Victory':
            sys.stdout.write(GREEN)
            self.stats[self.weather_code]['win'] += 1
        else:
            sys.stdout.write(RED)
            self.stats[self.weather_code]['lose'] += 1

        print(result['status'], end='')
        sys.stdout.write(RESET)
        print(': ' + result['message'])


    def print_stats(self):
        print('------------------------------------------\n' +
              'STATISTICS\n' +
              'Iterations: ' + '\n\n' +
              'By weather type:')

        table = []
        for weather_code, stat in self.stats.items():
            table.append([weather_code, str(stat['win'] + stat['lose']), str(stat['win']), str(stat['lose']), str(survival_rate(stat['win'], stat['lose']))])

        print(tabulate(table, headers=['Weather', 'Battles', 'Wins', 'Losses', 'Survival rate']))

        print('\n\nOVERALL SUCCESS RATE: ', end='')
        success_rate = 0
        if success_rate < 60:
            sys.stdout.write(RED)
        else:
            sys.stdout.write(GREEN)
        print(str(success_rate) + '%')

def survival_rate(wins, losses):
    total = wins + losses
    if total == 0:
        return '-'

    if wins == 0:
        return '0%'

    rate = wins/total
    return '{0:g}'.format(rate*100) + '%'


def time():
    return '[' + datetime.now().strftime('%d.%m.%Y %H:%m:%S') + '] '