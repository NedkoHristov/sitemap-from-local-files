# sitemap-from-local-files

# Usecase
Since you're here you're trapped into the similar problem that I had - to create a sitemap based on local files that you had a copy with Then crowl the website from anywhere (web.archive.org?) and bring a fairly working copy of the website (on the static parts).

# Usage:

Using python3 run the script inside the local directory that needs to be converted to a sitemap and execute it. It fast so it will take seconds:

```
python3 sitemap-from-local-files.py
```

# Variables:
`directory` - by default it's the current directory

`domain` - by default it's `example.com`

# Examples:

```
python3 sitemap-from-local-files.py
```

```
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://neshtosi.com/sitemap-from-local-files.py</loc>
  </url>
  <url>
    <loc>https://neshtosi.com/README.md</loc>
  </url>
</urlset>#
