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
| CV | `_pages/cv.md` |
| Publications (one file each) | `_publications/` – `category:` is one of `manuscripts`, `conferences`, `books`, `reports`, `theses`, `datasets` |
| Talks | `_talks/` |
| Research projects | `_portfolio/` |
| Teaching | `_teaching/` |
| Supervision | `_pages/supervision.md` |
| News | `_posts/` |
| Top menu | `_data/navigation.yml` |

## Local preview

```bash
bundle install
bundle exec jekyll serve -l -H localhost
```
