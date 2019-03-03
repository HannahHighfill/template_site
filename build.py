#pages = [
#    {
#    "filename": "content/index.html",
#    "output": "docs/index.html",
#    "title": "About Me",
#    },
#    {
#    "filename": "content/projects.html",
#    "output": "docs/projects.html",
#    "title": "My Projects",
#    },
#    {
#    "filename": "content/blog.html",
#    "output": "docs/blog.html",
#    "title": "My blog",
#    },
#]
#    

import glob
all_html_files = glob.glob("content/*.html")
print(all_html_files)

import os

file_path = "content/blog.html"
file_name = os.path.basename(file_path)
print(file_name)
name_only, extension = os.path.splitext(file_name)
print(name_only)


pages = []
pages.append({
    "filename": "content/index.html",
    "title": "Index",
    "output": "docs/index.html",
})

def main():
    for page in pages:
        top = open('templates/top.html').read()
        middle = open(page['filename']).read()      
        bottom = open('templates/bottom.html').read()
        combined = top + middle + bottom
        open(page["output"],"w+").write(combined)    
    
print("Built!")
    
    
if __name__== "__main__":
    main()

print("again")
