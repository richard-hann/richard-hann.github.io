# richard-hann.github.io

Personal academic homepage of **Dr. Richard Hann** – Senior Researcher and Director of the UAV Icing Lab, Norwegian University of Science and Technology (NTNU).

Live site: <https://richard-hann.github.io>

Built with the [Academic Pages](https://github.com/academicpages/academicpages.github.io) Jekyll template and hosted on GitHub Pages.

## Where to edit content

| What | Where |
|------|-------|
| Name, sidebar bio, profile links | `_config.yml` (`author:` block) |
| Profile photo | `images/profile.png` |
| Home page / bio | `_pages/about.md` |
| Publications, presentations, datasets, people, teaching, funding, research projects | **edit only your page https://richahan.folk.ntnu.no/index.htm** – a GitHub Action (`.github/workflows/sync-folk.yml`) copies it every night, using the Word bookmarks `Publications`, `Presentations`, `Datasets`, `People`, `Teaching`, `Funding`, `Research_projects` (and optionally `Academic_engagement`). Run it at once under *Actions → Sync from folk.ntnu.no → Run workflow*. |
| Top menu | `_data/navigation.yml` |

## Local preview

```bash
bundle install
bundle exec jekyll serve -l -H localhost
```
