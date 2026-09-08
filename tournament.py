from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    BattleStrategy,
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
    InvalidStrategyError,
)


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    n = len(opponents)

    print("*** Tournament ***")
    print(f"{n} opponents involved\n")

    for i in range(n):
        for j in range(i + 1, n):
            factory_a, strategy_a = opponents[i]
            factory_b, strategy_b = opponents[j]

            creature_a = factory_a.create_base()
            creature_b = factory_b.create_base()

            print("* Battle *")
            print(creature_a.describe())
            print("vs.")
            print(creature_b.describe())
            print("now fight!")

            try:
                strategy_a.act(creature_a)
                strategy_b.act(creature_b)
            except InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}\n")
                return
            print()


def main() -> None:
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    healing_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    normal_strategy = NormalStrategy()
    aggressive_strategy = AggressiveStrategy()
    defensive_strategy = DefensiveStrategy()

    print("Tournament 0 (basic)")
    opponents_t0 = [
        (flame_factory, normal_strategy),
        (healing_factory, defensive_strategy),
    ]
    battle(opponents_t0)

    print("Tournament 1 (error)")
    opponents_t1 = [
        (flame_factory, aggressive_strategy),
        (healing_factory, defensive_strategy),
    ]
    battle(opponents_t1)

    print("Tournament 2 (multiple)")
    opponents_t2 = [
        (aqua_factory, normal_strategy),
        (healing_factory, defensive_strategy),
        (transform_factory, aggressive_strategy),
    ]
    battle(opponents_t2)


if __name__ == "__main__":
    main()
