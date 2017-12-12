m = input("您好，请输入...")
print(m)

soup = bs4.BeautifulSoup(res.text, "html.parser")
print(soup)
targets = soup.find_all("div", class_="hd")
for each in targets:
	print(each.a.span.text)