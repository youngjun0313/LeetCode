class Solution {
    public void sortColors(int[] nums) {
        int one_pivot = 0;
        int two_pivot = 0;

        for(int i = 0; i< nums.length; i++) {
            if(nums[i] == 0) {
                swap(nums, i, two_pivot);
                swap(nums, two_pivot, one_pivot);
                one_pivot++;
                two_pivot++;
            } else if(nums[i] == 1) {
                swap(nums, i, two_pivot);
                two_pivot++;
            }
        }
    }

    private static void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}