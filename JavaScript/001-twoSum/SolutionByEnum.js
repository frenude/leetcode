/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
	for (let i = 0; i < nums.length; i++) {
		for (let j = i + 1; j < nums.length; j++) {
			if (nums[j] == target - nums[i]) {
				return [i, j]
			}
		}
	}
	return []
}

const index = twoSum([1, 3, 5], 4)
console.log(index) // [0, 1]
