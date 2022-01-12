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

const deleteDuplicates = (head) => {
  let curNode = head;
  while (curNode && curNode.next) {
    let nextNode = curNode.next;
    while (curNode.val === nextNode.val) {
      nextNode = nextNode.next;
    }
    curNode.next = nextNode;
    curNode = curNode.next;
  }
  return head;
};
