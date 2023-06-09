#https://www.codingninjas.com/codestudio/problems/compare-version-numbers_8230793?challengeSlug=striver-sde-challenge

def compareVersions(v1, v2):
    v1_parts = list(map(int, v1.split('.')))
    v2_parts = list(map(int, v2.split('.')))

    length = max(len(v1_parts), len(v2_parts))

    for i in range(length):
        rev1 = v1_parts[i] if i < len(v1_parts) else 0
        rev2 = v2_parts[i] if i < len(v2_parts) else 0

        if rev1 == rev2:
            continue
        return -1 if rev1 < rev2 else 1

    return 0
  
#i splitted each version at '.' and i checked all the numbers respectively in a loop
