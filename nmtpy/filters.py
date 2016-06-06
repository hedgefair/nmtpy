class CompoundFilter(object):
    """Filters out fillers from compound splitted sentences."""
    def __init__(self):
        pass

    def __filter(self, s):
        return s.replace(" @@ ", "").replace(" @@", "").replace(" @", "").replace("@ ", "")

    def __call__(self, inp):
        if isinstance(inp, str):
            return self.__filter(inp)
        else:
            return [self.__filter(e) for e in inp]

def get_filter(name):
    filters = {
                "compound"     : CompoundFilter(),
              }
    return filters.get(name, None)
