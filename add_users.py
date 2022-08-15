from github import Github

GITHUB_PAT = "PAT HERE"

ORG_NAME = "ORG NAME"
TEAM_ID = -1 # ADD TEAM ID (get like this https://fabian-kostadinov.github.io/2015/01/16/how-to-find-a-github-team-id/)

USER_LIST = [
    "USER LIST HERE",
]

def main():
    g = Github(GITHUB_PAT)

    org = g.get_organization(ORG_NAME)
    team = org.get_team(TEAM_ID)

    for user_name in USER_LIST:
        try:
            user = g.get_user(user_name)

            print(f"Inviting '{user.login}' ('{user.name}') to '{team.name}'")

            team.add_membership(user, role='member')
        except:
            print(f"ERROR: Failed to add '{user_name}'")

if __name__ == '__main__':
    main()