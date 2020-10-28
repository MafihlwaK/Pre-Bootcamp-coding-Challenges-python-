string = "datAsciEnce"

def vowels(str):
    vow1 = "aeiouAEIOU"
    ans = []
    for char in str:
        if char in vow1:
            ans.append(char)
    return ans

print(vowels(string))



 


    