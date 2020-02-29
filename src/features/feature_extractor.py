from features import url_utils
from features import url


class feature_extractor:

    def __init__(self, dataframe):
        self.dataframe = dataframe

    def extract_features(self):
        self._extract_url_features_()
        self._extract_domain_features_()
        self._extract_path_features_()
        self._extract_query_features_()
        self._extract_fragment_features()
        self._extract_ext_features()

        return self.dataframe

    def _extract_url_features_(self):
        self.dataframe["url_delimiter_count"] = self.dataframe["Url"].map(lambda x: url_utils.get_delimiter_count(x))
        self.dataframe["url_digit_count"] = self.dataframe["Url"].map(lambda x: url_utils.get_digit_count(x))
        self.dataframe["url_letter_count"] = self.dataframe["Url"].map(lambda x: url_utils.get_letter_count(x))
        self.dataframe["url_symbol_count"] = self.dataframe["Url"].map(lambda x: url_utils.get_symbol_count(x))
        self.dataframe["url_digit_to_letter_ratio"] = self.dataframe["Url"].map(
            lambda x: url_utils.get_digit_to_letter_ratio(x))
        self.dataframe["url_encodes_characters"] = self.dataframe["Url"].map(lambda x: url.encodes_characters(x))
        self.dataframe["url_uses_https"] = self.dataframe["Url"].map(lambda x: url.uses_https(x))
        self.dataframe["url_get_port"] = self.dataframe["Url"].map(lambda x: url.get_port(x))
        self.dataframe["url_uses_default_port_number"] = self.dataframe["Url"].map(
            lambda x: url.uses_default_port_number(x))

    def _extract_domain_features_(self):
        self.dataframe["domain"] = self.dataframe["Url"].map(lambda x: url.get_domain(x))
        self.dataframe["domain_delimiter_count"] = self.dataframe["domain"].map(
            lambda x: url_utils.get_delimiter_count(x))
        self.dataframe["domain_digit_count"] = self.dataframe["domain"].map(lambda x: url_utils.get_digit_count(x))
        self.dataframe["domain_letter_count"] = self.dataframe["domain"].map(lambda x: url_utils.get_letter_count(x))
        self.dataframe["domain_symbol_count"] = self.dataframe["domain"].map(lambda x: url_utils.get_symbol_count(x))
        self.dataframe["domain_digit_to_letter_ratio"] = self.dataframe["domain"].map(
            lambda x: url_utils.get_digit_to_letter_ratio(x))

    def _extract_path_features_(self):
        self.dataframe["path"] = self.dataframe["Url"].map(lambda x: url.get_path(x))
        self.dataframe["path_delimiter_count"] = self.dataframe["path"].map(lambda x: url_utils.get_delimiter_count(x))
        self.dataframe["path_digit_count"] = self.dataframe["path"].map(lambda x: url_utils.get_digit_count(x))
        self.dataframe["path_letter_count"] = self.dataframe["path"].map(lambda x: url_utils.get_letter_count(x))
        self.dataframe["path_symbol_count"] = self.dataframe["path"].map(lambda x: url_utils.get_symbol_count(x))
        self.dataframe["path_digit_to_letter_ratio"] = self.dataframe["path"].map(
            lambda x: url_utils.get_digit_to_letter_ratio(x))

    def _extract_query_features_(self):
        self.dataframe["query"] = self.dataframe["Url"].map(lambda x: url.get_query(x))
        self.dataframe["query_delimiter_count"] = self.dataframe["query"].map(
            lambda x: url_utils.get_delimiter_count(x))
        self.dataframe["query_digit_count"] = self.dataframe["query"].map(lambda x: url_utils.get_digit_count(x))
        self.dataframe["query_letter_count"] = self.dataframe["query"].map(lambda x: url_utils.get_letter_count(x))
        self.dataframe["query_symbol_count"] = self.dataframe["query"].map(lambda x: url_utils.get_symbol_count(x))
        self.dataframe["query_digit_to_letter_ratio"] = self.dataframe["query"].map(
            lambda x: url_utils.get_digit_to_letter_ratio(x))

        self.dataframe["decoded_query_values"] = self.dataframe["Url"].map(lambda x: url.get_decoded_query_values(x))

        self.dataframe["total_query_value_length"] = self.dataframe["decoded_query_values"].map(
            lambda x: url.get_total_query_value_length(x))
        self.dataframe["avg_query_value_length"] = self.dataframe["decoded_query_values"].map(
            lambda x: url.get_average_query_value_length(x))
        self.dataframe["max_query_value_length"] = self.dataframe["decoded_query_values"].map(
            lambda x: url.get_max_query_value_length(x))
        self.dataframe["total_query_value_digit_count"] = self.dataframe["decoded_query_values"].map(
            lambda x: url.get_total_query_value_digit_count(x))
        self.dataframe["avg_query_value_digit_count"] = self.dataframe["decoded_query_values"].map(
            lambda x: url.get_average_query_value_digit_count(x))
        self.dataframe["total_query_value_digit_count"] = self.dataframe["decoded_query_values"].map(
            lambda x: url.get_total_query_value_letter_count(x))
        self.dataframe["avg_query_value_letter_count"] = self.dataframe["decoded_query_values"].map(
            lambda x: url.get_average_query_value_letter_count(x))
        self.dataframe["total_query_value_symbol_count"] = self.dataframe["decoded_query_values"].map(
            lambda x: url.get_total_query_value_symbol_count(x))
        self.dataframe["avg_query_value_symbol_count"] = self.dataframe["decoded_query_values"].map(
            lambda x: url.get_average_query_value_symbol_count(x))

        self.dataframe["total_query_variable_length"] = self.dataframe["Url"].map(
            lambda x: url.get_total_query_variable_length(x))
        self.dataframe["avg_query_variable_length"] = self.dataframe["Url"].map(
            lambda x: url.get_average_query_variable_length(x))
        self.dataframe["max_query_variable_length"] = self.dataframe["Url"].map(
            lambda x: url.get_max_query_variable_length(x))
        self.dataframe["total_query_variable_digit_count"] = self.dataframe["Url"].map(
            lambda x: url.get_total_query_variable_digit_count(x))
        self.dataframe["avg_query_variable_digit_count"] = self.dataframe["Url"].map(
            lambda x: url.get_average_query_variable_digit_count(x))
        self.dataframe["total_query_variable_digit_count"] = self.dataframe["Url"].map(
            lambda x: url.get_total_query_variable_letter_count(x))
        self.dataframe["avg_query_variable_letter_count"] = self.dataframe["Url"].map(
            lambda x: url.get_average_query_variable_letter_count(x))
        self.dataframe["total_query_variable_symbol_count"] = self.dataframe["Url"].map(
            lambda x: url.get_total_query_variable_symbol_count(x))
        self.dataframe["avg_query_variable_symbol_count"] = self.dataframe["Url"].map(
            lambda x: url.get_average_query_variable_symbol_count(x))

    def _extract_fragment_features(self):
        self.dataframe["fragment"] = self.dataframe["Url"].map(lambda x: url.get_fragment(x))
        self.dataframe["fragment_delimiter_count"] = self.dataframe["fragment"].map(
            lambda x: url_utils.get_delimiter_count(x))
        self.dataframe["fragment_digit_count"] = self.dataframe["fragment"].map(lambda x: url_utils.get_digit_count(x))
        self.dataframe["fragment_letter_count"] = self.dataframe["fragment"].map(
            lambda x: url_utils.get_letter_count(x))
        self.dataframe["fragment_symbol_count"] = self.dataframe["fragment"].map(
            lambda x: url_utils.get_symbol_count(x))
        self.dataframe["fragment_digit_to_letter_ratio"] = self.dataframe["fragment"].map(
            lambda x: url_utils.get_digit_to_letter_ratio(x))

    def _extract_ext_features(self):
        self.dataframe["file_ext"] = self.dataframe["Url"].map(lambda x: url.extract_file_ext(x))
        self.dataframe["file_ext_delimiter_count"] = self.dataframe["file_ext"].map(
            lambda x: url_utils.get_delimiter_count(x))
        self.dataframe["file_ext_digit_count"] = self.dataframe["file_ext"].map(lambda x: url_utils.get_digit_count(x))
        self.dataframe["file_ext_letter_count"] = self.dataframe["file_ext"].map(
            lambda x: url_utils.get_letter_count(x))
        self.dataframe["file_ext_symbol_count"] = self.dataframe["file_ext"].map(
            lambda x: url_utils.get_symbol_count(x))
        self.dataframe["file_ext_digit_to_letter_ratio"] = self.dataframe["file_ext"].map(
            lambda x: url_utils.get_digit_to_letter_ratio(x))
        self.dataframe["file_ext_is_executable"] = self.dataframe["file_ext"].map(
            lambda x: url_utils.get_digit_to_letter_ratio(x))
