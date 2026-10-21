from abc import ABC, abstractmethod


# creature class
class Creature(ABC):
    def __init__(self, name: str, entity_type: str) -> None:
        self.name: str = name
        self.entity_type: str = entity_type

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return (f"{self.name} is a {self.entity_type} type Creature")


# transform class
class TransformCapability(ABC):
    @abstractmethod
    def transformed(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass


# the creatures
class Flameling(Creature):
    def __init__(self) -> None:
        super().__init__("Flameling", "Fire")

    def attack(self) -> str:
        return (f"{self.name} uses Ember!")


class Pyrodon(Creature):
    def __init__(self) -> None:
        super().__init__("Pyrodon", "Fire/Flying")

    def attack(self) -> str:
        return (f"{self.name} uses Flamethrower!")


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Shiftling", "Normal")
        self.transform: bool = False

    def attack(self) -> str:
        if self.transform:
            return (f"{self.name} performs a boosted strike!")
        return (f"{self.name} attacks normally.")

    def transformed(self) -> str:
        self.transform = True
        return (f"{self.name} shifts into a sharper form!")

    def revert(self) -> str:
        self.transform = False
        return (f"{self.name} returns to normal.")


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Morphagon", "Normal/Dragon")
        self.transform: bool = False

    def attack(self) -> str:
        if self.transform:
            return (f"{self.name} unleashes a devastating morph strike!!")
        return (f"{self.name} attacks normally.")

    def transformed(self) -> str:
        self.transform = True
        return (f"{self.name} morphs into a dragonic battle form!")

    def revert(self) -> str:
        self.transform = False
        return (f"{self.name} stabilizes its form.")


# factory class
class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        pass


class FlameFactory(CreatureFactory):
    def create_base(self) -> Flameling:
        return Flameling()

    def create_evolved(self) -> Pyrodon:
        return Pyrodon()


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Shiftling:
        return Shiftling()

    def create_evolved(self) -> Morphagon:
        return Morphagon()
