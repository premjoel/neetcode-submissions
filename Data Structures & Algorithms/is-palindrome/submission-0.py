class Solution:
    def isPalindrome(self, s: str) -> bool:
        # rev_string = [0]*len(s)
        original = []
        for i,st in enumerate(s):
            if st.isalnum():
                original.append(st.lower())
        
        rev_string = original[::-1]
        print(rev_string, original)
        if original == rev_string:
            return True
        else:
            return False
            

        