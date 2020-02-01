from selenium import webdriver
from pprint import pprint
import time
a=webdriver.Chrome()
a.get('https://www.zomato.com/dharamshala')
a.find_element_by_xpath("//input[@id='keywords_input']").send_keys("Dinner")
time.sleep(3)
a.find_element_by_xpath("//div[@role='button']").click()
time.sleep(3)
main_list=[]

q=a.find_elements_by_xpath("//div[@class='col-l-4 mtop pagination-number']")
for i in q:
	k=(i.text[10:13])
k= (int(k))
for i in range(k):
	a.get('https://www.zomato.com/dharamshala/restaurants?category=10&page='+str(i+1))

	details={'name':'','location':'','cuisines':'','timing':''}
	peyar=[]
	idam=[]
	sirapu=[]
	rate=[]
	manikoor=[]
	name=a.find_elements_by_xpath("//a[@class='result-title hover_feedback zred bold ln24   fontsize0 ']")
	for i in name:
		peyar.append(i.text)
	address=a.find_elements_by_xpath("//div[@class='col-m-16 search-result-address grey-text nowrap ln22']")
	for i in address:
		idam.append(i.text)
	speciality=a.find_elements_by_xpath("//span[@class='col-s-11 col-m-12 nowrap  pl0']")
	for i in speciality:
		sirapu.append(i.text)
	neram=a.find_elements_by_xpath("//div[@class='col-s-11 col-m-12 pl0 search-grid-right-text ']")
	for i in neram:
		manikoor.append(i.text)

	for i in range(len(peyar)):
		details['name']=peyar[i]
		details['location']=idam[i]
		details['cuisines']=sirapu[i]
		details['timing']=manikoor[i]
		main_list.append(details.copy())
pprint (main_list)
a.quit()	