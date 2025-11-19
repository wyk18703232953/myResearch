 /**
 * @brief Given a binary tree root, return its maximum depth.
 *
 * Variant: Breadth-first search using a level delimiter (nullptr) to mark level boundaries.
 * This preserves semantics (maximum number of levels) but changes the traversal detail.
 */
 int maxDepth(TreeNode* root) {
    // If the tree is empty, depth is zero
       if (!root) {
           return 0;
       }
   
       std::queue<TreeNode*> q;
       q.push(root);
       q.push(nullptr); // Level delimiter to separate levels
       int depth = 0;
   
       while (!q.empty()) {
           TreeNode* node = q.front();
           q.pop();
   
           if (node == nullptr) {
               // Completed one level
               ++depth;
               // If more levels exist, add another delimiter for the next level
               if (!q.empty()) {
                   q.push(nullptr);
               }
           } else {
               // Enqueue children for the next level
               if (node->left)  q.push(node->left);
               if (node->right) q.push(node->right);
           }
       }
   
       return depth;
   }',
   