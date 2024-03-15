from typing import Dict
from typing import NewType

# Could easily abstract some of this and input in not only number of trees
# but also costs of each blob. Then it would be easy to add new levels
# as each blob acts in the same way but will have new costs attached
class Level1:
    Choices = NewType("Choices", Dict[str, int])

    def __init__(self, target: int):
        self.__target = target

    def __getUserChoices(self) -> Choices:
        choices: Dict[str, int] = {}
        print(f"There are {self.__target} trees, each red blob cuts a tree once and each")
        print("purple blob causes each red blob to act again.")
        print()
        print("Prices of blobs:")
        print("Red - 1")
        print("Purple - 5")
        print()
        choices["red"] = int(input("How many red blobs do you wish to buy?\n"))
        choices["purple"] = int(input(
            "How many purple blobs do you wish to buy?\n"))
        return self.Choices(choices)

    def __redsAct(self, reds: int) -> int:
        chopped: int = 0
        for _ in range(reds):
            chopped += 1
        return chopped

    def __purplesAct(self, reds: int, purples: int) -> int:
        chopped: int = 0
        for _ in range(purples):
            chopped += self.__redsAct(reds)
        return chopped

    # This is not optimised but is more meant to serve as a way to show
    # how the blobs act together, otherwise you could just do
    # reds * (purples + 1)
    def __chopped(self, choices: Choices) -> int:
        chopped: int = 0
        chopped += self.__redsAct(reds=choices["red"])
        chopped += self.__purplesAct(reds=choices["red"],
                                     purples=choices["purple"])

        return chopped

    def __cost(self, choices: Choices) -> int:
        cost: int = 0
        cost += choices["red"]
        cost += choices["purple"]

        return cost

    def run(self) -> None:
        choices: Dict[str, int] = self.__getUserChoices()
        chopped = self.__chopped(choices)
        if chopped >= self.__target:
            print("Success")
            print(f"Cost = {str(self.__cost(choices))}")
            print(f"Total chopped = {str(chopped)}")
        else:
            print("Fail")
            print(f"Cost = {str(self.__cost(choices))}")
            print(f"Total chopped = {str(chopped)}")


def main() -> None:
    l1 = Level1(20)
    l1.run()


if __name__ == "__main__":
    main()
