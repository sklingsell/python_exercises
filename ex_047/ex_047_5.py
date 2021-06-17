values = [1,3,4,7,9,14,44,2,77,39,51,20,99,45,8]
alpha = 0.7

def quantile(series,alpha):
    sorted_values = sorted(series)

    lower_idx = round(len(series)*alpha/2)
    upper_idx = round(len(series)*(1-alpha/2))-1

    return(lower_idx,upper_idx)

print(quantile(values,alpha))