# skip-if: '-x' in EXTRA_JIT_ARGS
# allow-warning: import level 0 will be treated as -1

print repr(unicode())
print repr(unicode('hello world'))

# Some random unicode character:
u = u'\u0180'
print len(u)
print repr(u)
print repr(u.encode("utf8"))

# This is tricky, since we need to support file encodings, and then set stdout to UTF8:
# print u

d = {}
d["hello world"] = "hi"
print d[u"hello world"]

class C(object):
    pass
c = C()
c.a = 1
print hasattr(c, 'a')
print hasattr(c, u'a')
print u'a' in c.__dict__
print u'' == ''
print '' == u''
print hash(u'') == hash('')

try:
    hasattr(object(), u"\u0180")
except UnicodeEncodeError as e:
    print e

def p(x):
    return [hex(ord(i)) for i in x]
s = u"\u20AC" # euro sign
print p(s) 
print p(s.encode("utf8"))
print p(s.encode("utf16"))
print p(s.encode("utf32"))
print p(s.encode("iso_8859_15"))

print repr(u' '.join(["hello", "world"]))

# GC test: the unicode module interns certain unicode strings (the empty string among them).
# Make sure we don't end up GCing it.
# Call BaseException().__unicode__() since that happens to be one of the ways to access
# the interned empty string ("unicode_empty")
import gc
for i in xrange(100):
    print repr(BaseException().__unicode__())
    gc.collect()
    # do some allocations:
    for j in xrange(100):
        [None] * j
