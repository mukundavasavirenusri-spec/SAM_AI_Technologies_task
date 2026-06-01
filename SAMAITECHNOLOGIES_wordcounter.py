string = "The UPSC Civil Services Examination is India’s premier recruitment test for top administrative roles like the IAS and IPS. " \
"Conducted by the Union Public Service Commission, this rigorous three-stage process assesses a candidate's intellectual depth, analytical skills, " \
"and administrative aptitude to serve the nation." \

counts = {}
for word in string.split() :
    counts.setdefault(word,0)
    counts[word] += 1

print(counts)