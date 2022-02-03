/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> vect;
        helper(vect, root);
        return vect;
    }
    
    void helper(vector<int>& vect, TreeNode* curr) {
        if (curr == NULL) return;
        helper(vect, curr->left);
        helper(vect, curr->right);
        vect.push_back(curr->val);
    }
};