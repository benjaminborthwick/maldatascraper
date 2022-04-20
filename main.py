# This is a sample Python script.
from jikanpy import Jikan
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    members = []
    with open("members.txt") as file:
        file.seek(0, 2)  # go to end of file
        eof = file.tell()  # get end-of-file position
        file.seek(0, 0)  # go back to start of file
        nextLine = file.tell() != eof
        while nextLine:
            members.append(file.readline().strip())
            nextLine = file.tell() != eof
    jikan = Jikan()
    animelist = {}


    for member in members:
        i = 1
        while True:
            print(member + ": Page " + str(i))
            try:
                user = jikan.user(member, request="animelist", parameters={'page': i}, argument='completed')
            except:
                print(member + " is not a valid user name")
            else:
                for anime in user['anime']:
                    if anime['watching_status'] > 2:
                        continue
                    count = animelist.setdefault(anime['title'], [])
                    animelist[anime['title']].append(member if anime['watching_status']==2 else (member + " (W)"))
            if (len(user['anime']) < 300):
                break
            i += 1
    animes = sorted(animelist.items(), key=lambda entry: len(entry[1]), reverse=True)
    with open("results.csv", "w") as results:
        results.write("Anime")
        for member in members:
            results.write("\t" + member)
        results.write("\n")
        for anime in animes:
            try:
                results.write(anime[0])
            except:
                for char in anime[0]:
                    try:
                        results.write(char)
                    except:
                        results.write(' ')
            for person in members:
                if person in anime[1]:
                    if (person + " (W)") in anime[1]:
                        results.write("\t2")
                    else:
                        results.write("\t1")
                else:
                    results.write("\t0")
            results.write("\n")



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
