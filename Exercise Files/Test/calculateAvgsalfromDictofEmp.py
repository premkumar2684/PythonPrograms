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





#list(filter(lambda x:x%2==0, number))
#print(list(filter(findEven,number)))
def finddev(employees):
    return employees['dept']=='developer'
   
onlydevelper=list(filter(finddev,employees))
#print(onlydevelper)
def findsalarydev(employees):
    return employees['salary']
devsalary= list(map(findsalarydev,onlydevelper))
print(devsalary)   
#print(sum(devsalary)/len(onlydevelper))
def get_sum(acc,x):
    return acc + x

totalsal= reduce(get_sum,devsalary)
print(totalsal)