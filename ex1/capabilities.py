from abc import ABC, abstractmethod
from ex1 import CreatureFactory
from ex0.creatures import Creature


class HealCapability(ABC):
    @abstractmethod
    def heal(self, target: str) -> str:
        pass

class TransformCapability(ABC):
    def __init__(self) -> None:
        self.impact = 0

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass


class HealingCreatureFactory(CreatureFactory):

    class Sproutling(Creature, HealCapability):
        def heal(self, target: str) -> str:
            return f"Sproutling heals {target} for a small amount"


    class Bloomelle(Creature, HealCapability):
        def heal(self, target: str) -> str:
            return f"Bloomelle heals {target} and others for a large amount"


class TransformCreatureFactory(CreatureFactory):

    class Shiftling(Creature, TransformCapability):
        def transform(self) -> str:
            return "Shiftling shift into a sharper form"

        def revert(self) -> str:
            return "Shiftling returns to normal"


    class Morphagon(Creature, TransformCapability):
        def transform(self) -> str:
            return "Morphagon morphs into a dragonic battle form!"

        def revert(self) -> str:
            return "Morphagon stabilizes its form"
