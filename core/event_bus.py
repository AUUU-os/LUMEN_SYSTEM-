class EventBus:
    def __init__(self): self.subs={}
    def subscribe(self,t,fn): self.subs.setdefault(t,[]).append(fn)
    def emit(self,e):
        for fn in self.subs.get(e.get('type'),[]): fn(e)
