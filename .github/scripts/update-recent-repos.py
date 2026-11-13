import os
import re
import urllib.request
import json

CUSTOM_DESCRIPTIONS = {
    "WC-Landing": "WebConcierge responsive client & marketing landing page",
    "demoBot": "Automated conversational assistant & bot prototype",
    "Chandra-vllm": "LLM inference & serving experiments with vLLM",
    "ready4love": "Dating & social discovery web application prototype",
    "soora-native": "React Native mobile client application",
}

CUSTOM_LANGUAGES = {
    "WC-Landing": "React / JavaScript",
}

def clean_description(name, raw_desc):
    if name in CUSTOM_DESCRIPTIONS:
        return CUSTOM_DESCRIPTIONS[name]
    if not raw_desc or "codesandbox" in raw_desc.lower():
        return "Interactive web application & experiments"
    return raw_desc

def fetch_recent_repos():
    url = "https://api.github.com/users/LastGentlman/repos?sort=pushed&per_page=30"
    headers = {"User-Agent": "GitHub-Action-Recent-Repos"}
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"token {token}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        repos = json.loads(resp.read().decode("utf-8"))

    filtered = []
    for r in repos:
        if r.get("fork") or r.get("private") or r.get("name") == "LastGentlman":
            continue
        filtered.append(r)
        if len(filtered) >= 6:
            break

    lines = []
    for r in filtered:
        name = r["name"]
        html_url = r["html_url"]
        desc = clean_description(name, r.get("description"))
        lang = CUSTOM_LANGUAGES.get(name) or r.get("language") or "Code"
        stars = r.get("stargazers_count", 0)
        star_str = f" · ⭐ {stars}" if stars > 0 else ""
        lines.append(f"- **[{name}]({html_url})** — {desc} `[{lang}{star_str}]`")

    return "\n".join(lines)

def update_readme():
    content = fetch_recent_repos()
    base_dir = os.path.join(os.path.dirname(__file__), "..", "..")
    for filename in ["README.md", "README.es.md"]:
        readme_path = os.path.join(base_dir, filename)
        if not os.path.exists(readme_path):
            continue
        with open(readme_path, "r", encoding="utf-8") as f:
            readme = f.read()

        pattern = r"(<!-- RECENT-REPOS:START -->\n)(.*?)(<!-- RECENT-REPOS:END -->)"
        replacement = rf"\g<1>{content}\n\g<3>"
        new_readme = re.sub(pattern, replacement, readme, flags=re.DOTALL)

        if new_readme != readme:
            with open(readme_path, "w", encoding="utf-8") as f:
                f.write(new_readme)
            print(f"{filename} updated with recent repositories.")
        else:
            print(f"{filename} already up to date.")

if __name__ == "__main__":
    update_readme()
