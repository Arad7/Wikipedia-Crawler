# Wikipedia Crawler
A Python-based web crawler that identifies instances of keywords in Wikipedia hyperlinks.

## How it works
This program takes a user-provided Wikipedia entry (e.g., 'ball') as input and retrieves the corresponding Wikipedia page. It then navigates through each hyperlink on the page and counts the occurrences of the original keyword (provided by the user) in the linked page's content.

At the end of the process, the program outputs an ordered list (from smallest to largest) of all the hyperlinks, along with the number of times the keyword appears in each linked page.

**Note**: For larger Wikipedia pages with numerous hyperlinks, the process may take several minutes due to the high number of linked pages being crawled.

### Example:
If the input keyword is "ball", the output might include:
'''
football: 826
'''
This indicates that the word "ball" appears 826 times on the Wikipedia page for "football" (as of 2021). The counts may vary as Wikipedia pages are updated.
