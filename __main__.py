import csv
def add_book():
  print("BOOK TITLE\nExample: Learning Python")
  while True:
      title = input("Input:")
      if title != '':
          break
      else:
          print("Please enter a title: ")
  print("\n\n\n")
  print("BOOK AUTHOR\nExample: Mark Lutz")
  while True:
      author = input("Input:")
      if author != '':
          break
      else:
          print("Please enter a author: ")
  print("\n\n\n")
  print("ISBN13\nExample: 9871449355730")
  while True:
      ISBN = input("Input: ")
      if ISBN.isdigit() and len(ISBN)==13:
        break
      else:
         print("Sorry, ISBN13 please.")
  print("\n\n\n")
  print("PUBLISHER\nExample: O´Reilly and Associates")
  while True:
      publisher = input("Input:")
      if publisher != '':
          break
      else:
          print("Sorry, you didn´t enter a publisher.")
  print("\n\n\n")
  print("EDITION, YEAR\nExample: 1st edition, 2013")
  while True:
      editionyear = input("Input:")
      if editionyear != '':
          break
      else:
          print("Sorry, you must enter as \n Example: 1st edition, 2013: ")
  print("\n\n\n")
  print("PAGES\nExample: 1591")
  while True:
      pages = input("Input:")
      if pages != '' and pages.isdigit():
          break
      else:
          print("Sorry, you must enter as \n Example: 1st edition, 2013: ")
  print("\n\n\n")
  print("Keyword\nExample: Scifi")
  while True:
      keyword = input("Input:")
      if keyword != '':
          break
      else:
          print("Sorry, you must enter as \n Example: Scifi: ")
  print('\n')
  with open('library.csv', 'a', newline='') as f:
      headers_list = ['Title', 'Author', 'ISBN', 'Publisher', 'Edition, year', 'Pages', 'Keyword']
      csv_writer = csv.DictWriter(f, fieldnames = headers_list, delimiter = '|')
      csv_writer.writerow({'Title' : title, 
                           'Author' : author, 
                           'ISBN' : ISBN, 
                           'Publisher' : publisher, 
                           'Edition, year' : editionyear,
                           'Pages' : pages, 
                           'Keyword' : keyword})
      

def show_keywords():
    keyword_list=[]
    with open('library.csv', 'r', encoding="utf-8") as f:
        csv_reader = csv.DictReader(f, delimiter = '|')
        for row in csv_reader:
            if row['Keyword'] not in keyword_list:
                keyword_list.append(row['Keyword'])
        for temp in keyword_list:
            print('Keyword: ', temp, sep = '')
    print('\n')


def show_library():
    keyword_list=[]
    with open('library.csv', 'r', encoding="utf-8") as f:
        csv_reader = csv.DictReader(f, delimiter = '|')
        for row in csv_reader:
            if row['Keyword'] not in keyword_list:
                keyword_list.append(row['Keyword'])
    for elem in keyword_list:
        print('\nKeyword ', elem, ':\n', sep='')
        with open('library.csv', 'r', encoding="utf-8") as f:
                csv_reader = csv.DictReader(f, delimiter = '|')
                for row in csv_reader:
                    if elem == row['Keyword']:
                        print(row['Title'], ' - ', row['Author'], '; ', 'ISBN: ', row['ISBN'], '; ', 'Publisher: ', row['Publisher'], '; ', 'Edition, year: ', row['Edition, year'], '; ', 'Pages: ', row['Pages'], '.', sep='')
    print('\n')


def search_by_keyword():
    temp = 0
    kw = input('Input searchable keyword: ')
    with open('library.csv', 'r', encoding="utf-8") as f:
        csv_reader = csv.DictReader(f, delimiter = '|')
        for row in csv_reader:
            if kw.lower() == row['Keyword'].lower():
                temp+=1
    if temp>0:
        print('Number of entries for this keyword: ', str(temp), '.\nDo you want to view this Y/N: ', sep='')
        while True:
            temp1 = input()
            if temp1 == 'Y' or temp1 == 'y':
                with open('library.csv', 'r', encoding="utf-8") as f:
                    csv_reader = csv.DictReader(f, delimiter = '|')  
                    for line in csv_reader:
                        if kw.lower() == line['Keyword'].lower():
                            print('Title: ', line['Title'], '; ', 'Author: ', line['Author'], '; ', 'ISBN: ', line['ISBN'], '; ', 'Publisher: ', line['Publisher'], '; ', 'Edition, year: ', line['Edition, year'], '; ', 'Pages: ', line['Pages'], '.', sep='')
                    break
            elif temp1 == 'N' or temp1 == 'n':
                break
            else:
                print('Please enter Y or N: ')
    else:
        print('Number of entries for this keyword: 0')
    print('\n')
    
                            
with open('library.csv', 'w', newline='', encoding="utf-8") as f:
    headers_list = ['Title', 'Author', 'ISBN', 'Publisher', 'Edition, year', 'Pages', 'Keyword']
    csv_writer = csv.DictWriter(f, fieldnames = headers_list, delimiter = '|')
    csv_writer.writeheader()


while True:
    print('1. Enter book\n2. Show keywords\n3. Show library info\n4. Search by keyword\n')
    action = input('Choose an action: ')
    if action == '1':
        add_book()
    elif action == '2':
        show_keywords()
    elif action == '3':
        show_library()
    elif action == '4':
        search_by_keyword()
    else:
        print('Exiting application...')
        break
        
    