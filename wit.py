from datetime import date
from os import chdir, getcwd, path, mkdir, listdir
from random import choices
from shutil import copytree
from sys import argv




def init():
    origen_path = getcwd()

    try:
        mkdir(path.join(getcwd(), '.wit'))

        chdir(path.join(getcwd(), '.wit'))
        mkdir(path.join(getcwd(), 'images'))
        mkdir(path.join(getcwd(), 'staging_area'))
        staging_area_path  = path.join(getcwd(), 'staging_area')

        print(".wit folder has been created")

    except FileExistsError:
        print(".wit already exsits in this path")

    finally:
        print(f"{'*' * 20}")
        print(f"The content of the path is:")
        chdir(origen_path)
        print(f"{listdir()}")
        

def add():
    origen_path = getcwd()
    copy_path = getcwd()
    back_folders = []

    while '.wit' not in listdir(copy_path):
        print(copy_path.split('\\')[-1])
        print(listdir())
        back_folders += [copy_path.split('\\')[-1]]
        path_list = copy_path.split('\\')[:-1]
        
        if ':' in path_list[-1]:
            print(".wit folder not exsits in this path")
            return None

        copy_path = '\\'.join(path_list)

    chdir(copy_path)
    root_path = getcwd()
        
    print(".wit folder is found!, creating a backup here:")
    chdir(path.join(root_path, '.wit', 'staging_area'))

    while len(back_folders) != 1:
        folder = back_folders.pop()
        try:
            mkdir(path.join(getcwd(), folder))
            chdir(path.join(getcwd(), folder))
        except FileExistsError:
            chdir(path.join(getcwd(), folder))
            continue

    content_path = getcwd()

    try:
        copytree(origen_path, path.join(content_path, back_folders[0]))
        files = []
        for i in listdir(content_path):
            files += [i]
            

        chdir(path.join(root_path, '.wit'))
        with open('add.txt', 'w') as file:
            file.write(f"{origen_path}, {path.join(content_path, back_folders[0])}, {date.today()}, {files}\n")

    except FileExistsError:
        print("There is already a backup...")
    

def commit(message):
    copy_path = getcwd()

    while '.wit' not in listdir(copy_path):
        path_list = copy_path.split('\\')[:-1]
        
        if ':' in path_list[-1]:
            print(".wit folder not exsits in this path")
            return None

        copy_path = '\\'.join(path_list)
        chdir(copy_path)

    print(".wit folder is found!, creating a backup here:")
    root_path = getcwd()

    chdir(path.join(root_path, '.wit'))

    with open('add.txt', 'w') as file:
        file.write('')

    chdir(path.join(root_path, '.wit', 'images'))

    characters = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f']
    commit_id = ''.join(choices(characters, k = 40))

    with open(f"{commit_id}.txt" , 'w') as file:
        file.write(f"parent = None \ndate = {date.today()}\nmessage = {message}")

    copytree(path.join(root_path, '.wit', 'staging_area'), path.join(root_path, '.wit', 'images', commit_id))

    chdir(path.join(root_path, '.wit'))
    with open('references.txt', 'a') as file:
        file.write(f"HEAD = {commit_id}, master = {commit_id}, {copy_path}, {path.join(root_path, '.wit', 'images', commit_id)}\n")


def status():    
    copy_path = getcwd()

    while '.wit' not in listdir(copy_path):
        path_list = copy_path.split('\\')[:-1]
        
        if ':' in path_list[-1]:
            print(".wit folder not exsits in this path")
            return None

        copy_path = '\\'.join(path_list)
        chdir(copy_path)

    print(".wit folder is found!, creating a backup here:")
    root_path = getcwd()

    chdir(path.join(root_path, '.wit'))
    with open('references.txt', 'r') as file:
        commit_id = file.split(" ")[2]

    with open('add.txt', 'r') as file:
        file = file.read()
        files_added = file.split(',')[0]

    changed = None # dont know how to do that
    Untracked = None # dont know how to do that

    print(f"{commit_id}\nChanges to be committed: {files_added}\nChanges not staged for commit {changed}\nUntracked files: {Untracked}")


