/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle = function(head) {
    if (!head || !head.next) {
        return false;
    }
    
    let slow = head;
    let fast = head;
    
    while (fast !== null && fast.next !== null) {
        slow = slow.next;          // Moves 1 step
        fast = fast.next.next;     // Moves 2 steps
        
        if (slow === fast) {
            return true;           // Cycle detected
        }
    }
    
    return false;                  // Reached the end of the list, no cycle
};
