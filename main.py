# This is a sample Python script.
from mal import client
from mal import enums
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
    cli = client.Client('abbf306998a9acabe108f8cf31d7d683')
    print(cli.get_anime_list("SixGear", limit=1000, status='completed'))
    animelist = {}


    # for member in members:
    #     u_list = cli.get_anime_list(member, limit=100, status='completed')
    #     i = 1
    #     while u_list is not None:
    #         for anime in u_list:
    #             count = animelist.setdefault(anime.entry.title, [])
    #             animelist[anime.entry.title].append(member)
    #         print(member + ' Page ' + str(i))
    #         i += 1
    #         u_list = u_list.next_page(cli)
    # animes = sorted(animelist.items(), key=lambda entry: len(entry[1]), reverse=True)
    # with open("results.csv", "w") as results:
    #     results.write("Anime")
    #     for member in members:
    #         results.write("\t" + member)
    #     results.write("\n")
    #     for anime in animes:
    #         try:
    #             results.write(anime[0])
    #         except:
    #             for char in anime[0]:
    #                 try:
    #                     results.write(char)
    #                 except:
    #                     results.write(' ')
    #         for person in members:
    #             if person in anime[1]:
    #                 if (person + " (W)") in anime[1]:
    #                     results.write("\t2")
    #                 else:
    #                     results.write("\t1")
    #             else:
    #                 results.write("\t0")
    #         results.write("\n")



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
