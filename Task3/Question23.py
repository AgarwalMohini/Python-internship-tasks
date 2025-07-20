#Find second Largest

nums = list(map(int, input("Enter numbers: ").split()))
unique_nums = list(set(nums))

if len(unique_nums) < 2:
    print("No second largest number.")
else:
    unique_nums.sort(reverse=True)
    print("Second largest number is:", unique_nums[1])
