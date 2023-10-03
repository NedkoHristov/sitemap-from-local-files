import os
from xml.sax.saxutils import escape

def generate_sitemap(directory, domain):
    sitemap_entries = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            # Generate the URL for the file based on its location
            file_path = os.path.relpath(os.path.join(root, file), directory)
            url = f"https://{domain}/{escape(file_path.replace(os.path.sep, '/'))}"

            # Append the URL to the sitemap entries
            sitemap_entries.append(f"  <url>\n    <loc>{url}</loc>\n  </url>")

    # Generate the sitemap XML
    sitemap_xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + '\n'.join(sitemap_entries) +
        '\n</urlset>'
    )

    return sitemap_xml

# Specify the directory and domain
directory = "."  # Current directory and its subdirectories
domain = "neshtosi.com"

# Generate the sitemap
sitemap = generate_sitemap(directory, domain)

# Save the sitemap to a file
with open("sitemap.xml", "w") as f:
    f.write(sitemap)
