def run():
    print("""
git pull - fetches and downloads content from the remote repository and updates the local repository to match
that content.

git status - checks the status. Indicates which files/folders have been newly created or changed. This is a
useful command to use before and after staging changes.

git add . - stages all changes in the current directory and its sub-directories. This command is used before the changes are committed.

git commit -m "some message" - commits the staged changes. An optional short message is provided to indicate what has changed and why.

git push - push everything from the local repository to the remote repository. This should be done once the changes are ready to be shared.
""")


run()
