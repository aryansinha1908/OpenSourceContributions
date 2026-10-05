<h1 align="center">Open Source Contributions</h1>

<p align="center">
  A running log of pull requests and issues I've worked on across the open-source ecosystem.
</p>

<p align="center">
<!-- BADGES:START -->
  <a href="https://github.com/aryansinha1908">
    <img src="https://img.shields.io/badge/GitHub-aryansinha1908-181717?style=for-the-badge&logo=github" alt="GitHub" />
  </a>
  <img src="https://img.shields.io/badge/Pull_Requests-22-blue?style=for-the-badge" alt="Pull Requests" />
  <img src="https://img.shields.io/badge/Merged-15-success?style=for-the-badge" alt="Merged" />
<!-- BADGES:END -->
</p>

<!-- Last auto-updated: set by the update-readme workflow on each successful run -->
<!-- LAST-UPDATED:START -->
_Last scanned: 2026-10-05 14:02 UTC_
<!-- LAST-UPDATED:END -->

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=aryansinha1908&show_icons=true&theme=tokyonight&hide_border=true" alt="GitHub Stats" height="165"/>
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=aryansinha1908&theme=tokyonight&hide_border=true" alt="GitHub Streak" height="165"/>
</p>

---

## About

I contribute fixes, features, and documentation improvements to open-source projects — usually by picking up an open issue, understanding the root cause, and shipping a focused, well-tested PR. This repo is a single place to point people to that work instead of scattering it across dozens of forks.

> **Tip:** Every row below links straight to the real PR/issue on GitHub — click through for the full diff and discussion.

---

## Highlighted Contributions

A few PRs that involved non-trivial investigation or design decisions, not just a one-line fix:

