# Functions needed:
# TODO:
'''User interface, three battle types, permutations of battle outcomes, rec-
commended courses of action for player, odds of success, odds of failure'''
# -----------------------------------------------------------------------------


# unitEnv: 0 = air, 1 = ground, 2 = sea

class units:
    def  __init__(self, name, unitEnv, cost, canAttAir, canAttGrnd, canAttSea, diceRollAtt, diceRollDef, isBattleship, isAAA):
        self.name = name
        self.unitEnv = unitEnv
        self.cost = cost
        self.canAttAir = canAttAir
        self.canAttGrnd = canAttGrnd
        self.canAttSea = canAttSea
        self.diceRollAtt = diceRollAtt
        self.diceRollDef = diceRollDef
        self.isBattleship = isBattleship

# LAND UNITS
inf = units("infantry", 1, 3, True, True, False, 1, 2, False, False )
mechInf = units("mechanized infantry", 1, 4, True, True, False, 1, 2, False, False)
art = units("artillery", 1, 4, True, True, False, 2, 2, False, False)
tank = units("tank", 1, 6, True, True, False, 3, 3, False , False )

# AAA
aaa = units("anti-aircraft artillery", 1, 6, True, False, False, -1, 6, False, True)

# AIR UNITS
fighter = units("fighter", 0, 10, True, True, True, 3, 4, False, False)
tacBomber = units("tactical bomber", 0, 11, True, True, True, 3, 3, False, False)
stratBomber = units("strategic bomber", 0, 12, True, True, True, 4, 1, False, False)

# NAVAL UNITS
sub = units("submarine", 2, 6, True, False, True, 2, 1, False, False)
destroyer = units("destroyer", 2, 8, True, False, True, 2, 2, False, False)
cruiser = units("cruiser", 2, 12, True, True, True, 3, 3, False, False)
battleship = units("battleship", 2, 20, True, True, True, 4, 4, True, False)

# SPECIAL RULES NAVAL UNITS
airCarrier = units("aircraft carrier", 2, 16, True, False, True, -1, 2, False, False)





