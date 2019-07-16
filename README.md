# Simple Search String code challenge


### Requirements installation


```sh
pip install -r requirements.txt 
```

### Running the main file code:
> Try the below command to run the main program.

```sh
python3 simple_search.py <pathToFiles>
```
> **Example** To run the main program run this in main project directory.

```sh
python3 simple_search.py test/testFiles 
```



# Test!
To test the code using pytest. Goto the path/folder test we can use this command:

```sh
 pytest test.py
```
It will run all the unit test on the methods in simple_search.py

# String matching Explanation!

For string matching I am using my own cutom method **match_word_ratio_finder** which takes search word and all the contents of file as input and try to find the search word in the content and return a list of 2 elements. 1st element represent the percentage that the word to be searched found in the content or not and the 2nd element represents the occurrence of the search word in the content.

# Ranking criteria

As I am receiving a list from my custom method **match_word_ratio_finder** I use the value as sorting parameter. If two files contains the all the elements then it will check the 2nd parameter **i.e** the occurrence of these words the one which has more occurrence will be rank higher.