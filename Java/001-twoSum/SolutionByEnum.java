import java.util.Arrays;

/**
 * @Author: Frenude
 * @Description: //TODO
 * @Date: Created in 01 04,2021
 * @Modified By:
 **/
public class SolutionByEnum {

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
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if ((nums[i] + nums[j]) == target) {
                    return new int[]{i, j};
                }
            }
        }
        return new int[0];
    }
}
