def twoSum(nums, target):
    dict_ = dict()
    for i in range(len(nums)):
        if target - nums[i] in dict_:
            return [i,dict_[target -nums[i]]]
        else:
            dict_[nums[i]] = i