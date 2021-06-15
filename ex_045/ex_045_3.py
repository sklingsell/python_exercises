values = [1,3,4,7,9,14,44,2,77,39,51,20,99,45,8]
alpha = 0.7

sorted_values = sorted(values)

lower_idx = round(len(values)*alpha/2)
upper_idx = round(len(values)*(1-alpha/2))-1

print(lower_idx)
print(upper_idx)

print('Lower value: ' + str(sorted_values[lower_idx]))
print('Upper value: ' + str(sorted_values[upper_idx]))