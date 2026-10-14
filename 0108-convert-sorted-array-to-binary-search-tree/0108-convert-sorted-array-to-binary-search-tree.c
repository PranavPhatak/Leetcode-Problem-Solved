/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
struct TreeNode *sortedArrayToBST(int *nums, int numsSize) {

if(numsSize <= 0){
    return NULL;
}

int mid = numsSize/2;
struct TreeNode* newNode = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    newNode->val = nums[mid];
    newNode->left = sortedArrayToBST(nums,mid);
     newNode->right = sortedArrayToBST(nums+mid+1,numsSize-mid-1);

return newNode;
}

