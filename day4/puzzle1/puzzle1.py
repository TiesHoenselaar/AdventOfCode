string = "vxupkizork-sgmtkzoi-pkrrehkgt-zxgototm-644[kotgr]"
string2 = "aaaaa-bbb-z-y-x-123[abxyz]"

string = string2

checksum = string.split("[",)[1][:-1]
sectorID = int(string.split("[",)[0].split("-")[-1])
name = ''.join(sorted(''.join(string.split("[",)[0].split("-")[0:-1])))


print("checksum:\t{0}".format(checksum))
print("sectorID:\t{0}".format(sectorID))
print("name:\t\t{0}".format(name))

print(name.count('a'))