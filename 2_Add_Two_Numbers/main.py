# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def set_next(self, next=None):
        if next:
            self.next = next


class Solution:
    def addTwoNumbers(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:
        carry = 0
        sum = 0
        power = -1

        while l1 is not None or l2 is not None:
            power += 1
            print(l1.val)
            temp_sum = l1.val + l2.val
            if temp_sum > 9:
                carry, temp_sum = divmod(temp_sum, 10)
                print(carry, temp_sum)
            sum += (temp_sum + carry) * (power*10)

            carry = 0
            l1 = l1.next
            l2 = l2.next

        return sum


def CreateList(l1: [list]) -> ListNode:
    for i, val in enumerate(l1):
        if i > 0:
            new_node = ListNode(val=val)
            prev_node.set_next(new_node)
            prev_node = new_node
        else:
            head_node = ListNode(val=val)
            prev_node = head_node

    print(head_node.val, head_node.next)

    return head_node


p = Solution()
print(
    p.addTwoNumbers(l1=CreateList([2, 4, 3]), l2=CreateList([5, 6, 4])))
# print(Solution.addTwoNumbers(l1 = [0], l2 = [0]))
# print(Solution.addTwoNumbers(l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]))
