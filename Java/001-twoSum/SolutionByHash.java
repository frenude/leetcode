import java.util.Arrays;
import java.util.HashMap;

/**
 * @Author: Frenude
 * @Description: //TODO
 * @Date: Created in 01 04,2021
 * @Modified By:
 **/
public class SolutionByHash {
    public static void main(String[] args) {
        int[] nums = {2, 7, 11, 15};
        int target = 9;
        Solution solution = new Solution();
        // lambda 练习
//        BiFunction<int[], Integer, int[]> twoSum = solution::twoSum;
//        int[] ints = twoSum.apply(nums, target);
        int[] ints = solution.twoSum(nums, target);
        System.out.println(Arrays.toString(ints));
    }
}

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> hashMap = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (hashMap.containsKey(target - nums[i])) {
                return new int[]{hashMap.get(target - nums[i]), i};
            }
            hashMap.put(nums[i], i);
        }
        return new int[0];
    }
}
