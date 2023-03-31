"""
Problem link:

https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/
"""





# Right Approach
def append_s_t_method(str1, str2):
    i = j = 0
    while i <len(str1) and j <len(str2):
        if str1[i] == str2[j]:
            i +=1
            j +=1
        else:
            i +=1
    return len(str2) - j







#Wrong approach
def append_C_S(s,t):
    count = 0
    for i in range(len(t)):
        if t[i] in s:
            continue
        else:
            new_str = t[i:]
            count = len(new_str)
            break
    
    return count     
            
# test1
s1 = "coaching"
t1 = "coding"

# test 2

s2 = "abcde"
t2 = "a"

# test 3

s3 = "z"
t3 = "abcde"


s4 = "kmeqwbmaymnouefjdkqdzkgznooulizyerzqrelyrdlgvvtywugwhsvuhqwwzrogsxdtdbjlqqhmbnwvrdxfvavfjkawvxxbsavymfjplbafoljfilxumdxkauhithnuryedfseqdzwqdtfpfhnhzriivjlvcuwxpcrkalvkrvkxvcouxwhawmjjdnmhctfkwxhoxjggplgcstjnuxhfhaoniqcfvkekzjcycjjdkbefxkzejzhsdgnttecmrmddpllqijvqfrlczvwtvrnlslfnesatavkdocvtgqhjjkiiwzyigzfobvmjjudvhhtusvqhpysmbcyypmiazjttkljbhzyfbwonwrqrunaamqsahvfihwnxjffipwbihutdaezfsoztrqctloljvvevvdyrkmkyubjdgtvbowjiswdrivrbxatkkcxirvhkzrfmuwbslzcjincffnanjbovxahubcnravizpibdeansgxsbjjdyvnuqzlsznjvaezehegyvosoatfnnqvpqhpxthrnqgkgchjxkdmlpygxpgmcorchqveyxjogzryhvcozqkasumkaaevscaetpxhewwoewmizvaoulpuefmoishuifkvqxrxuebwclzzmgfoexbmkkjcfusdsyuesvpdnthfgdtnawluahukgfbonzobhlgmcelekiekoelnedixcipqivsehyvktihucbxghftbuslgapezebsskzvzcvhcmjeibzglckbaymwrckmnvmojxrknuwsfqijfgpnpkoshhvmnotpzacgsfgitvujoiuscsiebgdgzgletaruamhntjtwzteltbfzkvmmpwzfmzpfqnjgblkrulagfufxiptcywuqxepcrvlvvhaxgvxjedvqywywtjqsfyzywzajlfeeywoavautfcedksvtaglxmcqvowfwguzyziiioxclokbfuqinnciziddonwrmlvlbwofdgxdtdiuaru"

t4 = "dhjexhsvmnlifeeibuirosaaoxcnipishzcvzpixjfrjxhyzepigqktjashiszxdpdbyeqhcjcthogczowbmbtqxwvtbpxbpqgxzwlbwvzzvbknlgytaerzfzxumfondridapbwodizbmitrlriclhvnwwsrkdyjhzqtckfgpciqghxoeuuybuivqhvwdwricrppltbfhraiwticbvrlncooksgeuqatttysuuwqbuivekxcdbtlxyxplhobrsspcfalcwvbbcavljocxbwwpnncrswxqbkhioywrknmthcsxxldyembvkibjdgbsoyrfnmeccwxbvsstekwciclgbiplgfbvbgasntgofipcvhspoieyytruyuyauroyjdjoeqshubpyoaigzochuyroepjpzduwhudmnkewphjwkpgevyaxcgwbsdlvzwvkcmzblibddtjcgbkmpkwefthqkuiqptdqkpnuwrbwwpuxlombjufdowbqixooenjkvnslhhpjnmikmqsgobnsimhszzrsrdmuvbjdiixvzzlcdmevhdajybnxhvtbbasgpvqangnhkcfutlsndfylikjmktzmdcypchehhwusrvvsldqfygwwcoleueklokqqrelqylubfggguivqyvlpvafjstltzhsdaedxpsjxuzuohaftfcwsdcvqoqlrtkpavaskiiuvqkhfzatbfrwajlqxoaysqygcgrkzchhdzugqtqlugzmbimxejyspaoqzrebbzobbvppvlajbgrakbnxlafptwazozvvmsxosvlzreuibwanuknjocbkpepctlfnqriypdcyppmlxavbvyvqnomczqqzsnkjncyqnalytbytsujqwvfaxwksqnooarrjkrgferrmhhnggmumzlpnozjlktrwtusqphumkpltgwszsjwgsvxjqsefrhczelgvczzypzmbzocbtkhbhcwtpziylfkpinjqipidbvp"

output4 = 956


print("approach1",append_C_S(s4,t4))


print("approach2",append_s_t_method(s4, t4))