def checkout(commit_id):
    copy_path = getcwd()

    while '.wit' not in listdir(copy_path):
        path_list = copy_path.split('\\')[:-1]
        
        if ':' in path_list[-1]:
            print(".wit folder not exsits in this path")
            return None

        copy_path = '\\'.join(path_list)
        chdir(copy_path)

    print(".wit folder is found!, creating a backup here:")
    root_path = getcwd()

    chdir(path.join(root_path, '.wit'))
    with open('references.txt', 'r') as file:
        file = file.read()
        for row in file.split('\n'):
            if commit_id in row:
                with open('activated.txt', 'w') as active:
                    active.write(f"{commit_id}\n")
                row_as_list = row.split(',')
                src = row_as_list[2]
                des = row_as_list[3]
                copytree(src, des)
            else:
                print("the commit_id did not find")
        
def graph():
    copy_path = getcwd()

    while '.wit' not in listdir(copy_path):
        path_list = copy_path.split('\\')[:-1]
        
        if ':' in path_list[-1]:
            print(".wit folder not exsits in this path")
            return None

        copy_path = '\\'.join(path_list)
        chdir(copy_path)

    print(".wit folder is found!, creating a backup here:")
    root_path = getcwd()

    chdir(path.join(root_path, '.wit', 'images'))

    for i in listdir():
        if '.txt' in i:
            with open (i, 'r') as file:
                file = file.read()
                row = file.split('\n')[0]
                parent = row.split("=")[1].strip()
                print(f"parent = {parent} of file {i}")


def branch(name, commit_id):
    copy_path = getcwd()

    while '.wit' not in listdir(copy_path):
        path_list = copy_path.split('\\')[:-1]
        
        if ':' in path_list[-1]:
            print(".wit folder not exsits in this path")
            return None

        copy_path = '\\'.join(path_list)
        chdir(copy_path)

    print(".wit folder is found!, creating a backup here:")
    root_path = getcwd()

    chdir(path.join(root_path, '.wit'))
    with open('activate.txt', 'r') as file:
        file = file.read()
        for i in file.split('\n'):
            if commit_id in i:
                characters = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f']
                commit_id_new = ''.join(choices(characters, k = 40))

                with open('references.txt', 'a') as file:
                    file = file.write(f"{name}, {commit_id}, {commit_id_new}\n")

                chdir(path.join(root_path, '.wit', 'images'))
                with open(f"{commit_id}.txt" , 'w') as file:
                    file.write(f"parent = None \ndate = {date.today()}\nmessage = None")

                copytree(path.join(root_path, '.wit', 'staging_area'), path.join(root_path, '.wit', 'images', commit_id_new))


def merge(name):
    copy_path = getcwd()

    while '.wit' not in listdir(copy_path):
        path_list = copy_path.split('\\')[:-1]
        
        if ':' in path_list[-1]:
            print(".wit folder not exsits in this path")
            return None

        copy_path = '\\'.join(path_list)
        chdir(copy_path)

    print(".wit folder is found!, creating a backup here:")
    root_path = getcwd()

    chdir(path.join(root_path, '.wit'))
    with open('references.txt', 'r') as file:
        file = file.read()
        for i in file.split("\n"):
            if name in i:
                i_list = i.split(",")
                folder1 = i_list[1]
                folder2 = i_list[2]
                characters = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f']
                commit_id = ''.join(choices(characters, k = 40))

                chdir(path.join(root_path, '.wit', 'images'))
                mkdir(path.join(getcwd(), commit_id))
                
                
                copytree(folder1, path.join(getcwd(), commit_id))
                copytree(folder2, path.join(getcwd(), commit_id))



if __name__ == '__main__':

    if argv[1].lower() == 'init':
        init()

    if argv[1].lower() == 'add':
        add()

    if argv[1].lower() == 'commit': 
        try:
            commit(argv[2])
        except IndexError:
            commit(None)

    if argv[1].lower() == 'status':
        status()

    if argv[1].lower() == 'checkout':
        checkout()

    if argv[1].lower() == 'graph':
        graph()

    if argv[1].lower() == 'branch': 
        try:
            branch(argv[2], argv[3])
        except IndexError:
            print("branch name or commit_id is missing")

    if argv[1].lower() == 'merge':
        try:
            merge(argv[2])
        except IndexError:
            print("branch name is missing")




        