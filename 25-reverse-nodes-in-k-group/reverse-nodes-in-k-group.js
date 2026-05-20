/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} k
 * @return {ListNode}
 */

var reverseKGroup = function(head, k) {

    let dummy = new ListNode(0);
    dummy.next = head;

    let groupPrev = dummy;

    while (true) {

        // Find kth node
        let kth = groupPrev;

        for (let i = 0; i < k && kth !== null; i++) {
            kth = kth.next;
        }

        // Less than k nodes left
        if (kth === null) break;

        let groupNext = kth.next;

        // Reverse group
        let prev = groupNext;
        let curr = groupPrev.next;

        while (curr !== groupNext) {
            let temp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = temp;
        }

        // Connect reversed group
        let temp = groupPrev.next;

        groupPrev.next = kth;

        groupPrev = temp;
    }

    return dummy.next;
  
};