fname = "day19/input.txt"
with open(fname) as f:
    replacements = f.readlines()
replacements = [x.split() for x in replacements if x != '=>']

word = "CRnSiRnCaPTiMgYCaPTiRnFArSiThFArCaSiThSiThPBCaCaSiRnSiRnTiTiMgArPBCaPMgYPTiRnFArFArCaSiRnBPMgArPRnCaPTiRnFArCaSiThCaCaFArPBCaCaPTiTiRnFArCaSiRnSiAlYSiThRnFArArCaSiRnBFArCaCaSiRnSiThCaCaCaFYCaPTiBCaSiThCaSiThPMgArSiRnCaPBFYCaCaFArCaCaCaCaSiThCaSiRnPRnFArPBSiThPRnFArSiRnMgArCaFYFArCaSiRnSiAlArTiTiTiTiTiTiTiRnPMgArPTiTiTiBSiRnSiAlArTiTiRnPMgArCaFYBPBPTiRnSiRnMgArSiThCaFArCaSiThFArPRnFArCaSiRnTiBSiThSiRnSiAlYCaFArPRnFArSiThCaFArCaCaSiThCaCaCaSiRnPRnCaFArFYPMgArCaPBCaPBSiRnFYPBCaFArCaSiAl"

possibilities = []
for replacement in replacements:
    find = replacement[0]
    replace = replacement[2]

    for i in range(len(word)-len(find)+1):
        if word[i:i+len(find)] == find:
            new_word = word[:i] + replace + word[i+len(find):]
            # print(new_word)
           
            if new_word not in possibilities:
               possibilities.append(new_word)

print(len(possibilities))

# print(content)