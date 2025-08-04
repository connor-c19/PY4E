# Web Services Basics

- There is a need to send/retreive information that is made for programmatic consumption

- Protocol (wire protocol): a format that multiple programs can use to transmit data

  - serialize: data structure agnostic data coversion
  - deserialize: convert info into native data structure

  - XML, JSON are used
    - XML: Older, more precise
    - JSON: Newer, more prevalent

# XML

## Basics

- Extensible Markup Language, used to help information systems share structured data

- Tags: indicate the beginning and ending of elements, can be named anything we choose

  - Can have attributes: <phone type = ""intl>xxx-xxx-xxxx</phone>

- Tags can have children or parents
  -There must be one master parent tag

## Schema

- A **validator** acts as a contract between two endpoints that validates the agreed-upon XML schema. An example of an XML schema is XSD structure:

```
<xs:complexType name="person">
  <xs:sequence>
    <xs:element name="lastname" type="xs:string"/>
    <xs:element name="age" type="xs:int"/>
    <xs:element name="dateborn" type="xs:date"/>
  </xs:sequence>
</xs:complexType>
```

- Constraints can be added to indicate how many times a sequence should happen

- Date/Time format:
  `YYYY-MM-DD`T`HH:MM:SS`Z`

## Defining XML in Python

```
import xml.etree.ElementTree as ET
data = '''
<person>
  <name>Chuck</name>
  <phone type ="intl">
    +1 XXX XXX XXXX
  </phone>
  <email hide="yes"/>
<person>
'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))
```

```
import xml.etree.ElementTree as ET
data = '''<stuff>
  <users>
    <user x="2">
      <id>001</id>
      <name>Chuck</name>
    </user>
    <user x="7">
      <id>009</id>
      <name>Brent</name>
    </user>
  </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count:', len(lst))
for item in lst:
  print("Name",item.find('name').text)
  print("ID",item.find('id').text)
  print("Attr",item.get('x'))
```

# JSON

- Best for sending simple data over the web without much 'fuss'

- Structure is much simpler in Python, always represented as a dictionary or list

```
import json
data = '''{
  "name" : "Chuck"
  "phone" : {
    "type" : intl,
    "number" : "+1 xxx xxx xxxx"
  },
  "email" : {
    "hide" : "yes"
  }
}'''

info = json.loads(data)
print("Name: ", info['name'])
print("Hide: ", info['email']['hide'])
```

# Service Oriented Approach

- Most non-trivial web applications use services from other applications

- Services publish the "rules" using APIs

## Web services

- An Application Program Interface is an interface that defines and controls how services can be consumed by other services

- Example of using Google Maps API:

```
import urlllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://py4e-data.dr-chuck.net/json?'

while(True):
  address = input('Enter location: ')
  if len(address) < 1: break

  url = serviceurl + urllib.parse.urlencode({'address': address})

  print('Retrieving', url)

  uh = urllib.request.urlopen(url)
  data = uh.read().decode()
  print('Retrieved', len(data), 'characters')

  try:
    js = json.loads(data)
  except:
    js = None

  if not js or 'status' not in js or js['status'] != 'OK':
    print('==== Failure to Retrieve ====')
    print('data')
    continue

  lat = js['results'][0]["geometry"]["location"]["lat"]
  lng = js['results'][0]["geometry"]["location"]["lng"]
  print("Lat: ", lat, "Lng: ", lng)
  location = js['results'][0]["formatted_address"]
  print(location)


```
