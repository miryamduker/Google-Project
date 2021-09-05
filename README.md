# googleProject
AutoCompleteData

In this project we got a huge directory tree archive.
We then let the user insert any word/sentence that he wishes.
For that input wemust return and print the closest 5 matchest.
A match is any line in the directory tree that contains the user's input.
If there is no so match then we will search for a match of one mistake, which means that there can be either an additional character or a missing one or a wrong one.
Searching through so much data can take a long time. That's why it's important to keep the data in an easy way to retrieve the data.
We kept the data in a python dict where every word was a key and it's value was an array of data objects whose sentence contains this word .
The Data object properties are it's path,line number and it's sentence.
Now when we get an input from the user we start iterating over it word by word,
then taking the first word and going to it's value in the dict and checking in the array of sentences if this whole sentence exists.
If it does, that's great and we can just return 5 of them.
Otherwise we have to send the word to corrections(changing every possible mistake that can happen) and then check if there exists such a word
If it does we will check if a whole sentence with that fixed word exists.If so ,we'll return it.
If after iterating over all the user input words and we still have not found any sentences then we will print the user that none were found.
