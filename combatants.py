class attackers:
    def __init__(self, nInf, nMechInf, nArt, nTank, nFighter, nTactB, nStratB, nSub, nDestroyer, nCruiser, nBattleship, nAircraftCarrier):
        self.nInf = nInf
        self.nMechInf = nMechInf
        self.nArt = nArt
        self.nTank = nTank
        self.nFighter = nFighter
        self.nTactB = nTactB
        self.nStratB = nStratB
        self.nSub = nSub
        self.nDestroyer = nDestroyer
        self.nCruiser = nCruiser
        self.nBattleship = nBattleship
        self.nAircraftCarrier = nAircraftCarrier

    def totalUnits(self):
        totalUnits = self.nInf + self.nMechInf + self.nArt + self.nTank + self.nFighter + self.nTactB + self.nStratB + self.nSub + self.nDestroyer + self.nCruiser + self.nBattleship + self.nAircraftCarrier
        return totalUnits
        
        
class defenders:
    def __init__(self, nInf, nMechInf, nArt, nTank, nAAA, nFighter, nTactB, nStratB, nSub, nDestroyer, nCruiser, nBattleship, nAircraftCarrier, nTransport):
        self.nInf = nInf
        self.nMechInf = nMechInf
        self.nArt = nArt
        self.nTank = nTank
        self.nFighter = nFighter
        self.nTactB = nTactB
        self.nStratB = nStratB
        self.nSub = nSub
        self.nDestroyer = nDestroyer
        self.nCruiser = nCruiser
        self.nBattleship = nBattleship
        self.nAircraftCarrier = nAircraftCarrier
        
        self.nAAA = nAAA
        self.nTransport = nTransport

    def totalUnits(self):
        totalUnits = self.nInf + self.nMechInf + self.nArt + self.nTank + self.nFighter + self.nTactB + self.nStratB + self.nSub + self.nDestroyer + self.nCruiser + self.nBattleship + self.nAircraftCarrier + self.nAAA + self.nTransport
        return totalUnits