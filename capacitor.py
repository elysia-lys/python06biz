from typing import Protocol
from ex3 import TransformCreatureFactory


class CreatureTransform(Protocol):
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        pass

    def transformed(self) -> str:
        pass

    def revert(self) -> str:
        pass


def test_transform(creature: CreatureTransform) -> None:
    print(creature.describe())
    print(creature.attack())
    print(creature.transformed())
    print(creature.attack())
    print(creature.revert())


if __name__ == "__main__":
    factory = TransformCreatureFactory()
    base = factory.create_base()
    evolved = factory.create_evolved()

    print("Testing Creature with transform capability")
    print("base:")
    test_transform(base)
    print("evolved:")
    test_transform(evolved)
