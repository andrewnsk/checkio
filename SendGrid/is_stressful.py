import itertools


def is_stressful(subj):
    """
        recoognise stressful subject
        "help", "asap", "urgent".
        Any of those "red" words can be spelled in different ways -
            "HELP", "help", "HeLp", "H!E!L!P!", "H-E-L-P", even in a very loooong way "HHHEEEEEEEEELLP"
        Input: Subject line as a string
        Output: Boolean.
        Precondition: subject can be up to 100 letters
    """
    stress = 0
    red_words = 'help', 'asap', 'urgent'
    if '!!!!' in subj or subj.isupper():
        stress += 1
    string = subj.lower().replace('!', '').replace('-', '').replace('.', '').split(' ')
    clear_data = [''.join(ch for ch, _ in itertools.groupby(x)) for x in string]
    for word in red_words:
        if word in clear_data:
            stress += 2
    if stress > 0:
        return True
    return False

"""
def is_stressful(subj):
    return (subj.isupper() or
            subj.endswith('!!!') or
            any(re.search('+[.!-]*'.join(word), subj.lower())
                for word in ['help', 'asap', 'urgent']))

"""
if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_stressful("Hi") is False, "First"
    assert is_stressful("I neeed HELP") is True, "Second"
    print('Done! Go Check it!')
