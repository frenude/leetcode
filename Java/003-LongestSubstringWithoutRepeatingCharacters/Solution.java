import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;

/**
 * @Author: Frenude
 * @Description: //TODO
 * @Date: Created in 01 05,2021
 * @Modified By:
 **/


public class Solution {

    public static void main(String[] args) {
        String s = "pwwkew";
        Solution solution = new Solution();
        int i = solution.lengthOfLongestSubstring(s);
        System.out.println(i);
    }


    public int lengthOfLongestSubstring(String s) {
        int l = -1;
        int r = 0;
        HashMap<Character, Integer> map = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            if (map.containsKey(s.charAt(i)) && map.get(s.charAt(i)) > l) {
                l = map.get(s.charAt(i));
                map.put(s.charAt(i), i);
            } else {
                map.put(s.charAt(i), i);
                r = Math.max(r, i - l);
            }
        }
        return r;
    }

}
