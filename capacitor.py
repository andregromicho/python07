from ex1 import HealingCreatureFactory, TransformCreatureFactory


def main():

    healing_factory = HealingCreatureFactory()

    print("Testing Creature with healing capability")
    base_heal = healing_factory.create_base()
    evolved_heal = healing_factory.create_evolved()

    print("base:")
    print(base_heal.describe())
    print(base_heal.attack())
    print(base_heal.heal())

    print("evolved:")
    print(evolved_heal.describe())
    print(evolved_heal.attack())
    print(evolved_heal.heal())

    transform_factory = TransformCreatureFactory()

    print("Testing Creature with transform capability")
    base_transform = transform_factory.create_base()
    evolved_transform = transform_factory.create_evolved()

    print("base:")
    print(base_transform.describe())
    print(base_transform.attack())
    print(base_transform.transform())
    print(base_transform.attack())
    print(base_transform.revert())

    print("evolved:")
    print(evolved_transform.describe())
    print(evolved_transform.attack())
    print(evolved_transform.transform())
    print(evolved_transform.attack())
    print(evolved_transform.revert())


if __name__ == "__main__":
    main()
