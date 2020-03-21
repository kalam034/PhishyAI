import pandas as pd

from . import url, url_utils


def generate_features():

    dataframe = pd.read_csv(
        "../data/interim/final_merged_dataframes.csv", header=0, low_memory=False)

    dataframe = extract_features(dataframe)

    dataframe.to_csv("../data/processed/features.csv",
                     index=False, header=True)

def extract_features(dataframe):

    print('\n')
    print("Extracting Features")

    dataframe = _extract_url_features_(dataframe)
    dataframe = _extract_domain_features_(dataframe)
    dataframe = _extract_path_features_(dataframe)
    dataframe = _extract_query_features_(dataframe)
    dataframe = _extract_fragment_features(dataframe)
    dataframe = _extract_ext_features(dataframe)
    dataframe = _remove_extra_columns(dataframe)
    dataframe = _drop_null_values(dataframe)

    return dataframe


def _extract_url_features_(dataframe):
    dataframe["url_delimiter_count"] = dataframe["Url"].map(
        lambda x: url_utils.get_delimiter_count(x))
    dataframe["url_digit_count"] = dataframe["Url"].map(
        lambda x: url_utils.get_digit_count(x))
    dataframe["url_letter_count"] = dataframe["Url"].map(
        lambda x: url_utils.get_letter_count(x))
    dataframe["url_symbol_count"] = dataframe["Url"].map(
        lambda x: url_utils.get_symbol_count(x))
    dataframe["url_digit_to_letter_ratio"] = dataframe["Url"].map(
        lambda x: url_utils.get_digit_to_letter_ratio(x))
    dataframe["url_encodes_characters"] = dataframe["Url"].map(
        lambda x: url.encodes_characters(x))
    dataframe["url_uses_https"] = dataframe["Url"].map(
        lambda x: url.uses_https(x))
    dataframe["url_get_port"] = dataframe["Url"].map(
        lambda x: url.get_port(x))
    dataframe["url_uses_default_port_number"] = dataframe["Url"].map(
        lambda x: url.uses_default_port_number(x))

    return dataframe


def _extract_domain_features_(dataframe):
    dataframe["domain"] = dataframe["Url"].map(lambda x: url.get_domain(x))
    dataframe["domain_delimiter_count"] = dataframe["domain"].map(
        lambda x: url_utils.get_delimiter_count(x))
    dataframe["domain_digit_count"] = dataframe["domain"].map(
        lambda x: url_utils.get_digit_count(x))
    dataframe["domain_letter_count"] = dataframe["domain"].map(
        lambda x: url_utils.get_letter_count(x))
    dataframe["domain_symbol_count"] = dataframe["domain"].map(
        lambda x: url_utils.get_symbol_count(x))
    dataframe["domain_digit_to_letter_ratio"] = dataframe["domain"].map(
        lambda x: url_utils.get_digit_to_letter_ratio(x))

    return dataframe


def _extract_path_features_(dataframe):
    dataframe["path"] = dataframe["Url"].map(lambda x: url.get_path(x))
    dataframe["path_delimiter_count"] = dataframe["path"].map(
        lambda x: url_utils.get_delimiter_count(x))
    dataframe["path_digit_count"] = dataframe["path"].map(
        lambda x: url_utils.get_digit_count(x))
    dataframe["path_letter_count"] = dataframe["path"].map(
        lambda x: url_utils.get_letter_count(x))
    dataframe["path_symbol_count"] = dataframe["path"].map(
        lambda x: url_utils.get_symbol_count(x))
    dataframe["path_digit_to_letter_ratio"] = dataframe["path"].map(
        lambda x: url_utils.get_digit_to_letter_ratio(x))

    return dataframe


