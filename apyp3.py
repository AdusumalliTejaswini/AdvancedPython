def computesalary(basic,grade):
    hra=0.2*basic
    da=0.5*basic
    pf=0.11*basic
    if grade=='A':
        allowance=1700.0
    elif grade=='B':
        allowance=1500.0
    else:
        allowance=1300.0
    gross=round(basic+hra+da+allowance-pf)
    return gross
basic=10000
grade='A'
print(computesalary(basic,grade));