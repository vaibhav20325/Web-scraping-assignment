# Web-scraping-assignment
##Vaibhav Agarwal

##2020CS50447

The chromedriver.exe given is for windows please ensure that you are using the right version which matches with your chrome browser version.
The .exe file should be present in this folder

####Task 1

After running the script Enter your details and it would automatically login to moodle.

####Task 2

run python fetch_round.py <contest_no> to scrape the problems of that contest

####Bonus task 1 is by the name **past_contests.py**

After running the script enter the number of past contests you want to scrape.

####Bonus task 2 is by the name **scrape_by_difficulty.py**

After running the script enter the number of questions you want to scrape, the lower bound and the upper bound. If the number of problems you need is large the program will automatically go to the next page to get more problems and will go on like this till it meets the requirement. If the number of problems you want is greater than the total number of problems available on the site in the given difficulty range then it would scrape all the problems and print an Error in the terminal.
