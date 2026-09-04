from abc import ABC, abstractmethod
from ex0 import Creature
from ex1 import HealCapability, TransformCapability
from typing import cast


class InvalidStrategyError(Exception):
    pass


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature) -> None:
        ...

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        ...


class NormalStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' for this normal strategy"
            )
        print(creature.attack())

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)


class AggressiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}'"
                " for this aggressive strategy"
            )
        print(cast(TransformCapability, creature).transform())
        print(creature.attack())
        print(cast(TransformCapability, creature).revert())

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)


class DefensiveStrategy(BattleStrategy):

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}'"
                " for this defensive strategy"
            )
        print(creature.attack())
        print(cast(HealCapability, creature).heal())

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)
