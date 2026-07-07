import json

def view():
    with open('bookmarks.json', 'r', encoding='utf-8') as file:
        bookmarks_db = json.load(file)
    for i in bookmarks_db:
        for key, value in i.items():
            print(f"{key}, {value}")

def Add():
    name= input("Enter name ")
    url= input("Enter URL ")
    new_book= {name : url}
    with open('bookmarks.json','r', encoding='utf-8') as rfile:
        bookmarks_db = json.load(rfile)
    bookmarks_db.append(new_book)
    with open('bookmarks.json','w', encoding='utf-8') as wfile:
        json.dump(bookmarks_db,wfile)
    print("New bookmark added")
 
def remove():
    del_by_name=input("enter name of website you want to delete ")
    with open('bookmarks.json','r', encoding='utf-8') as rfile:
        bookmarks_db = json.load(rfile)
    for i in range(0,len(bookmarks_db)):
        if del_by_name in bookmarks_db[i]:
            bookmarks_db.pop(i)
            break
    with open('bookmarks.json','w', encoding='utf-8') as wfile:
        json.dump(bookmarks_db,wfile)
    print("bookmark deleted")




def edit():
    print("this bookmark edited")