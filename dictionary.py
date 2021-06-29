# dictionaries are built in data types available with python
# defining dictionaries in python
employee = {'name': 'Joseph', 'age': 30, 'departments': ['Development', 'Testing']}

#print(employee)

# access value by referencing key index
#print(employee['salary'])

# try to access a key which does not exist
#print(employee['designation'])

# access value with  get method

#employee['designation'] = 'Engineer'
#print(employee.get('designation','Not found'))
#employee['designation'] = 'Engineer'
#print(employee)

# updating multiple values in dictionary (update method)
#employee.update({'name':'John','age' : 27,'departments':['Development','Testing'],'designation':'Senior Engineer'})
#print(employee)

# delete using del

#del employee['age']
#print(employee)

# delete using pop method

#departments = employee.pop('departments')
#print(departments)
#print(employee)
#print(employee)

# find length of dictionary
#print(len(employee))

# access only keys from dictionary using keys() method
#print(employee.keys())

# access only values from dictionary using values() method

#print(employee.values())

# access both keys and values using items() method

#print(employee.items())

#for key, value in employee.items():
  # print(key,value)

# sorting on dictionaries based on key

#print(sorted(employee))

# check presence of key in dictionary
print('name' in employee)