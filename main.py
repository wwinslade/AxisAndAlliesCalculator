import units
import numpy as np
 
import units
import battleScenarios as bs
import combatants as cb
import hitProbability as hP

# DATA INPUT
o = cb.attackers(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
d = cb.defenders(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)

battleTypeIn = 'naval'

nSimulations = 100

# PROCESSING

# Sets battle type to use based on user-defined var
if battleTypeIn == 'conventional':
    battleType = bs.convBattle
elif battleTypeIn == 'amphibious':
    battleType = bs.amphibBattle
elif battleTypeIn == 'naval':
    battleType = bs.seaBattle
    
attTot = o.totalUnits()
defTot = d.totalUnits()


# Beginning Hit Probability Simulations
infHits = hP.hitSimAttack('inf', o.nInf)



        
            

            
            
    

