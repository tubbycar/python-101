def transform_poly(list):
    new_list=[]
    for i, item in enumerate(list):
        power=int(len(list)-i-1)
        new_list.append((item,power))
    return new_list
    
def multiply(orig_set):
    data_set=[]
    for data in orig_set:
        data=transform_poly(data)
        data_set.append(data)
    if [0] in orig_set:
        return [0]
    if len(orig_set)==1:
        return orig_set
    else:
        to_sum=[]
        for item in data_set[0]:
            for var in data_set[1]:
                new_var_coeff=item[0]*var[0]
                new_var_power=item[1]+var[1]
                new_var=(new_var_coeff,new_var_power)
                to_sum.append(new_var)
        power_list=[]
        for tup in to_sum:
            if tup[1] not in power_list:
                power_list.append(tup[1])
        return_list=[]
        for i in range(power_list[0],-1,-1):
            def_coeff=0
            for item in to_sum:
                if item[1]==i:
                    def_coeff+=item[0]
            return_list.append(def_coeff)
        recur_list=[]
        recur_list.append(return_list)
        orig_set=orig_set[2:]
        recur_list=recur_list+orig_set
        return multiply(recur_list)
