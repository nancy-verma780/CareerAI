import httpx


async def analyze_github(username):

    url = f"https://api.github.com/users/{username}/repos"


    async with httpx.AsyncClient() as client:

        response = await client.get(url)


    repos = response.json()


    if not isinstance(repos,list):

        return {
            "error":"GitHub user not found"
        }


    languages=[]


    for repo in repos:

        if repo.get("language"):

            languages.append(
                repo["language"]
            )


    score = 0


    if len(repos) > 5:
        score += 30

    if len(set(languages)) > 2:
        score += 30

    if len(repos) > 10:
        score += 40


    return {

        "username":username,

        "repositories":len(repos),

        "top_languages":list(set(languages)),

        "github_score":score

    }