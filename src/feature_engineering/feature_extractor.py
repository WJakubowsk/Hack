import numpy as np
import pandas as pd
from thefuzz import fuzz
from typing import List

class FeatureExtractor:
    def __init__(self, df):
        self.df = df
    
    @staticmethod
    def _fuzzy_match_string(string_list: List[str], term: str):
        return max([fuzz.ratio(string, term) for string in string_list])
    
    def get_binary_str_col(self, text_col: str, term: str, fuzzy_match_threshold: float):
        """
        extracts information about presents of certain term within the data string. Uses Fuzzy matching for
        imperfect matches. Creates new binary column in the dataset, which represents the presence of the desired term
        """
        self.df[term] = self.df[text_col].apply(lambda x: 1 if (term in x) or (self._fuzzy_match_string(x, term) > fuzzy_match_threshold) else 0)
    
    def feature_engineering(self, text_col: str, terms: List[str], fuzzy_match_treshold: float):
        for term in terms:
            print('extracting feature for term ', term)
            self.get_binary_str_col(text_col=text_col, term=term, fuzzy_match_threshold=fuzzy_match_treshold)
    
