from ex0 import AquaFactory, FlameFactory, CreatureFactory


def testing_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    base = factory.create_base()
    print(f"{base.describe()}")
    print(base.attack())
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())


def fight(flameling: FlameFactory, aquabub: AquaFactory) -> None:
    flame_base = flameling.create_base()
    aqua_base = aquabub.create_base()
    print(flame_base.describe())
    print(" vs.")
    print(aqua_base.describe())
    print(" fight!")
    print(flame_base.attack())
    print(aqua_base.attack())


if __name__ == "__main__":
    flameling = FlameFactory()
    aquabub = AquaFactory()
    testing_factory(flameling)
    print()
    testing_factory(aquabub)
    print("\nTesting battle")
    fight(flameling, aquabub)
