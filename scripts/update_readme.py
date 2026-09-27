#!/usr/bin/env python3
"""
Scans a GitHub user's public pull requests and rewrites the
auto-generated sections of README.md (marked with HTML comment
markers) with a fresh table.

Env vars:
  GITHUB_USERNAME   - the GitHub username to scan (required)
  GITHUB_TOKEN      - a token with public read access (provided
                      automatically by GITHUB_ACTIONS as
                      secrets.GITHUB_TOKEN)
  EXCLUDE_OWN_REPOS - "true" (default) to skip PRs opened against
                      the user's own repositories
  README_PATH       - path to the README file (default: README.md)
"""

import json
import os
import re
import sys
import urllib.request
import urllib.error
from datetime import datetime, timezone

USERNAME = os.environ.get("GITHUB_USERNAME", "").strip()
TOKEN = os.environ.get("GITHUB_TOKEN", "").strip()
EXCLUDE_OWN_REPOS = os.environ.get("EXCLUDE_OWN_REPOS", "true").lower() == "true"
README_PATH = os.environ.get("README_PATH", "README.md")

if not USERNAME:
    print("ERROR: GITHUB_USERNAME env var is required.", file=sys.stderr)
    sys.exit(1)

API_ROOT = "https://api.github.com"


def gh_get(url):
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    if TOKEN:
        req.add_header("Authorization", f"Bearer {TOKEN}")
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        body = e.read().decode(errors="replace")
        print(f"ERROR: GitHub API request failed ({e.code}): {url}\n{body}", file=sys.stderr)
        sys.exit(1)


def fetch_all_prs(username):
    """Paginate through the search API for every PR authored by `username`."""
    items = []
    page = 1
    per_page = 100
    while True:
        url = (
            f"{API_ROOT}/search/issues"
            f"?q=author:{username}+type:pr"
            f"&sort=created&order=desc&per_page={per_page}&page={page}"
        )
        data = gh_get(url)
        batch = data.get("items", [])
        items.extend(batch)
        if len(batch) < per_page:
            break
        page += 1
        # GitHub's search API caps results at 1000 total.
        if page * per_page > 1000:
            break
    return items


def status_icon(item):
    merged_at = item.get("pull_request", {}).get("merged_at")
    if merged_at:
        return "✅"
    if item.get("state") == "open":
        return "🟡"
    return "❌"


def build_table(prs):
    rows = [
        "| Status | Project | PR | Description |",
        "|:---:|---|---|---|",
    ]
    for item in prs:
        repo = item["repository_url"].split("/repos/")[1]
        icon = status_icon(item)
        pr_url = item["html_url"]
        number = item["number"]
        title = item["title"].replace("|", "\\|").strip()
        repo_url = f"https://github.com/{repo}"
        rows.append(f"| {icon} | [{repo}]({repo_url}) | [#{number}]({pr_url}) | {title} |")
    rows.append("")
    rows.append("**Legend:** ✅ Merged &nbsp;·&nbsp; 🟡 Open / In Review &nbsp;·&nbsp; ❌ Closed (not merged)")
    return "\n".join(rows)


def build_stats(prs, repo_count):
    merged = sum(1 for i in prs if i.get("pull_request", {}).get("merged_at"))
    open_ = sum(1 for i in prs if i.get("state") == "open")
    closed_unmerged = len(prs) - merged - open_
    return "\n".join(
        [
            f"- **Total PRs opened:** {len(prs)} (across external repositories)",
            f"- **Merged:** {merged}",
            f"- **Open / In review:** {open_}",
            f"- **Closed without merge:** {closed_unmerged}",
            f"- **Distinct organizations/projects contributed to:** {repo_count}",
        ]
    )


def build_badges(username, prs):
    merged = sum(1 for i in prs if i.get("pull_request", {}).get("merged_at"))
    return "\n".join(
        [
            f'  <a href="https://github.com/{username}">',
            f'    <img src="https://img.shields.io/badge/GitHub-{username}-181717?style=for-the-badge&logo=github" alt="GitHub" />',
            "  </a>",
            f'  <img src="https://img.shields.io/badge/Pull_Requests-{len(prs)}-blue?style=for-the-badge" alt="Pull Requests" />',
            f'  <img src="https://img.shields.io/badge/Merged-{merged}-success?style=for-the-badge" alt="Merged" />',
        ]
    )


def replace_between_markers(text, start_marker, end_marker, new_content):
    pattern = re.compile(
        re.escape(start_marker) + r".*?" + re.escape(end_marker),
        re.DOTALL,
    )
    replacement = f"{start_marker}\n{new_content}\n{end_marker}"
    if not pattern.search(text):
        print(f"WARNING: markers {start_marker!r}/{end_marker!r} not found in {README_PATH}; skipping.", file=sys.stderr)
        return text
    return pattern.sub(replacement, text)


def main():
    all_prs = fetch_all_prs(USERNAME)

    if EXCLUDE_OWN_REPOS:
        prs = [
            i for i in all_prs
            if i["repository_url"].split("/repos/")[1].split("/")[0].lower() != USERNAME.lower()
        ]
    else:
        prs = all_prs

    repos = {i["repository_url"].split("/repos/")[1] for i in prs}

    with open(README_PATH, "r", encoding="utf-8") as f:
        readme = f.read()

    readme = replace_between_markers(
        readme, "<!-- BADGES:START -->", "<!-- BADGES:END -->", build_badges(USERNAME, prs)
    )
    readme = replace_between_markers(
        readme, "<!-- CONTRIBUTIONS-TABLE:START -->", "<!-- CONTRIBUTIONS-TABLE:END -->", build_table(prs)
    )
    readme = replace_between_markers(
        readme, "<!-- STATS:START -->", "<!-- STATS:END -->", build_stats(prs, len(repos))
    )
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    readme = replace_between_markers(
        readme, "<!-- LAST-UPDATED:START -->", "<!-- LAST-UPDATED:END -->",
        f"_Last scanned: {timestamp}_"
    )

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(readme)

    print(f"Updated {README_PATH}: {len(prs)} PRs across {len(repos)} repos.")


if __name__ == "__main__":
    main()
