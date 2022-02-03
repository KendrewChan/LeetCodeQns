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
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> vect;
        inOrder(vect, root);
        return vect;
    }
    
    void inOrder(vector<int>& vect, TreeNode* curr) {
        if (curr == NULL) return;
        inOrder(vect, curr->left);
        vect.push_back(curr->val);
        inOrder(vect, curr->right);
    }
};