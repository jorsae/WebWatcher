from exceptions import TypeException

def replace_string(original_text, find_text, replace_text):
    if type(original_text) != str or type(find_text) != str or type(replace_text) != str:
        raise TypeException(f'{type(text)=} {type(replace_text)=}')
    
    return original_text.replace(find_text, replace_text)

def create_substring(original_text, front=None, back=None):
    return original_text[front:back]