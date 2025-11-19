/**
 * @brief Given a binary tree root, return its maximum depth.
 *
 * Variant: Depth-first search using an explicit stack to track per-node depth.
 * This preserves the semantic goal (maximum number of levels) but uses a
 * different traversal strategy from the breadth-first variants.
 */
 int maxDepth(TreeNode* root) {
    // Empty tree has depth 0
    if (!root) {
        return 0;
    }

    // Stack holds pairs of (node, depth_of_node)
    std::stack<std::pair<TreeNode*, int>> st;
    st.push(std::make_pair(root, 1));

    int maxDepthFound = 0;

    while (!st.empty()) {
        std::pair<TreeNode*, int> cur = st.top();
        st.pop();

        TreeNode* node = cur.first;
        int depth = cur.second;

        if (!node) continue;

        if (depth > maxDepthFound) {
            maxDepthFound = depth;
        }

        // Push children with incremented depth (right before left to mirror typical DFS order)
        if (node->right) st.push(std::make_pair(node->right, depth + 1));
        if (node->left)  st.push(std::make_pair(node->left, depth + 1));
    }

    return maxDepthFound;
}
