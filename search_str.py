import time

count_word_dict = {}
n = int(input())//2

for i in range(0,n):
    
    count_word_input = input().split(' ')
    pref = input().split(' ')[1]
    
    count = int(count_word_input[1])
    word = count_word_input[2]
    
    if word in count_word_dict.keys():
        count_word_dict[word] += count
    else:
        count_word_dict[word] = count
    
    pref_ident = {}    
    for k, v in count_word_dict.items():
        pref_ident_list = list(pref_ident.values())
        if k.startswith(pref) & (v in pref_ident_list):
                ident_key = str(list(pref_ident.keys())[pref_ident_list.index(v)])
                if k < ident_key:
                    del pref_ident[ident_key]
                    pref_ident[k] = v
        else:
            pref_ident[k] = v
                
    sorted_dict = {k: v for k, v in sorted(pref_ident.items(), key=lambda item: item[1], reverse=True)}
    print(list(sorted_dict.keys())[0])

                
                        
    
    
    
