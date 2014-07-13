def digits(n, base):
    if not isinstance(n, (int, long)):
        raise ValueError('Arg n must be an int or long, got {}'.format(type(n)))
    if n < 0:
        raise ValueError('Arg n must not be less than 0.')
    if not isinstance(base, (int, long)):
        raise ValueError('Arg base must be an int or long, got {}'.format(type(base)))
    if base < 2:
        raise ValueError('Base must be greater than 2.')
    if n == 0:
        return [0]
    l = []
    while n > 0:
        n, r = divmod(n, base)
        l.append(r)
    return l[::-1]

def _ab_requirements(f):
    def aux(n, ab):
        if '__getitem__' not in dir(ab):
            raise ValueError('Can\'t __getitem__ on argument ab.')
        if len(set(ab)) != len(ab):
            raise ValueError('Duplicate items in arg ab.')
        if len(ab) < 2:
            raise ValueError('Arg ab is too short. len(ab) = {}'.format(len(ab)))
        return f(n, ab)
    return aux

@_ab_requirements
def ntos(n, ab):
    if not isinstance(n, (int, long)):
        raise ValueError('Arg n must be an int or long, got {}'.format(type(n)))
    d = digits(n, len(ab))
    str_ab = [str(x) for x in ab]
    return ''.join([str_ab[x] for x in d])

@_ab_requirements
def ston(s, ab):
    if not set(s).issubset(set(ab)):
        raise ValueError('Arg s contains characters not present in alphabet')
    n = 0
    base = len(ab)
    for i, v in enumerate(s[::-1]):
        n += ab.index(v) * (base**i)
    return n