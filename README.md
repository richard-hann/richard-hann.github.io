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
| Publications, presentations, datasets, people, funding | edit `markdown_generator/hann_publications.py` (publications, presentations) and `markdown_generator/hann_more.py` (datasets, people, funding, research projects), then run `python3 markdown_generator/build_hann.py` |
| Teaching | `_teaching/` |
| News | `_posts/` |
| Top menu | `_data/navigation.yml` |

## Local preview

```bash
bundle install
bundle exec jekyll serve -l -H localhost
```
