import collections

def create_vocab_from_file(file_path: str, end_token: str = '_') -> collections.defaultdict:
    """Reads the file path of a text file and returns a dictionary of 
    words with space separated letters and a end of word token with their 
    frequencies.

    Args:
        file_path (str): The path of the text file

    Returns:
        dict: Dictionary of tokens (as key) and their frequencies (as values)
    """
    vocab = collections.defaultdict(int)
    
    with open(file_path, 'rt', encoding='utf-8') as file:
        for line in file:
            words = line.strip().split()
            
            for word in words:
                # Join the letters of a word separeted by a space.
                # Add a `_` at the end. Finally, increase the count 
                # of this token.
                vocab[' '.join(list(word)) + f' {end_token}'] += 1
    return vocab


def get_tokens_from_vocab(vocab: dict) -> list:
    """Reads the vocabularies. Then create count of each individual token. 
    Also creates the token to word map. Finally returns the tokens and its
    frequencies in a dictionary. And token to word map as a dictionary.

    Args:
        vocab (dict): The vocabularies dictionary.

    Returns:
        (dict, dict): Two dictionaries. The first one contains the tokens 
        and their frequencies. The second one contains the token to word map.
    """
    frequencies = collections.defaultdict(int)
    words_to_tokens = {}
    
    for word, count in vocab.items():
        chars = word.split()
        
        for char in chars:
            frequencies[char] += count
        words_to_tokens[''.join(chars)] = chars
    return frequencies, words_to_tokens
    