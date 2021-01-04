/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
	let reduceHash = {}
	for (let i = 0; i < nums.length; i++) {
		let reduceResult = target - nums[i]
		if (reduceHash[reduceResult] === 0 || reduceHash[reduceResult]) {
			return [reduceHash[reduceResult], i]
		}
		reduceHash[nums[i]] = i
	}
}

const index = twoSum([1, 3, 5], 4)
console.log(index) // [0, 1]
