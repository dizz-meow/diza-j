class Solution(object):
    def movesToStamp(self, stamp, target):
        M, N = len(stamp), len(target)
        target_chars = list(target)
        res = []
        
        # A flag to check if we made any replacement during a full scan
        changed = True
        
        # Helper function to check if stamp can be placed at index `i`
        def can_stamp(i):
            made_change = False
            for j in range(M):
                # '?' acts as a wildcard because it was already stamped in a later step
                if target_chars[i + j] == '?':
                    continue
                elif target_chars[i + j] != stamp[j]:
                    return False
                else:
                    made_change = True
            
            # Returns True only if it matches and has at least one non-'?' character to change
            return made_change

        while changed:
            changed = False
            # Scan all possible starting positions for the stamp
            for i in range(N - M + 1):
                if can_stamp(i):
                    # Replace characters with '?' to simulate reverse stamping
                    for j in range(M):
                        target_chars[i + j] = '?'
                    changed = True
                    res.append(i)
                    
        # If the entire target is converted to '?', we found a valid sequence
        if all(c == '?' for c in target_chars):
            return res[::-1] # Reverse the result because we worked backwards
            
        return []
