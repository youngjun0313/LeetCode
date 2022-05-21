class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int n1=nums1.length;
        int n2=nums2.length;
        int l = n1 + n2;
        int[] nums;
        int pn=0;
        int pm=0;

        if(n1==0) {
            nums = nums2;
        } else if(n2==0) {
            nums = nums1;
        } else {
            nums = new int[l/2+1];
            for(int i=0; i<l/2+1; i++) {
                if(pn>=n1) {
                    nums[i] = nums2[pm];
                    pm++;
                } else if(pm>=n2) {
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