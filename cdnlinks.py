import os

def generate_jsdelivr_links(user, repo, branch, folder):
    base_url = f"https://cdn.jsdelivr.net/gh/{user}/{repo}@{branch}/"
    cdn_links = []
    
    for root, dirs, files in os.walk(folder):
        for file in files:
            rel_path = os.path.relpath(os.path.join(root, file), ".")
            cdn_links.append(base_url + rel_path.replace("\\", "/"))  # Fix for Windows paths

    return cdn_links

# Example usage:
user = "roxrox0"
repo = "media"
branch = "main"
folder = "female/lipsync"

cdn_links = generate_jsdelivr_links(user, repo, branch, folder)

for link in cdn_links:
    print(link)
