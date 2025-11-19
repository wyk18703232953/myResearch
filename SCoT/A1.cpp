/**
 * @brief Given a binary tree root, return its maximum depth.
 *
 * Variant: Recursive post-order depth calculation using a small internal helper.
 * The depth of a node is 1 + max(depth(left), depth(right)).
 * This keeps semantics identical (the number of levels from root to deepest leaf).
 */

// Internal helper: computes depth of a subtree rooted at `node`
static int depthRec(TreeNode* node) {
    if (!node) {
        // An empty subtree contributes zero depth
        return 0;
    }
    int leftDepth  = depthRec(node->left);
    int rightDepth = depthRec(node->right);

    // Choose the deeper side and add one for the current node
    return (leftDepth > rightDepth ? leftDepth : rightDepth) + 1;
}

// Public interface expected by callers
int maxDepth(TreeNode* root) {
    // Delegate to the recursive helper
    return depthRec(root);
}
