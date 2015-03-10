"""Example app to signup Codeorg"""
import argparse
import mechanicalsoup

parser = argparse.ArgumentParser(description='Login to Code.org')
parser.add_argument("email")
parser.add_argument("password")
args = parser.parse_args()

browser = mechanicalsoup.Browser()

login_page = browser.get("http://studio.code.org/users/sign_up?user%5Buser_type%5D=teacher")

print(login_page)

login_form = login_page.soup.select("#signup")[0].select("form")[0]

login_form.select("#user_name")[0]['value'] = args.email.split('@')[0]
login_form.select("#user_email")[0]['value'] = args.email
login_form.select("#user_password")[0]['value'] = args.password
login_form.select("#user_password_confirmation")[0]['value'] = args.password
login_form.select("#user_school")[0]['value'] = "Programaê!"

page2 = browser.submit(login_form, login_page.url)
print(page2)

# desconecta
page3 = browser.get("https://learn.code.org/users/sign_out")
print("logout",page3)
