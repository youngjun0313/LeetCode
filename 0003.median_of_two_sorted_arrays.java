class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int l = nums1.length + nums2.length;
        int[] nums = new int[l];
        int pn=0;
        int pm=0;

        if(nums1.length==0) {
            nums = nums2;
        } else if(nums2.length==0) {
            nums = nums1;
        } else {
            for(int i=0; i<l; i++) {
                if(pn>=nums1.length) {
                    nums[i] = nums2[pm];
                    pm++;
                } else if(pm>=nums2.length) {
                    nums[i] = nums1[pn];
                    pn++;
                } else {
                    if (nums1[pn] < nums2[pm]) {
                        nums[i] = nums1[pn];
                        pn++;
                    } else {
                        nums[i] = nums2[pm];
                        pm++;
                    }
                }
            }
        }
        if(l==1)
            return nums[0];
        else {
            if(l%2==0){
                return (nums[l/2] + nums[l/2-1])/2.0;
            } else {
                return nums[l/2];
            }
        }
    }
}