"""RandomGen testing suite."""

import unittest

from mangroup.randomgen import RandomGen


class TestRandomGen(unittest.TestCase):
    """RandomGen unit testing."""

    def test_empty_inputs(self):
        """Input with empty inputs."""
        gen = RandomGen([], [])
        with self.assertRaises(ValueError):
            gen.next_num()

    def test_different_list_lengths(self):
        """Input with 2 different length lists."""
        with self.assertRaises(IndexError):
            _ = RandomGen([0, 1, 2, 3], [])

    def test_many_trials(self):
        """Verify probability distribution over many trials
        (within an acceptable error of 0.01)."""
        trials = 1000000
        random_nums = [1, 2, 3]
        probabilities = [0.2, 0.2, 0.6]

        gen = RandomGen(random_nums, probabilities)

        nums_count = dict.fromkeys(random_nums, 0)
        for _ in range(0, trials):
            next_num = gen.next_num()
            nums_count[next_num] += 1

        acceptable_error = 0.01
        for probability, count in zip(probabilities, nums_count.values()):
            generated_probability = count / trials
            self.assertLessEqual(
                abs(generated_probability - probability), acceptable_error
            )
