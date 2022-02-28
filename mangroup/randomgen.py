import random


class RandomGen(object):
    # Values that may be returned by next_num()
    _random_nums: list[int] = []

    # Probability of the occurence of random_nums
    _probabilities: list[float] = []

    def __init__(
        self, random_nums: list[int], probabilities: list[float]
    ) -> None:
        """
        Initialise random_nums and probabilities lists.
        """
        if len(random_nums) != len(probabilities):
            raise IndexError

        self._probabilities = probabilities
        self._random_nums = random_nums

    def next_num(self) -> int:
        """
        Returns one of the randomNums. When this method is called
        multiple times over a long period, it should return the
        numbers roughly with the initialized probabilities.
        """

        return random.choices(
            self._random_nums, weights=self._probabilities, k=1
        )[0]
