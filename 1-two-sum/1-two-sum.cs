public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int, int> map = new Dictionary<int, int>();
        int remaining;
        for (int i = 0; i < nums.Length; i++) {
            remaining = target - nums[i];
            if (map.ContainsKey(remaining)) {
                return new int[] {i, map[remaining]};
            }
            map[nums[i]] = i;
        }
        return new int[0];
    }
}
