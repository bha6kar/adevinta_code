import sys,os
import collections

class Simple_search:
    def search_string_in_file(self,file_path,search_string):
        file_names = os.listdir(file_path)
        filename_with_score = {}
        for file_name in file_names:   
            with open(file_path + '/' + file_name, 'r') as f:
                lines = ''
                for line in f:
                    lines = lines + ' ' + line
                match_string_ratio = self.match_word_ratio_finder(search_string,lines)
                filename_with_score [file_name] = match_string_ratio
        sorted_filename_with_score = sorted(filename_with_score.items(), key=lambda kv: kv[1], reverse = True)
        top10_filename_with_score_list = sorted_filename_with_score[0:10]
        top10_filename_with_score_dict = collections.OrderedDict(top10_filename_with_score_list)
        top10_filename_with_score_dict_non_zero = {key:val for key, val in top10_filename_with_score_dict.items() if val != [0.0, []]}
        if len(top10_filename_with_score_dict_non_zero) == 0:
            return 0
        top10_filename_with_score_dict= {}
        for file_name, search_match_score in top10_filename_with_score_dict_non_zero.items():
            top10_filename_with_score_dict.__setitem__(file_name, search_match_score[0])
        return top10_filename_with_score_dict

    def match_word_ratio_finder(self, search_string, file_content):
        result = []
        match_occurenc_list = []
        search_string_splitted = search_string.split()
        match_count = 0
        file_content_list = file_content.split()
        
        for i in search_string_splitted:
            if i in file_content_list:
                match_occurenc = file_content_list.count(i)
                match_count = match_count + 1
                match_occurenc_list.append(match_occurenc)
        
        y = len(search_string_splitted)
        match_ratio = round((match_count/y) * 100.0,2)
        result.append(match_ratio)
        result.append(match_occurenc_list)
        return result

    def main(self):
        file_path = sys.argv[1]
        while True:
            search_string = ''
            try:
                search_string = input("search>")
            except:
                pass
            if search_string == "":
                break
            elif search_string == ":quit":
                break
            top10_filename_with_score_dict = self.search_string_in_file(file_path, search_string)
            
            if top10_filename_with_score_dict == 0:
                print('no matches found')
            else:
                for file_name, search_match_score in top10_filename_with_score_dict.items(): 
                    print(file_name, ":", search_match_score)

if __name__ == "__main__":
    search_string_in_file = Simple_search()
    search_string_in_file.search_string_in_file('test/testFiles','to be or not to be')
    search_string_in_file.main()