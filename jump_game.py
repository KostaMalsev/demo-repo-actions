def min_jumps(nums):
    """
    Function to calculate the minimum number of jumps required to reach the end of the list.

    :param nums: List of non-negative integers where each element represents the maximum jump length from that position.
    :return: Minimum number of jumps to reach the end of the list.
    """
    n = len(nums)  # Length of the input list.
    if n <= 1:
        return 0  # If the list has one or no elements, no jumps are needed.

    jumps = 0  # Initialize the number of jumps to 0.
    current_end = 0  # Physical end of the current jump.
    farthest = 0  # Farthest we can reach with the current jump.

    for i in range(n - 1):
        farthest = max(farthest, i + nums[i])  # Update the farthest point we can reach.
        if i == current_end:
            jumps += 1  # Increment the number of jumps.
            current_end = farthest  # Update the end of the current jump.
            if current_end >= n - 1:
                break  # Break if we can reach or exceed the last index.
    
    return jumps  # Return the number of jumps.

# Test cases to validate the solution
def test_min_jumps():
    assert min_jumps([2, 3, 1, 1, 4]) == 2, "Test case 1 failed"
    assert min_jumps([2, 3, 0, 1, 4]) == 2, "Test case 2 failed"
    assert min_jumps([1, 2, 3]) == 2, "Test case 3 failed"
    assert min_jumps([1, 1, 1, 1]) == 3, "Test case 4 failed"
    assert min_jumps([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 0]) == 1, "Test case 5 failed"
    print("All test cases passed!")

if __name__ == "__main__":
    test_min_jumps()
