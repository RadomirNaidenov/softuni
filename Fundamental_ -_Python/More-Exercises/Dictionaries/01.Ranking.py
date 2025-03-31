contests = {}
while True:
    command = input().strip()
    if command == "end of contests":
        break
    contest, password = command.split(':')
    contests[contest] = password

submissions = {}
while True:
    command = input().strip()
    if command == "end of submissions":
        break
    contest, password, username, points = command.split('=>')
    points = int(points)
    
    
    if contest in contests and contests[contest] == password:
        if username not in submissions:
            submissions[username] = {}
        if contest not in submissions[username] or submissions[username][contest] < points:
            submissions[username][contest] = points


best_candidate = ""
max_points = 0

for username, contests in submissions.items():
    total_points = sum(contests.values())
    if total_points > max_points:
        best_candidate = username
        max_points = total_points


print(f"Best candidate is {best_candidate} with total {max_points} points.")
print("Ranking:")


for username in sorted(submissions.keys()):
    print(username)
    
    for contest, points in sorted(submissions[username].items(), key=lambda item: -item[1]):
        print(f"#  {contest} -> {points}")
