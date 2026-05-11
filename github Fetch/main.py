import requests

def fetch_top_python_repos(top_n=5, token=None):
	headers = {"Accept": "application/vnd.github.v3+json"}
	if token:
		headers["Authorization"] = f"token {token}"

	response = requests.get(
		"https://api.github.com/search/repositories",
		params={"q": "language:python", "sort": "stars", "order": "desc"},
		headers=headers,
		timeout=10,
	)
	response.raise_for_status()
	json_response = response.json()
	popular_repos = json_response.get("items", [])
	for repo in popular_repos[:top_n]:
		print(f"Name: {repo.get('name')}")
		print(f"Description: {repo.get('description')}")
		print(f"Stars: {repo.get('stargazers_count')}\n")

if __name__ == "__main__":
	# Optionally set GITHUB_TOKEN in your environment and pass it here
	fetch_top_python_repos(top_n=5)