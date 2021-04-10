import unittest

# the analyze function takes in an var arguent of numbers
# it should return a dicitonary of {'mean':0,'median':0,'mode':0,'largest':0,'smallest':0}
def analyze(*nums):
    dct = {}
    dct['mean'] = sum(nums)/len(nums)
    dct['largest'] = max(nums)
    dct['smallest'] = min(nums)
    sorted_nums = sorted(nums)
    middle_i = len(sorted_nums) // 2
    if len(nums)%2 == 0:
        dct['median'] = (sorted_nums[middle_i] + sorted_nums[middle_i + 1]) / 2
    else:
        dct['median'] = sorted_nums[middle_i]
    
    nums_count = {}
    highest_count = 0
    cur_mode = nums[0]
    for num in nums:
        if num in nums_count.keys():
            nums_count[num] += 1
        else:
            nums_count[num] = 1

        if nums_count[num] > highest_count:
            highest_count = nums_count[num]
            cur_mode = num
    
    dct['mode'] = cur_mode
    return dct

########################### TESTS ##############################################################
class TestMethods(unittest.TestCase):

    def test_analyze_1(self):
        data = analyze(1,2,2,2,3)
        self.assertDictEqual(data, {'mean':2,'median':2,'mode':2, 'largest':3,'smallest':1})
        

    def test_analyze_2(self):
        data = analyze(10,5,10,200,-65)
        self.assertDictEqual(data, {'mean':32,'median':10,'mode':10, 'largest':200,'smallest':-65})
        


if __name__ == '__main__':
    unittest.main()
