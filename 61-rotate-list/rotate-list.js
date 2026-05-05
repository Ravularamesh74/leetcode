/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = val;
 *     this.next = next || null;
 * }
 */

var rotateRight = function(head, k) {
    if (!head || !head.next || k === 0) return head;

    // Step 1: Find length and tail
    let length = 1;
    let tail = head;
    
    while (tail.next) {
        tail = tail.next;
        length++;
    }

    // Step 2: Normalize k
    k = k % length;
    if (k === 0) return head;

    // Step 3: Make circular
    tail.next = head;

    // Step 4: Find new tail
    let stepsToNewTail = length - k;
    let newTail = head;

    for (let i = 1; i < stepsToNewTail; i++) {
        newTail = newTail.next;
    }

    // Step 5: Break and set new head
    let newHead = newTail.next;
    newTail.next = null;

    return newHead;
};