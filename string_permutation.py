def string_permutation(temp_list):
    if len(temp_list) == 1:
        return temp_list[0]
    else:
        a =set()
        for obj in temp_list:
            res=string_permutation(temp_list.replace(obj,'',1))
            for x in res:
                a.add(obj+x)
        return a
            

print(string_permutation('abc'))
