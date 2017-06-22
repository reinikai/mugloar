# mugloar
[![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://opensource.org/licenses/MIT)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/3bc92fb26a2541d4b905d775f5a0144c)](https://www.codacy.com/app/reinikai/mugloar?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=reinikai/mugloar&amp;utm_campaign=Badge_Grade)

A solution for [Dragons of Mugloar](https://www.dragonsofmugloar.com/) in Python. The code uses type hinting ([PEP-484](https://www.python.org/dev/peps/pep-0484/)) so one would need at least Python version 3.6.0 to be able to run it out of the box.

## Quickstart

There is a Makefile for convenience. It relies on [vex](https://github.com/sashahart/vex), but you can use any virtualenv you like. After cloning:

```
$ make init
$ make deps
$ vex mugloar
$ mugloar/mugloar.py
```

Sample output:

```
[...]
[22.06.2017 16:17:12] Started game id 4687134 against Sir. Leo Warren of Prince Edward Island (⚔: 0, ⛨: 7, 🏃: 7, 🐏: 6)
[22.06.2017 16:17:12] Weather for battle is NMR (8).
[22.06.2017 16:17:12] Sending dragon number 1 (⛨: 0, ⚔: 9, 🐉: 7, 🔥: 4).
[22.06.2017 16:17:12] Victory: Dragon was successful in a glorious battle
[22.06.2017 16:17:12] Stat diff (knight/dragon): 
armor/clawSharpness: 7/9, difference 2
agility/wingStrength: 7/7, difference 0
endurance/fireBreath: 6/4, difference -2
attack/scaleThickness: 0/0, difference 0
------------------------------------------
[22.06.2017 16:17:12] Started game id 525651 against Sir. Lawrence Patrick of Alberta (⚔: 2, ⛨: 7, 🏃: 8, 🐏: 3)
[22.06.2017 16:17:13] Weather for battle is HVA (12).
[22.06.2017 16:17:13] Sending dragon number 1 (⛨: 5, ⚔: 10, 🐉: 5, 🔥: 0).
[22.06.2017 16:17:13] Victory: Dragon scratched up the umbrella boat and knight drowned.
[22.06.2017 16:17:13] Stat diff (knight/dragon): 
agility/wingStrength: 8/5, difference -3
armor/clawSharpness: 7/10, difference 3
endurance/fireBreath: 3/0, difference -3
attack/scaleThickness: 2/5, difference 3
------------------------------------------
[22.06.2017 16:17:13] Started game id 5423287 against Sir. Curtis Greene of Nova Scotia (⚔: 3, ⛨: 5, 🏃: 6, 🐏: 6)
[22.06.2017 16:17:13] Weather for battle is NMR (8).
[22.06.2017 16:17:13] Sending dragon number 1 (⛨: 2, ⚔: 4, 🐉: 8, 🔥: 6).
[22.06.2017 16:17:13] Victory: Dragon was successful in a glorious battle
[22.06.2017 16:17:13] Stat diff (knight/dragon): 
agility/wingStrength: 6/8, difference 2
endurance/fireBreath: 6/6, difference 0
armor/clawSharpness: 5/4, difference -1
attack/scaleThickness: 3/2, difference -1
------------------------------------------
BATTLE STATISTICS

Weather      Battles    Wins    Losses    Success ratio
-----------  ---------  ------  --------  -----------------
FUNDEFINEDG  1          1       0         100%
HVA          3          3       0         100%
NMR          23         23      0         100%
SRO          3          0       3         0%
T E          0          -       -         -
-----------  ---------  ------  --------  -----------------
TOTALS:      30         27      3         90%
```