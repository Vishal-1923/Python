# *********************************************** Regular Expressions ******************************************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/blob/main/95-Day-95-Regular-Expressions/.tutorial/01-regularExpressions.md

# Regular Expressions should not be used for basic matching.

# to use Regular expression, one should import re package (built-in)

import re
pattern = "was" #now i want to search for small-letter ife i.e., wife or life
pattern = r"[a-z]ife" #r"" is raw string [] represents class of characters jaisseki small a se small z s start hona chahiye
text = '''
Modern humans arrived on the Indian subcontinent from Africa no later than 55,000 years ago.[22][23][24] Their long occupation, initially in varying forms of isolation as hunter-gatherers, has made the region highly diverse, second only to Africa in human genetic diversity.[25] Settled life emerged on the subcontinent in the western margins of the Indus river basin 9,000 years ago, evolving gradually into the Indus Valley Civilisation of the third millennium BCE.[26] By 1200 BCE wife, an archaic form of Sanskrit, an Indo-European language, had diffused into India from the northwest.[27][28] Its evidence today is found in the hymns of the Rigveda. Preserved by an oral tradition that was resolutely vigilant, the Rigveda records the dawning of Hinduism in India.[29] The Dravidian languages of India were supplanted in the kife and western regions.[30] By 400 BCE, fife and exclusion by caste had emerged within Hinduism,[31] and Buddhism and Jainism had arisen, proclaiming social orders unlinked to heredit
'''
# match = re.search(pattern, text) #ye pehle match p hi ruk jaaega 
# print(match) #it will just tell ki was paya gya hai

matches = re.finditer(pattern, text)
for match in matches:
    # print(match)
    print(match.span())
    print(text[match.span()[0]:match.span()[1]])#match.span()[0]:starting idx of matched substring


# https://regexr.com/