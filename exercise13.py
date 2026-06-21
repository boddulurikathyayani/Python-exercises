def check_list(nums):
    if nums[0] == nums[-1]:
        return True
    else:
        return False

# Test
print(check_list([10, 20, 30, 10]))
print(check_list([10, 20, 30, 40]))
#output:
True
False
