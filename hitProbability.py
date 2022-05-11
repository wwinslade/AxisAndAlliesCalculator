# HIT LOGIC MODULE

import units as u
import numpy as np

def hitSimAttack(unitType, nUnit):
    
    unit = getattr(u, unitType)
    hits = 0
    
    for i in range(nUnit):
        diceRoll = np.random.randint(1, 7)
        if diceRoll <= unit.diceRollAtt:
            hits += 1
    
    return hits


def hitSimDefense(unitType, nUnit):
    
    unit = getattr(u, unitType)
    hits = 0
    
    for i in range(nUnit):
        diceRoll = np.random.randint(1, 7)
        if diceRoll <= unit.diceRollAtt:
            hits += 1
    
    return hits