def _extract_query_features_(dataframe):
    dataframe["query"] = dataframe["Url"].map(lambda x: url.get_query(x))
    dataframe["query_delimiter_count"] = dataframe["query"].map(
        lambda x: url_utils.get_delimiter_count(x))
    dataframe["query_digit_count"] = dataframe["query"].map(
        lambda x: url_utils.get_digit_count(x))
    dataframe["query_letter_count"] = dataframe["query"].map(
        lambda x: url_utils.get_letter_count(x))
    dataframe["query_symbol_count"] = dataframe["query"].map(
        lambda x: url_utils.get_symbol_count(x))
    dataframe["query_digit_to_letter_ratio"] = dataframe["query"].map(
        lambda x: url_utils.get_digit_to_letter_ratio(x))

    dataframe["decoded_query_values"] = dataframe["Url"].map(
        lambda x: url.get_decoded_query_values(x))

    dataframe["total_query_value_length"] = dataframe["decoded_query_values"].map(
        lambda x: url.get_total_query_value_length(x))
    dataframe["avg_query_value_length"] = dataframe["decoded_query_values"].map(
        lambda x: url.get_average_query_value_length(x))
    dataframe["max_query_value_length"] = dataframe["decoded_query_values"].map(
        lambda x: url.get_max_query_value_length(x))
    dataframe["total_query_value_digit_count"] = dataframe["decoded_query_values"].map(
        lambda x: url.get_total_query_value_digit_count(x))
    dataframe["avg_query_value_digit_count"] = dataframe["decoded_query_values"].map(
        lambda x: url.get_average_query_value_digit_count(x))
    dataframe["total_query_value_digit_count"] = dataframe["decoded_query_values"].map(
        lambda x: url.get_total_query_value_letter_count(x))
    dataframe["avg_query_value_letter_count"] = dataframe["decoded_query_values"].map(
        lambda x: url.get_average_query_value_letter_count(x))
    dataframe["total_query_value_symbol_count"] = dataframe["decoded_query_values"].map(
        lambda x: url.get_total_query_value_symbol_count(x))
    dataframe["avg_query_value_symbol_count"] = dataframe["decoded_query_values"].map(
        lambda x: url.get_average_query_value_symbol_count(x))

    dataframe["total_query_variable_length"] = dataframe["Url"].map(
        lambda x: url.get_total_query_variable_length(x))
    dataframe["avg_query_variable_length"] = dataframe["Url"].map(
        lambda x: url.get_average_query_variable_length(x))
    dataframe["max_query_variable_length"] = dataframe["Url"].map(
        lambda x: url.get_max_query_variable_length(x))
    dataframe["total_query_variable_digit_count"] = dataframe["Url"].map(
        lambda x: url.get_total_query_variable_digit_count(x))
    dataframe["avg_query_variable_digit_count"] = dataframe["Url"].map(
        lambda x: url.get_average_query_variable_digit_count(x))
    dataframe["total_query_variable_digit_count"] = dataframe["Url"].map(
        lambda x: url.get_total_query_variable_letter_count(x))
    dataframe["avg_query_variable_letter_count"] = dataframe["Url"].map(
        lambda x: url.get_average_query_variable_letter_count(x))
    dataframe["total_query_variable_symbol_count"] = dataframe["Url"].map(
        lambda x: url.get_total_query_variable_symbol_count(x))
    dataframe["avg_query_variable_symbol_count"] = dataframe["Url"].map(
        lambda x: url.get_average_query_variable_symbol_count(x))

    return dataframe


def _extract_fragment_features(dataframe):
    dataframe["fragment"] = dataframe["Url"].map(
        lambda x: url.get_fragment(x))
    dataframe["fragment_delimiter_count"] = dataframe["fragment"].map(
        lambda x: url_utils.get_delimiter_count(x))
    dataframe["fragment_digit_count"] = dataframe["fragment"].map(
        lambda x: url_utils.get_digit_count(x))
    dataframe["fragment_letter_count"] = dataframe["fragment"].map(
        lambda x: url_utils.get_letter_count(x))
    dataframe["fragment_symbol_count"] = dataframe["fragment"].map(
        lambda x: url_utils.get_symbol_count(x))
    dataframe["fragment_digit_to_letter_ratio"] = dataframe["fragment"].map(
        lambda x: url_utils.get_digit_to_letter_ratio(x))

    return dataframe


def _extract_ext_features(dataframe):
    dataframe["file_ext"] = dataframe["Url"].map(
        lambda x: url.extract_file_ext(x))
    dataframe["file_ext_delimiter_count"] = dataframe["file_ext"].map(
        lambda x: url_utils.get_delimiter_count(x))
    dataframe["file_ext_digit_count"] = dataframe["file_ext"].map(
        lambda x: url_utils.get_digit_count(x))
    dataframe["file_ext_letter_count"] = dataframe["file_ext"].map(
        lambda x: url_utils.get_letter_count(x))
    dataframe["file_ext_symbol_count"] = dataframe["file_ext"].map(
        lambda x: url_utils.get_symbol_count(x))
    dataframe["file_ext_digit_to_letter_ratio"] = dataframe["file_ext"].map(
        lambda x: url_utils.get_digit_to_letter_ratio(x))
    dataframe["file_ext_is_executable"] = dataframe["file_ext"].map(
        lambda x: url_utils.get_digit_to_letter_ratio(x))

    return dataframe


def _remove_extra_columns(dataframe):
    dataframe = dataframe.drop(
        ["Url", "domain", "query", "path", "file_ext", "fragment", "decoded_query_values"], axis=1)

    return dataframe


def _drop_null_values(dataframe):
    return dataframe.dropna()
