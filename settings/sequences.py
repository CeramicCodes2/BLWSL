from pydantic import BaseModel,BaseSettings

class Sequence(BaseModel):
    value:int
    def __add__(self,other:int):
        self.value += other
        return self.value
class sequenceSettings(BaseSettings):
    value:Sequence
    class Config:
        env_prefix = 'sequence_'
        env_file = 'sequences.env'