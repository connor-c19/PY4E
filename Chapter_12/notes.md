# Network Basics

- [Free networking textbook](https://www.net-intro.com)

## TCP/IP and Sockets (Layers 4/5 of OSI)

- TCP (transport control protocol) is built upon IP (internet protocl). Basically provides a nice, reliable connection or 'pipe' to online services

- This TCP/IP connection is composed of two (or more) processes that can both 'talk' and 'listen'. These are known as **sockets**. The internet provides the backbone for this network of 'computers'

- TCP/IP port numbers are essentially extensions for a given socket, making many of them reachable at the same IP address. There is a range of commonly used ports defined [here](https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers)

- Python can be used to make sockets:

  - `import socket`
  - `socket.socket(socket.AF_INET, socket.SOCK_STREAM)`
    - First arg: make a socket that goes across the internet
    - Second arg: stream socket, take in input as one character at a time rather than blocks of text
  - `mysock.connect( ('data.pr4e.org',80) )`
    - First arg: host
    - Second arg: port

- What data can we expect to send/recieve?

## Application Protocols

- HTTP - Hypertext Transfer Protocol

  - Pretty dominant over the internet, lays the rules of the road for sending and receiving web documents

- URL: http://www.dr-chuck.com/page.html

  - http:// - protocol
  - www.dr-chuck.com - host
  - page.html - document

- Web browswer, a process running that creates a socket to connect to and request resources from webservers across the web

  - Also is responsible for rendering retrieved documents into a readable format of the style defined

- Hyperlink (anchor reference): when clicked, requests another page

- Internet standards are determined by the IETF, and post standards in Internet Request For Comments (RFC)
  - Such standards define the rules for how to request (GET) resources from a host

## Building a web browser

- Make a socket in Python
- After connecting, web servers will usually expect the browser to make a request first:

```
  cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
  mysock.send(cmd)
  while True:
    data = mysock.recv(512)
    if (len(data)<1):
      break
    print(data.decode())
  mysock.close()

```

# Text Processing

- ASCII was the first standardization of the binary representation of latin characters

  - `ord()` will reveal the ASCII values for registered characters, ranging from 0-256

- Unicode is the current standardization of binary representation for ALL characters

  - UTF-8: a substandard of unicode which is variable length, allows for all of the unicode characters to be transmitted in 1-4 bytes, depending on the value

- Byte variables: essentialy an array of bytes
  - `x = b'abc'`
  - How data is received over the network

# Helpful Libraries

## Simplifying Sockets with urllib

- The above HTTP operations are so common that a standard library exists to handle web communication:

```
import urllib

# Parameter available to get headers as well as body
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

for line in fhand:
  print(line.decode().strip())

```

## Web scraping with Beautiful Soup

- Web scraping is when a program pretends to be a browswer and retrieves web pages, extracts information from them, and then looks at more web pages

  - Pull data
  - Get your own data with no export capability
  - Monitor a site for new information
  - Create a search engine

- Need to be careful, some websites do not take kindly to web scraping

- Lots of different ways for HTML to be written, which can make parsing web documents consistently extremely difficult. Here's where [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup) comes in

```
import urllib
import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()

## Soup object can have queries run against
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags

tags = soup('a')
for tag in tags:
  print(tag.get('href', None))

```
