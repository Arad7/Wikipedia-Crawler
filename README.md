# Wikipedia Crawler
 A web crawler finding instances of key words in hyperlinks

# What does it do?
The user need to give a Wikipedia entry (just the name, for example: ball)
The program will go to the Wikipedia page of the desired entry and will enter each of the hyperlinks links in the page. for each hyperlink, it will count how many time the original phrase (that the user put as an input) is shown.

At the end, the program will print an OrderedList from smallest to largest of all the hyperlinks and a corresponding number that represent how many times the phrased is shown.

Note -> for bigger Wikipedia pages, this can take few minutes as there could be dozens or hundreds of hyperlinks in the Wikipedia page.

Example: if we enter the value: ball, the last thing the program will print will be-
football: 826
This means that the word "ball" is mentioned 826 times in the Wikipedia page of "football".
(this specific example is correct to 2021), those values changes as the Wikipedia pages changes. 
