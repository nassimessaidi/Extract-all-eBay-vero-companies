#from subprocess import check_output

#output = check_output('dir', shell=True).decode()
import subprocess
try:
    import requests
    import os
    from bs4 import BeautifulSoup
    print("Please wait a seconds...")
except:
    required_libs = "pip install requests bs4"
    print("Please wait a seconds...")
    import subprocess
    process = subprocess.Popen(required_libs,
                               shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)

    result = [line for line in process.stdout]
    errcode = process.returncode
    if errcode is not None:
        raise Exception('cmd %s failed, see above for details', required_libs)


URL = "https://pages.ebay.com/seller-center/listing-and-marketing/verified-rights-owner-program.html#m17-1-tb3"

res = requests.get(URL)
soup = BeautifulSoup(res.content, "html.parser")

# get the tag of html who has the vero name company
vero_companies_html_tags = soup.find_all('a', attrs={'class': 'gaLnkTrk'})

# get the vero companies as a string
companies = [company.text for company in vero_companies_html_tags[42:-27]]

# save the cvero mopanies in a file called vero_companies.txt
filename = "vero_companies.txt"
with open(filename, 'w') as f:
    for company in companies:
        f.write(company + '\n')

companies_number = len(companies)
current_directory = os.getcwd()
file_directory = os.path.join(current_directory, filename)
print(f'\nAll {companies_number} companies are saved in: \n{file_directory}\n')
