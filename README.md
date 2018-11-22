# News Reporting
- Database is posgresql database.
- Database is called news and consists of three table("articles","log","authors")
## Installation
  1- Install Virtual Machine(VirtualBox).
  2- Install Vagrant.
  3- Install git.
  4- Download FSND-Virtual-Machine.
  5- download database https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
## Commands 
- "vagrant up".
- "vagrant ssh".
- "psql news".
## Code consist of :
- connection with database.
- queries which show reporting of news.
# Queries
1-  What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.
2-  Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.
3- On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser.
# The way to open the project
### After installing vm and vagrant
 - open bash git 
 - then writting this is command "cd Downloads/FSND-Virtual-Machine/Vagrant/"
 - then writting this is command "vagrant up" for install vm .
 - then writting this is command "vagrant ssh"
 - for running queries from database "psql -d news -f newsdata.sql"
 - for running file python "python news.py".
