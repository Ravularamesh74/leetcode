/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var swapPairs = function(head) {

    // Dummy node before head
    let dummy = new ListNode(0);
    dummy.next = head;

    let prev = dummy;

    // Need at least 2 nodes to swap
    while (prev.next && prev.next.next) {

        let first = prev.next;
        let second = prev.next.next;

        // Swapping
        first.next = second.next;
        second.next = first;
        prev.next = second;

        // Move prev to next pair
        prev = first;
    }

    return dummy.next;
};