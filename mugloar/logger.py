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
                          str(survival_rate(stat['win'], stat['lose']))])

        table.append(['-----------','---------','------','--------','---------------'])
        table.append(['TOTALS:', str(wins + losses), str(wins), str(losses), BOLD + survival_rate(wins, losses) + RESET])

        print(tabulate(table, headers=['Weather', 'Battles', 'Wins', 'Losses', 'Survival rate']))


def survival_rate(wins, losses):
    total = wins + losses
    if total == 0:
        return '-'

    if wins == 0:
        return RED + '0%' + RESET

    rate = wins/total*100

    color = GREEN
    if rate < 60:
        color = RED

    return color + '{0:g}'.format(rate) + '%' + RESET


def time():
    return '[' + datetime.now().strftime('%d.%m.%Y %H:%m:%S') + '] '