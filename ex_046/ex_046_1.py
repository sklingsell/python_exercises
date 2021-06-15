var_1,var_2,var_3=1,2,3
print(var_2)

var_temp=var_2
var_2=var_1
var_1=var_temp

print(var_temp,var_2,var_1)

var_2,var_1=var_1,var_2
print(var_2,var_1)