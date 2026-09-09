# bruceabernethy.com

Source for my blog. [Jekyll](https://jekyllrb.com) + the
[minimal-mistakes](https://github.com/mmistakes/minimal-mistakes) theme,
deployed to GitHub Pages.

## Running it locally

Ruby is pinned by `.ruby-version` and picked up automatically by `chruby` when
you `cd` in. One-time setup on a new machine:

```bash
brew install chruby ruby@3.4
ln -sfn /opt/homebrew/opt/ruby@3.4 ~/.rubies/ruby-3.4.10
```

then add to `~/.zshrc`:

```bash
source /opt/homebrew/opt/chruby/share/chruby/chruby.sh
source /opt/homebrew/opt/chruby/share/chruby/auto.sh
```

After that:

```bash
bundle install
bundle exec jekyll serve --drafts
```

The site is at <http://localhost:4000>. `--drafts` includes anything in
`_drafts/`, which is otherwise excluded from the build.

## Writing a post

```bash
bin/new-post "My Post Title"           # _posts/YYYY-MM-DD-my-post-title.md
bin/new-post --draft "Half An Idea"    # _drafts/half-an-idea.md
```

Both scaffold from `_templates/post.md`. Fill in `excerpt`, `category`, `tags`
and `header.teaser`; see [CLAUDE.md](CLAUDE.md) for the established category and
tag vocabulary.

Images live in `assets/images/` and are referenced from the site root, e.g.
`/assets/images/foo.png`.

## Publishing

Push to `main`. GitHub Actions builds and deploys to Pages
([workflow](.github/workflows/jekyll.yml)); it takes about two minutes. There is
no staging site, so build locally first.

## Layout

| path | what |
| --- | --- |
| `_posts/` | Published posts, `YYYY-MM-DD-slug.md` |
| `_drafts/` | Unpublished drafts, no date prefix |
| `_pages/` | Standalone pages and taxonomy archives |
| `_layouts/`, `_includes/` | Local overrides of theme files |
| `_data/navigation.yml` | Masthead menu |
| `_templates/`, `bin/` | Post scaffolding |
| `assets/` | Images and `main.scss` |
| `_config.yml` | Site configuration |
