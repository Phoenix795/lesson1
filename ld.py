# step 5(Комплексные типы данных: списки)
my_list = [3,5,7,9,10.5]
print('My list: ', my_list)
my_list.append('Python')
print('Length of my_list: ', len(my_list))
print('First element: ', my_list[0])
print('Last element: ', my_list[-1])
print('From second to fourth element: ',my_list[1:4])
print('My list: ', my_list)
del my_list[-1]
print('My list after removing: ',my_list)

# step 6(Комплексные типы данных: словари)
my_dictionary = {
    "city": "Москва", 
    "temperature": "20"
    }
print('Name of city: ', my_dictionary.get('city'))
my_dictionary['temperature'] = int(my_dictionary['temperature']) - 5
print('Changed temperature: ', my_dictionary['temperature'])
print('Country key in My dictionary is: ', my_dictionary.get('country'))
print('Default value for country key: ', my_dictionary.get('country', 'Россия'))
my_dictionary['date'] = "27.05.2019"
print('Length of My dictionary: ', len(my_dictionary))
