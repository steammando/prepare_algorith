def alternate(s):
    # Write your code here
    char_type = []
    length = 0
    for i in s:
        if i not in char_type:
            char_type.append(i)
    print(char_type)
    
    for i in range(len(char_type)):      
        for j in range(i+1, len(char_type)):
            selected = [char_type[i], char_type[j]]
            deleted = ''
            for k in range(0, len(s)):                  
                if s[k] == selected[0]:
                    deleted += selected[0]
                if s[k] == selected[1]:
                    deleted += selected[1]
                deleted_len = len(deleted)
                
                if deleted_len > 1:
                    if deleted[deleted_len - 2] == deleted[deleted_len - 1]:
                        deleted = ''
                        break
            if len(deleted) > length:
                length = len(deleted)
            print(selected, deleted, length)
    if length < 2:
        length = 0 
    return length
