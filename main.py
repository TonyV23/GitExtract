from pydriller import Repository

for commit in Repository('linkRepo').traverse_commits() :
    print (commit.hash)
    print (commit.author.name)
    print (commit.author_date)

    for modification in commit.modifications :
        print(modification.file_name +' is changed ')