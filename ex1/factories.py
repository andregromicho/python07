from .creatures import Creature, Sproutling, Bloomelle, Shiftling, Morphagon
from ex0 import CreatureFactory


class HealingCreatureFactory(CreatureFactory):

    def create_base(self) -> Creature:
        return Sproutling()

    def create_evolved(self) -> Creature:
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Shiftling()

    def create_evolved(self) -> Creature:
        return Morphagon()
