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
    vector<vector<int>> vect;
    void helper(TreeNode* root, int target, vector<int> curr) {
        if (root == NULL) return;
        vector<int> temp = curr;
        int t = target - root->val;
        temp.push_back(root->val);
        if (root->left == NULL && root->right == NULL) {
            if (t == 0) {
                vect.push_back(temp);
            }
            return;
        }
        if (root->left != NULL) {
            helper(root->left, t, temp);
        }
        if (root->right != NULL) {
            helper(root->right, t, temp);
        }
    }
    
public:
    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        vector<int> temp;
        helper(root, targetSum, temp);
        return vect;
    }
};