import requests
import re
def verifyaddress(address_list):
    pattern = '\d{6}' #indian pincode pattern - 6 consecutive digits
    valid_address_list = []
    for address in address_list:
        if not re.search(pattern,address):
            valid_address_list.append('incorrect address') #to check if the address has a pincode
            continue
        pincode = (re.findall(pattern,address))[0]
        url = f'https://api.postalpincode.in/pincode/{pincode}'
        res = requests.get(url) #retrieving data from API
        json = res.json()
        postoffices = json[0]['PostOffice']
        status = json[0]['Status']
        if status == "Error": #finding if it's a valid pincode
            valid_address_list.append('incorrect address')
        else:
            for office in postoffices: #checking if the address is valid using postoffice name
                if office['Name'] in address:
                    valid_address_list.append('correct address')
                    break
            else:
                valid_address_list.append('incorrect address')
    return valid_address_list
            
            
    

n = int(input())
address_list = []
for index in range(n):
    address = input()
    address_list.append(address)
print(verifyaddress(address_list))

'''
Test cases are

1. 2nd Phase, 374/B, 80 Feet Rd, Mysore Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bengaluru, Karnataka 560050  - correct address
2. 2nd Phase, 374/B, 80 Feet Rd, Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bengaluru, Karnataka 560050 - correct address
3. 374/B, 80 Feet Rd, State Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bangalore. 560050 - correct address
4. 2nd Phase, 374/B, 80 Feet Rd, Mysore Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bengaluru, Karnataka 560095 - incorrect address
5. Colony, Bengaluru, Karnataka 560050 - incorrect address
'''
