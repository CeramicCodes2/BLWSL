from pydantic import BaseModel,BaseSettings
from .Merger import save_settings
from . import PATH_SEQUENCES
class Sequence(BaseModel):
    value:int
    @property
    def nextValue(self) -> int:
        self.value += 1
        return self.value
    @property
    def currentValue(self) -> int:
        return self.value
class SequenceMerger(BaseModel):
    path:str = PATH_SEQUENCES
    sequences:dict[str,Sequence]
    name:str = "SEQUENCES"
    def saveSequence(self) -> None:
        save_settings(self,format='json',exclude={'name','path'})
        