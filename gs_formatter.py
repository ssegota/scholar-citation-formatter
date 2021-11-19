# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 11:50:31 2021

@author: ssego
"""

class Entry():
    pub_type=-1
    authors=""
    title=""
    pub=""
    year=""
    def __init__(self, pub_type, authors, title, pub, year):
        self.pub_type=pub_type
        
        self.title=title
        self.pub=pub
        self.year=year
        
        authors_split = authors.split(";")
        authors_split.pop()
        print(authors_split)
        new_author_string=""
        for author in authors_split:
            print(author)
            first_last=author.split(",")
            print(first_last)
            new_author_string+=first_last[0]+", "
            new_author_string+=first_last[1][1]
            new_author_string+=" et al."
            break
            
        self.authors=new_author_string
    
    def printer(self):
        return str(self.authors)+": "+str(self.title)+"; in "+str(self.pub)+", "+str(self.year)[:-2]


import pandas as pd

df = pd.read_csv("citations(2).csv", encoding_errors='ignore')

for i in df:
    print(i)

entries = []
for index, row in df.iterrows():
    ph=Entry(row["Type"], row["Authors"], row["Title"], row["Publication"], row["Year"])
    entries.append(ph)
    

conferences = []
journals_wos = []
journals_wos_d=[]
journals = []
books = []

"""
0 - Other, skip
1 - Journal, unindexed
2 - Conference
3 - Journal, indexed, WoS
4 - journal, indexed, domestic
5 - Book Chapter
"""
for e in entries:
    if e.pub_type==1:
        journals.append(e)
    elif e.pub_type==2:
        conferences.append(e)
    elif e.pub_type==3:
        journals_wos.append(e)
    elif e.pub_type==4:
        journals_wos_d.append(e)
    elif e.pub_type==5:
        books.append(e)
        
#sort
sort=True
if sort:
    journals_wos.sort(key=lambda x: x.year, reverse=True)
    journals_wos_d.sort(key=lambda x: x.year, reverse=True)
    journals.sort(key=lambda x: x.year, reverse=True)
    conferences.sort(key=lambda x: x.year, reverse=True)
    books.sort(key=lambda x: x.year, reverse=True)

#write
        
file=open("Formatted list.txt", "w", encoding="utf-8")

file.write("Publications for Sandi Baressi Šegota\n\n")
file.write("Journals, indexed in Web of Science\n\n")
for entry in journals_wos:
    file.write(entry.printer()+"\n")
file.write("\n\nJournals, indexed in Web of Science, domestic\n\n")
for entry in journals_wos_d:
    file.write(entry.printer()+"\n")
file.write("\n\nJournals, other\n\n")
for entry in journals:
    file.write(entry.printer()+"\n")
file.write("\n\nConference proceedings\n\n")
for entry in conferences:
    file.write(entry.printer()+"\n")
file.write("\n\nBook chapters\n\n")
for entry in books:
    file.write(entry.printer()+"\n")
file.close()