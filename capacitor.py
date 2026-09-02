from ex1 import CreatureFactory, HealingCreatureFactory, TransformCreatureFactory

def main():

    healing_factory = HealingCreatureFactory()

    print ("Testing Creature with healing capability")
    print("base:")
    base_heal = healing_factory.create_base()
    evolved_heal = healing_factory.create_evolved()

