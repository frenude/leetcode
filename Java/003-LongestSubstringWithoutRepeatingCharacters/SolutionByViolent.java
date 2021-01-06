import java.util.HashMap;
import java.util.HashSet;

/**
 * @Author: Frenude
 * @Description: //TODO
 * @Date: Created in 01 05,2021
 * @Modified By:
 **/


public class SolutionByViolent {

    public static void main(String[] args) {
        String s = "pwwkew";
        SolutionByViolent solution = new SolutionByViolent();
        int i = solution.lengthOfLongestSubstring(s);
        System.out.println(i);
    }


    public int lengthOfLongestSubstring(String s) {
        if (s == null && s.length() == 0) {
            return 0;
        }
        int max_l = 0;
        HashSet<Character> set = new HashSet<>();
        for (int i = 0; i < s.length(); i++) {
            int l = 0;
            for (int j = i; j < s.length(); j++) {
                if (set.contains(s.charAt(j))) {
                    break;
                }
                set.add(s.charAt(j));
                l++;
            }
            max_l = Math.max(l, max_l);
            set.clear();
        }
        return max_l;
    }

}
