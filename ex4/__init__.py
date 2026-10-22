from abc import ABC, abstractmethod
import typing
from ex3.creature import Creature, TransformCapability


class InvalidStrategyError(Exception):
    pass


class CreatureTransform(typing.Protocol):
    def attack(self) -> str:
        pass

    def transformed(self) -> str:
        pass

    def revert(self) -> str:
        pass


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, entity: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, entity: Creature) -> None:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, entity: Creature) -> bool:
        return True

    def act(self, entity: Creature) -> None:
        if not self.is_valid(entity):
            raise InvalidStrategyError(
                    f"Invalid Creature {entity.name}"
                    f" for this normal strategy"
                    )
        print(entity.attack())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, entity: Creature) -> bool:
        return isinstance(entity, TransformCapability)

    def act(self, entity: Creature) -> None:
        if not self.is_valid(entity):
            raise InvalidStrategyError(
                    f"Invalid Creature {entity.name}"
                    f" for this aggressive strategy"
                    )
        creature = typing.cast(CreatureTransform, entity)
        print(creature.transformed())
        print(creature.attack())
        print(creature.revert())


__all__ = [
        "BattleStrategy",
        "NormalStrategy",
        "AggressiveStrategy",
        "InvalidStrategyError"
        ]
