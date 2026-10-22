from ex3.creature import CreatureFactory
from ex3 import FlameFactory, TransformCreatureFactory
from ex4 import (
    BattleStrategy,
    NormalStrategy,
    AggressiveStrategy,
    InvalidStrategyError,
)
import typing


def battle(
        opponents: typing.Sequence[
            tuple[CreatureFactory, BattleStrategy
                  ]
            ]
        ) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            factory1, strategy1 = opponents[i]
            factory2, strategy2 = opponents[j]

            creature1 = factory1.create_base()
            creature2 = factory2.create_base()

            print("* Battle *")
            print(creature1.describe())
            print("vs.")
            print(creature2.describe())
            print("now fight!")

            try:
                strategy1.act(creature1)
                strategy2.act(creature2)
            except InvalidStrategyError as error:
                print(f"Battle error, aborting tournament: {error}")
                return


if __name__ == "__main__":
    basic = [
            (FlameFactory(), NormalStrategy()),
            (TransformCreatureFactory(), AggressiveStrategy())
            ]

    error = [
            (TransformCreatureFactory(), AggressiveStrategy()),
            (FlameFactory(), AggressiveStrategy()),
            ]

    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Shiftling+Aggressive) ]")
    battle(basic)

    print("\nTournament 1 (error)")
    print("[ (Shiftling+Aggressive), (Flameling+Aggressive) ]")
    battle(error)
