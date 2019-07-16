from adevinta_code import simple_search
class TestSimpleSearch():
    def setup(self):
        self.search = simple_search.Simple_search()
    def test_search_string_in_file_no_match(self):
        file_path = 'testFiles'
        search_string = '{'
        result = self.search.search_string_in_file(file_path, search_string)   
        assert result ==  0

    def test_search_string_in_file_with_top10_match(self):
        file_path = 'testFiles'
        search_string = 'to be or not to be'
        result = self.search.search_string_in_file(file_path, search_string)   
        assert result ==  {'c.txt' : 83.33, 'a.txt': 66.67,'b.txt': 83.33, 'e.txt': 100, 'f.txt': 50.0, 'g.txt': 100, 'h.txt': 100, 'i.txt': 66.67, 'j.txt': 100, 'k.txt': 83.33}

    def test_search_string_in_file_with_no_match_in_all_files(self):
        file_path = 'testFiles'
        search_string = 'thing here'
        result = self.search.search_string_in_file(file_path, search_string)   
        print(result)
        assert result ==  {'g.txt': 50.0, 'h.txt': 50.0, 'j.txt': 50.0}
    
    def test_match_word_ratio_finder_no_match(self):
        search_string = 'okl'
        file_content = 'kl hj'
        result = self.search.match_word_ratio_finder(search_string,file_content)  
        assert result == [0.0, []]

    def test_match_word_ratio_finder_with_all_match(self):
        search_string = 'to be or'
        file_content = 'any thing here asd to be or be'
        result = self.search.match_word_ratio_finder(search_string,file_content)   
        assert result == [100.0, [1, 2, 1]]

    def test_match_word_ratio_finder_with_half_match(self):
        search_string = 'to be or not '
        file_content = 'any thing here asd to be be'
        result = self.search.match_word_ratio_finder(search_string,file_content)   
        assert result == [50.0, [1, 2]]