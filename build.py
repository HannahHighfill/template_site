pages = [
    {
    "filename": "content/index.html",
    "output": "docs/index.html",
    "title": "About Me",
    },
    {
    "filename": "content/projects.html",
    "output": "docs/projects.html",
    "title": "My Projects",
    },
    {
    "filename": "content/blog.html",
    "output": "docs/blog.html",
    "title": "My blog",
    },
]
    
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
