# This is a sample Python script.
from mal import client
from mal import enums
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#docs: https://malpy.readthedocs.io/en/latest/index.html

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
    animelist = {}


    for member in members:
        u_list = cli.get_anime_list(member, limit=100, fields=[enums.Field.mean, enums.Field.title], status='completed')
        i = 1
        while u_list is not None:
            for anime in u_list:
                count = animelist.setdefault(anime.entry.title, [anime.entry.mean, []])
                animelist[anime.entry.title][1].append(anime.score)
            print(member + ' Page ' + str(i))
            i += 1
            u_list = u_list.next_page(cli)
    animes = sorted(animelist.items(), key=lambda entry: len(entry[1]), reverse=True)
    with open("scores.csv", "w") as results:
        C = 0
        num = 0
        for anime in animes:
            for score in anime[1][1]:
                C += score
                num += 1
        C = C/num
        for anime in animes:
            for char in anime[0]:
                try:
                    results.write(char)
                except:
                    results.write(' ')
            mal_mean = anime[1][0]
            results.write('\t' + str(mal_mean))
            sum = 0
            for score in anime[1][1]:
                sum += score
            v = len(anime[1][1])
            m = 1
            R = sum / v
            bayesian = (v / (v + m)) * R + (m / (v + m)) * C
            results.write('\t' + str(bayesian) + "\n")



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
