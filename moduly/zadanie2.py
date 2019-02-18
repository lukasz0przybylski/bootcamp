import sys

try:
    f_fname = sys.argv[1]
except IndexError:
    print("nie dales nazwy pliku")
    exit()


def prepere_line(napis):
    login, akcja, czas = napis.split(";")
    czas = int(czas)
    return login, akcja, czas


last_login_time = {}
user_tottal_time = defaultdict(int)

def my_key(login):
    return int(item[0].split("-")[-1])

try:
    with open(f_fname) as f:
        login, action, time = prepere_line(line)
        if action == "LOGIN":
            last_login_time[login] = time
        elif action == "LOGOUT":
            session_time = time - last_login_time[login]
            user_tottal_time[login] += session_time
    for login, time in sorted(user_tottal_time.items(), key=my_key ):
        print(f" - {login}: {time} s")

except FileNotFoundError:
    print("nie ma takiego pliku")

print(last_login_time)
print(user_tottal_time)
