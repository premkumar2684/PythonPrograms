from functools import reduce
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

def getnondev(employees):
    return employees['dept']!='developer'

nondev=list(filter(getnondev,employees))
print(nondev)

def getnondevsalary(employees):
    return employees['salary']

nondevsumsalary= list(map(getnondevsalary,nondev))
print(nondevsumsalary)

def getsumofnondevsalary(acc,x):
    return acc+x

sumofnondevsalry= reduce(getsumofnondevsalary,nondevsumsalary)
print(sumofnondevsalry)