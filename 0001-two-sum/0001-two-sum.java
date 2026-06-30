class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> numList = new HashMap<>();
        int[] ans = new int[2];

        for (int i=0;i<nums.length;i++){
            int complement = target - nums[i];
            if (numList.containsKey(complement)){
                ans[0] = numList.get(complement);
                ans[1] = i;
                break;
            }
            numList.put(nums[i], i);
        } 

        return ans;
    }
}