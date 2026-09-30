def isSubsequence(s: str, t: str) -> bool:
    s_ptr, t_ptr = 0, 0
    
    while s_ptr < len(s) and t_ptr < len(t):
        # If characters match, move the string 's' pointer forward
        if s[s_ptr] == t[t_ptr]:
            s_ptr += 1
        # Always move the target 't' pointer forward
        t_ptr += 1
        
    return s_ptr == len(s)
