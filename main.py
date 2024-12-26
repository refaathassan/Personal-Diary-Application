from datetime import datetime
def add_entity(notes,time=False):
    try:
        file=open("diary.txt","a")
        file.write(notes+"\t"+datetime.now().strftime('%Y-%m-%d %H:%M:%S')+"\n")
        file.close()
    except FileNotFoundError as e:
        print(e)
    except PermissionError as e:
        print(e)

def display_entities():
    try:
        file=open("diary.txt","r")
        line=file.read()
        file.close()
        print(line)
    except FileNotFoundError as e:
        print(e)
    except PermissionError as e:
        print(e)
add_entity("refaat",True)
display_entities()