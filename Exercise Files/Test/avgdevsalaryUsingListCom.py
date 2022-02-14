employees = [
    {
        'name':'prem',
        'salary':100000,
        'dept':'testing'

    },
    {
        'name':'Jash',
        'salary':200000,
        'dept':'developer'
    },
    {
    'name': 'Kathy',
    'salary': 120000,
    'dept': 'executive'
}, {
    'name': 'Anna',
    'salary': 100000,
    'dept': 'developer'
}, {
    'name': 'Dennis',
    'salary': 95000,
    'dept': 'developer'
}, {
    'name': 'Albert',
    'salary': 70000,
    'dept': 'marketing specialist'
}
    ]

onlydeveloper = [x for x in employees if x['dept']=='developer']
print(onlydeveloper)
def getsalary(onlydeveloper):
    return onlydeveloper['salary']
devsalary = [getsalary(x) for x in onlydeveloper]
print(devsalary)