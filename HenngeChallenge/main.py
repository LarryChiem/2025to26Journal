import sys


def sum_fourth_powers(nums, index):
    # Recursively sum the 4th powers of non-positive values (<= 0).
    if index == len(nums):
        return 0

    current = nums[index]

    if current <= 0:
        return (current**4) + sum_fourth_powers(nums, index + 1)
    else:  # Positive values are excluded
        return sum_fourth_powers(nums, index + 1)


def process_testcases(lines, idx, remaining, output):
    if remaining == 0:
        return output

    X = int(lines[idx])
    nums = list(map(int, lines[idx + 1].split()))

    # If X doesn't match the count of provided integers, output -1 for this test case.
    if len(nums) != X:
        output.append("-1")
    else:
        total = sum_fourth_powers(nums, 0)
        output.append(str(total))

    return process_testcases(lines, idx + 2, remaining - 1, output)


# Example
# Input:
# 2   # N, number of test cases to follow (1 <= N <= 100)
# 4   # X, number of space-separated integers Yn (-100 <= Yn <= 100)
# 3 -1 1 10 # Yn, space-separated integers. Now, calculate the power of four of Yn, excluding when Yn is positive, then sum it up.
# 5   # X, number of space-separated integers Yn (-100 <= Yn <= 100)
# 9 -5 -5 -10 10

# Output:
# 1
# 11250

# Explanation:
# 1 = -1^4, we exclude 3, 1, and 10 because they are positive.
# 11250 = -5^4 + -5^4 + -10^4, we exclude 9 and 10 because they are positive.


def main():
    # Read all input from standard input.
    # (When running locally, send EOF after the final line.)
    lines = sys.stdin.read().strip().splitlines()

    n = int(lines[0])

    results = process_testcases(lines, 1, n, [])
    sys.stdout.write("\n".join(results))


if __name__ == "__main__":
    main()
