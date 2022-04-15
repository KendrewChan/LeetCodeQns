class Solution {
    
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> lst = new ArrayList<>();
        recursePermute(lst, nums, new ArrayList<>());
        return lst;
    }
    
    void recursePermute(List<List<Integer>> lst, int[] nums, List<Integer> curr) {
        if (curr.size() == nums.length) {
            lst.add(new ArrayList<>(curr));
        } else {
            for (int i = 0; i < nums.length; i++) {
                int c = nums[i];
                if (curr.contains(c)) continue;
                curr.add(c);
                recursePermute(lst, nums, curr);
                curr.remove(curr.size()-1);
            }
        }
    }
}