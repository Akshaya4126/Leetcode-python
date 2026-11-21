class Solution:
    def reverseKGroup(self, head, k):
        current = head
        count = 0

        while current and count < k:
            current = current.next
            count += 1

        if count == k:
            current = self.reverseKGroup(current, k)

            while count > 0:
                temp = head.next
                head.next = current
                current = head
                head = temp
                count -= 1

            head = current

        return head