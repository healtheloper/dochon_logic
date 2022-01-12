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
const hasCycle = (head) => {
  if (!head || !head.next || !head.next.next) return false;
  let nodePointer1 = head.next;
  let nodePointer2 = head.next.next;

  while (nodePointer1 !== nodePointer2) {
    if (!nodePointer1) return false;
    nodePointer1 = nodePointer1.next;
    if (!nodePointer2 || !nodePointer2.next) return false;
    nodePointer2 = nodePointer2.next.next;
  }
  return true;
};
