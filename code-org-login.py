"""Example app to login to Code.org"""
import argparse
import mechanicalsoup

parser = argparse.ArgumentParser(description='Login to Code.org')
parser.add_argument("username")
parser.add_argument("password")
parser.add_argument("output")
args = parser.parse_args()

browser = mechanicalsoup.Browser()

login_page = browser.get("https://studio.code.org/users/sign_in")

print(login_page)

login_form = login_page.soup.select("#signin")[0].select("form")[0]

login_form.select("#user_login")[0]['value'] = args.username
login_form.select("#user_password")[0]['value'] = args.password

page2 = browser.submit(login_form, login_page.url)
print(page2)

page3 = browser.get("http://code.org/v2/sections")
print(type(page3))

#salva
with open(args.output,'wb') as f:
    f.write(page3.content)

# desconecta
page4 = browser.get("https://studio.code.org/users/sign_out")

'''
page5 = browser.get("http://code.org/v2/sections")
print(type(page5))
print(page5.content)
'''
