class Solution {
    public void sortColors(int[] nums) {
        List<Integer> zeros = new ArrayList<>();
        List<Integer> ones = new ArrayList<>();
        List<Integer> twos = new ArrayList<>();
        List<Integer> numbers = new ArrayList<>();

        for(int e: nums) {
            if(e==0) {
                zeros.add(e);
            } else if (e==1) {
                ones.add(e);
            } else {
                twos.add(e);
            }
        }

        numbers.addAll(zeros);
        numbers.addAll(ones);
        numbers.addAll(twos);

        for (int i = 0; i < nums.length; i++) {
            nums[i] = numbers.get(i);
        }
    }
}