| Project | Contribution | Impact |
|---|---|---|
| [`wemake-services/django-modern-rest`](https://github.com/wemake-services/django-modern-rest) | [#1404 – Faster JWT encode/decode via `msgspec`](https://github.com/wemake-services/django-modern-rest/pull/1404) | ~15–25% end-to-end latency reduction on JWT operations, byte-identical tokens preserved |
| [`wemake-services/django-modern-rest`](https://github.com/wemake-services/django-modern-rest) | [#1408 – Removed `dataclasses.asdict` from JWT payload build](https://github.com/wemake-services/django-modern-rest/pull/1408) | `encode` time cut roughly in half (29.9µs → 14.6µs) |
| [`OpsiMate/OpsiMate`](https://github.com/OpsiMate/OpsiMate) | [#900 – Centralized admin authorization middleware](https://github.com/OpsiMate/OpsiMate/pull/900) | Removed 18 duplicated auth checks across 5 controllers; caught a silently-degraded permission check in the process |
| [`kishorjakkula/LatticePolicy`](https://github.com/kishorjakkula/LatticePolicy) | [#236 – Retired a stale npm audit exception](https://github.com/kishorjakkula/LatticePolicy/pull/236) | Closed a security-policy gap left over from a prior dependency bump |

---

## All Pull Requests

<!-- CONTRIBUTIONS-TABLE:START -->
| Status | Project | PR | Description |
|:---:|---|---|---|
| 🟡 | [Open-Source-Kigali/docksight](https://github.com/Open-Source-Kigali/docksight) | [#275](https://github.com/Open-Source-Kigali/docksight/pull/275) | Issue 172 |
| ✅ | [wemake-services/django-modern-rest](https://github.com/wemake-services/django-modern-rest) | [#1408](https://github.com/wemake-services/django-modern-rest/pull/1408) | Build the JWToken payload without asdict |
| ✅ | [OpsiMate/OpsiMate](https://github.com/OpsiMate/OpsiMate) | [#900](https://github.com/OpsiMate/OpsiMate/pull/900) | Fix for Issue #772 |
| ✅ | [wemake-services/django-modern-rest](https://github.com/wemake-services/django-modern-rest) | [#1404](https://github.com/wemake-services/django-modern-rest/pull/1404) | Provide faster JWT decode and encode options with msgspec |
| 🟡 | [FZJ-IEK3-VSA/glaes](https://github.com/FZJ-IEK3-VSA/glaes) | [#168](https://github.com/FZJ-IEK3-VSA/glaes/pull/168) | Closes issue #166 |
| ✅ | [OpenAgentHQ/openagent-eval](https://github.com/OpenAgentHQ/openagent-eval) | [#367](https://github.com/OpenAgentHQ/openagent-eval/pull/367) | docs(ci): document mypy strict mode target and current CI status #339 |
| ✅ | [kishorjakkula/LatticePolicy](https://github.com/kishorjakkula/LatticePolicy) | [#236](https://github.com/kishorjakkula/LatticePolicy/pull/236) | Retire the React Router npm audit exception |
| 🟡 | [Open-Source-Kigali/docksight](https://github.com/Open-Source-Kigali/docksight) | [#179](https://github.com/Open-Source-Kigali/docksight/pull/179) | Issue 173 |
| ✅ | [vc079/AURASCAN](https://github.com/vc079/AURASCAN) | [#3](https://github.com/vc079/AURASCAN/pull/3) | feat: Adds CSV export to Telemetry logs |
| ✅ | [michaelegner/architecture-intelligence-platform](https://github.com/michaelegner/architecture-intelligence-platform) | [#16](https://github.com/michaelegner/architecture-intelligence-platform/pull/16) | fix: Makes runtime demo services wait for AIP to become healthy |
| ✅ | [OpenAgentHQ/openagent-eval](https://github.com/OpenAgentHQ/openagent-eval) | [#363](https://github.com/OpenAgentHQ/openagent-eval/pull/363) | feat(changelog): automate format validation and document process |
| ✅ | [Open-Source-Kigali/docksight](https://github.com/Open-Source-Kigali/docksight) | [#176](https://github.com/Open-Source-Kigali/docksight/pull/176) | fix: Removes console logs from ContainerTable.tsx file |
| ✅ | [moizycodes/moizy-open-source-issues](https://github.com/moizycodes/moizy-open-source-issues) | [#174](https://github.com/moizycodes/moizy-open-source-issues/pull/174) | feat: Adds isCacheStale utility with tests |
| ✅ | [allinerosamkup-ai/northstar-cognitive-platform](https://github.com/allinerosamkup-ai/northstar-cognitive-platform) | [#7](https://github.com/allinerosamkup-ai/northstar-cognitive-platform/pull/7) | feat: Adds port configuration using --port |
| ❌ | [Tanz2024/citizen-app](https://github.com/Tanz2024/citizen-app) | [#10](https://github.com/Tanz2024/citizen-app/pull/10) | Changed the expo default copyright holder line in LICENSE |
| ✅ | [lingdojo/kana-dojo](https://github.com/lingdojo/kana-dojo) | [#29201](https://github.com/lingdojo/kana-dojo/pull/29201) | content: add new japanese false friend |
| ✅ | [IvanTran-2001/FriendChise](https://github.com/IvanTran-2001/FriendChise) | [#393](https://github.com/IvanTran-2001/FriendChise/pull/393) | Added roster API endpoints #392 |
| ✅ | [Rohan-Shridhar/gridcraft](https://github.com/Rohan-Shridhar/gridcraft) | [#104](https://github.com/Rohan-Shridhar/gridcraft/pull/104) | Inverted paintbrush.png |
| ❌ | [Robbo-lab/mcp-task-app](https://github.com/Robbo-lab/mcp-task-app) | [#71](https://github.com/Robbo-lab/mcp-task-app/pull/71) | Fixed the README.md file according to the issue #45 |
| ✅ | [geturbackend/urBackend](https://github.com/geturbackend/urBackend) | [#76](https://github.com/geturbackend/urBackend/pull/76) | Added Aria Labels for buttons in CollectionsTable.jsx and DatabaseSidebar.jsx |
| ❌ | [crweiner/hacktoberfest-swag-list](https://github.com/crweiner/hacktoberfest-swag-list) | [#1018](https://github.com/crweiner/hacktoberfest-swag-list/pull/1018) | Added CopilotKit in the Hacktober swag list |
| ❌ | [Syknapse/Contribute-To-This-Project](https://github.com/Syknapse/Contribute-To-This-Project) | [#4265](https://github.com/Syknapse/Contribute-To-This-Project/pull/4265) | aryansinha1908's card |

**Legend:** ✅ Merged &nbsp;·&nbsp; 🟡 Open / In Review &nbsp;·&nbsp; ❌ Closed (not merged)
<!-- CONTRIBUTIONS-TABLE:END -->

---

## Issues Resolved

Most of the issues below were closed by one of the pull requests listed above:

| Project | Issue Closed | Fixed By |
|---|---|---|
| OpsiMate/OpsiMate | Duplicated admin-auth checks | [PR #900](https://github.com/OpsiMate/OpsiMate/pull/900) |
| wemake-services/django-modern-rest | Slow JWT payload build | [PR #1404](https://github.com/wemake-services/django-modern-rest/pull/1404), [PR #1408](https://github.com/wemake-services/django-modern-rest/pull/1408) |
| FZJ-IEK3-VSA/glaes | Unused images in repo | [PR #168](https://github.com/FZJ-IEK3-VSA/glaes/pull/168) |
| OpenAgentHQ/openagent-eval | Undocumented mypy CI status | [PR #367](https://github.com/OpenAgentHQ/openagent-eval/pull/367) |
| kishorjakkula/LatticePolicy | Temporary npm audit exception | [PR #236](https://github.com/kishorjakkula/LatticePolicy/pull/236) |
| Open-Source-Kigali/docksight | Missing Prettier formatting | [PR #179](https://github.com/Open-Source-Kigali/docksight/pull/179) |
| vc079/AURASCAN | No way to export telemetry logs | [PR #3](https://github.com/vc079/AURASCAN/pull/3) |
| michaelegner/architecture-intelligence-platform | Demo services racing container startup | [PR #16](https://github.com/michaelegner/architecture-intelligence-platform/pull/16) |
| OpenAgentHQ/openagent-eval | Changelog format drift | [PR #363](https://github.com/OpenAgentHQ/openagent-eval/pull/363) |
| Open-Source-Kigali/docksight | Debug logs left in production code | [PR #176](https://github.com/Open-Source-Kigali/docksight/pull/176) |
| moizycodes/moizy-open-source-issues | Missing cache-staleness utility | [PR #174](https://github.com/moizycodes/moizy-open-source-issues/pull/174) |
| allinerosamkup-ai/northstar-cognitive-platform | No CLI flag for port config | [PR #7](https://github.com/allinerosamkup-ai/northstar-cognitive-platform/pull/7) |
| Tanz2024/citizen-app | Stale template copyright notice | [PR #10](https://github.com/Tanz2024/citizen-app/pull/10) |
| Open-Source-Kigali/docksight | Formatting inconsistencies (`apps/web`) | [PR #179](https://github.com/Open-Source-Kigali/docksight/pull/179) |
| geturbackend/urBackend | Missing accessibility labels | [PR #76](https://github.com/geturbackend/urBackend/pull/76) |

---

## Contribution Stats

<!-- STATS:START -->
- **Total PRs opened:** 22 (across external repositories)
- **Merged:** 15
- **Open / In review:** 3
- **Closed without merge:** 4
- **Distinct organizations/projects contributed to:** 18
<!-- STATS:END -->

---

<p align="center">
  If you're a maintainer and want a hand with an open issue, feel free to reach out via <a href="https://github.com/aryansinha1908">GitHub</a>.
</p>

---

<details>
<summary>About the auto-update workflow (click to expand)</summary>

The tables and stats above are refreshed automatically by <code>.github/workflows/update-readme.yml</code>, which:

1. Runs on a schedule (weekly by default — see the workflow file for a biweekly option).
2. Calls <code>scripts/update_readme.py</code>, which queries the GitHub Search API for every PR authored by this account.
3. Rewrites the sections between the <code>&lt;!-- ...:START --&gt;</code> / <code>&lt;!-- ...:END --&gt;</code> comment markers in this file.
4. Commits the change back to the repo if anything changed.

No setup beyond adding the two files is needed — it uses the repo's built-in <code>GITHUB_TOKEN</code>, which is created automatically for every workflow run.

</details>
