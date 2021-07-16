import re

mystr = '''Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +44 (20) 7235 8281
Fax: +44 (20) 7235 8727
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions: View map

Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: 
+91 7032439787
+91 7042438007
+91 9032439057
+91 8152439852
+91 8052228899
Fax: +1 (703) 243 9791
66-66
455-4545
Email: northamerica@tata.com 
Website: www.northamerica.tata.com
Directions: View map fass
aiaiiiiiiiiiiiaiiaiaiiaiiiiiiiiaaaaaiaaaiiiiiiiiiiiiai'''

# pattern = re.compile(r'Suite')
# pattern = re.compile(r'\ dir')
# pattern = re.compile(r'.dir')
# pattern = re.compile(r'^Tata')
# pattern = re.compile(r'fass$')
# pattern = re.compile(r'fass$')
# pattern = re.compile(r'ai*')
# pattern = re.compile(r'a*i*')
# pattern = re.compile(r'a*i')
# pattern = re.compile(r'ai+')
# pattern = re.compile(r'a+i')
# pattern = re.compile(r'a+i+')
# pattern = re.compile(r'a{2}i{1}')
# pattern = re.compile(r'a{2}i+')
# pattern = re.compile(r'a{2}i*')
# pattern = re.compile(r'ai{2}')
# pattern = re.compile(r'(ai){2}')
# pattern = re.compile(r'(ai){1}|t')
# pattern = re.compile(r'(ai){2}|Fax')
# pattern = re.compile(r'\ATata')
# pattern = re.compile(r'ai\b')
# pattern = re.compile(r'ai\B')
# pattern = re.compile(r'\b91')
# pattern = re.compile(r'\d{5}-\d{4}')
pattern = re.compile(r'\b91 \d{10}')





matches = pattern.finditer(mystr)
l1 = []
i=0
for match in matches:
    print(match)
    i += 1
print(i)
j = 307
for num_list in range(i):
    k = j + 14
    l1.append(mystr[j:k])
    j = k+1

print(l1)