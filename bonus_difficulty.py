from selenium import webdriver
import os
import sys

n = int(input('Enter number of questions: '))
n1 = int(input('Enter lower bound: '))
n2 = int(input('Enter upper bound: '))

PATH = '..\chromedriver.exe'
driver=webdriver.Chrome(PATH)

q_code=[]
rows=[]

def row_generator(page_no):
    driver=webdriver.Chrome(PATH)
    driver.get("https://codeforces.com/problemset/page/"+str(page_no)+"?tags="+str(n1)+"-"+str(n2))
    problem_table=driver.find_element_by_class_name("problems")
    r=problem_table.find_elements_by_tag_name("tr")[1:]
    rows.extend(r)
    if len(rows) >= n:
        pass
    else:
        try:
            row_generator(page_no+1)
        except:
            print('So many problems aren\'t available in this range')

row_generator(1)

rows=rows[0:n]

for row in rows:
    contest_no = row.find_element_by_tag_name("a").text[0:4]
    question_no = row.find_element_by_tag_name("a").text[4:]
    q_code.append((contest_no,question_no))

def scrape(x):
    c_no,p_no = x
    parent_dir = './'
    current_dir = parent_dir + c_no + '_' + p_no
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
    
for i in q_code:
    scrape(i)

driver.quit()