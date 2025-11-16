class EmotionDrift:
    def __init__(self): self.level=0; self.state='CALM'
    def update_success(self,val=0.1): self.level=max(0,self.level-val)
    def update_failure(self,severity=0.2): self.level+=severity
