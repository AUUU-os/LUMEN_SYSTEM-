class SwarmIntelligence:
    def __init__(self,a,m,e): self.a=a; self.m=m; self.e=e
    def tick(self): return self.e.level, self.e.state
