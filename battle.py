from ex0 import CreatureFactory, FlameFactory, AquaFactory


def test_factory(factory: CreatureFactory) -> None:
    base_creature = factory.create_base()
    print(base_creature.describe())
    print(base_creature.attack())

    evolved_creature = factory.create_evolved()
    print(evolved_creature.describe())
    print(evolved_creature.attack())


def test_battle(
    factory_1: CreatureFactory,
    factory_2: CreatureFactory
) -> None:

    creature_1 = factory_1.create_base()
    creature_2 = factory_2.create_base()

    print(creature_1.describe())
    print("vs.")
    print(creature_2.describe())

    print("Fight!")
    print(creature_1.attack())
    print(creature_2.attack())


def main() -> None:
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()

    print("Testing Factory")
    test_factory(flame_factory)
    print()

    print("Testing Factory")
    test_factory(aqua_factory)
    print()

    print("Testing Battle")
    test_battle(flame_factory, aqua_factory)


if __name__ == "__main__":
    main()
