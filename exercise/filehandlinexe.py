#here we were ask to read an exateranal json file and query trough its data
import json
def readfile(filename,nCountries):
    try:
        with open(filename, encoding='utf-8') as f:
            countries = json.load(f)
    except FileNotFoundError:
        print('File not found')
    
    langArrOfArr = list(map(lambda pay: pay['languages'],countries)) #here we are mapping the langusge item into an array
    langlst= [i for row in langArrOfArr for i in row]
    langset = set(langlst) #here we eliminate repition by converitng the array into a set
    print(f'number of languages : {len(langset)}')
    final = []
    for language in langset:
        final.append({'lang' : language, 'count': int(langlst.count(language))}) #to push the dictionary of country and occurence
    final.sort(key=lambda x: x['count'], reverse=True) #sort the array of dictionaries

    return final[0:nCountries] #slice to return 10 most spoken language
print(readfile(filename='C:/Users/awaki/Desktop/30_days/30-Days-Of-Python2/data/countries_data.json',nCountries=10))

