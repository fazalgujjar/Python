base_salary = 35000
anual_inc = 15000
total_fund = 0
for i in range(1,40):
    if i >=1 and i<=12:
        base_sal = base_salary 
    elif i >=13 and i<=24:
        base_sal = base_salary + (anual_inc)
    elif i >=25 and i<=36:
        base_sal = base_salary + (2*anual_inc)
    elif i >=37 and i<=48:
        base_sal = base_salary + (3*anual_inc)
    prov_fund = base_sal*0.08
    total_fund =total_fund+prov_fund
    
print(total_fund)
    
    