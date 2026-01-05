def group_indices(numbers: list[int]) -> dict[int, list[int]]:
    group = {}
    for idx, num in enumerate(numbers):
        if num not in group:
            group[num] = []
        group[num].append(idx)
    return group
nums = [1, 2, 3, 1, 2, 1, 3, 3, 3]
result = group_indices(numbers=nums)
print(result)
