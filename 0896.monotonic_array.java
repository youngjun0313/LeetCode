class Solution {
    public boolean isMonotonic(int[] nums) {
        if(nums.length == 1)
            return true;

        boolean inc;
        inc = nums[0] <= nums[nums.length - 1];
        int prev = nums[0];

        for(int e: nums) {
            if(inc) {
                if(prev>e)
                    return false;
                prev = e;
            } else {
                if(prev<e)
                    return false;
                prev = e;
            }
        }
        return true;
    }
}