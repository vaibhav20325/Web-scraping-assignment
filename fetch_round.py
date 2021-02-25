from selenium import webdriver
import os
import sys

c_no=sys.argv[1]
q_no=[]
try:
    parent_dir='./'+c_no
    os.mkdir(parent_dir)
except:
    pass

PATH = '.\chromedriver.exe'
driver=webdriver.Chrome(PATH)

#Finding number of contest questions
driver.get("https://codeforces.com/contest/"+c_no)
table=driver.find_element_by_class_name("problems")
rows=table.find_elements_by_tag_name("tr")
for i in range(1,len(rows)):
    q_no.append(rows[i].find_element_by_tag_name('a').text)


for i in range(len(q_no)):
    p_no=q_no[i]
    current_dir=parent_dir+'/'+p_no
    try:
        os.mkdir(current_dir)
    except:
        pass
    driver.get("https://codeforces.com/problemset/problem/"+c_no+"/"+p_no)

    driver.save_screenshot(current_dir+"/problem.png")

    inputs=driver.find_elements_by_class_name("input")
    for input in inputs:
        text=input.find_element_by_tag_name("pre").text
        file_name='/input'+str(inputs.index(input)+1)+'.txt'
        f=open(current_dir+file_name,'w')
        f.write(text)
        f.close()
    
    outputs=driver.find_elements_by_class_name("output")
    for output in outputs:
        text=output.find_element_by_tag_name("pre").text
        file_name='/output'+str(outputs.index(output)+1)+'.txt'
        f=open(current_dir+file_name,'w')
        f.write(text)
        f.close()

driver.quit()


