import collections

def create_vocab_from_file(file_path: str):
    """Reads the file path of a text file and returns a dictionary of 
    tokens and their frequencies.

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
                vocab[' '.join(list(word)) + '_'] += 1
    return vocab