from mangroup.randomgen import RandomGen


def count_random_nums(
    random_nums: list[int], probabilities: list[float], trials: int
) -> dict[int, int]:
    """Generate random numbers and return counts for each."""
    gen = RandomGen(random_nums, probabilities)

    nums_count = dict.fromkeys(random_nums, 0)
    for i in range(0, trials):
        next_num = gen.next_num()
        nums_count[next_num] += 1

    return nums_count


if __name__ == "__main__":
    trials = 1000
    random_nums = [-1, 0, 1, 2, 3]
    probabilities = [0.01, 0.3, 0.58, 0.1, 0.01]

    generated_nums = count_random_nums(random_nums, probabilities, trials)

    print(f"Ran {trials} trials. Results:")
    for num, count in generated_nums.items():
        print(f"{num}: {count} times")
