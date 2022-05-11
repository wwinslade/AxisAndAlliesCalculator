class battleScenario:
    def __init__(self, scenarioName, airUnitEligible, grndUnitEligible, seaUnitEligible, bombardment, subStrike):
        self.scenarioName = scenarioName
        self.airUnitEligible = airUnitEligible
        self.grndUnitEligible = grndUnitEligible
        self.seaUnitEligible = seaUnitEligible
        self.bombardment = bombardment
        self.subStrike = subStrike
        # BATTLE SCENARIO: conventional = 0, amphib = 1, sea = 2

convBattle = battleScenario('conventional battle', True, True, False, False, False)
amphibBattle = battleScenario('amphibious battle', True, True, False, True, False)
seaBattle = battleScenario('naval battle', True, False, True, False, True)