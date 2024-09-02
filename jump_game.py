def min_jumps(nums):
    n = len(nums)
    if n <= 1:
        return 0

    jumps = 0
    current_end = 0
    farthest = 0

    for i in range(n - 1):
        farthest = max(farthest, i + nums[i])
        if i == current_end:
            jumps += 1
            current_end = farthest
            if current_end >= n - 1:
                break

    return jumps

# Test cases
def test_min_jumps():
    assert min_jumps([2, 3, 1, 1, 4]) == 2, "Test case 1 failed"
    assert min_jumps([2, 3, 0, 1, 4]) == 2, "Test case 2 failed"
    assert min_jumps([1, 2, 3]) == 2, "Test case 3 failed"
    assert min_jumps([1, 1, 1, 1]) == 3, "Test case 4 failed"
    assert min_jumps([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 0]) == 1, "Test case 5 failed"
    print("All test cases passed!")

if __name__ == "__main__":
    test_min_jumps()