"""

This program is part of an exercise in
Think Python: An Introduction to Software Design
Allen B. Downey

WARNING: this program contains a NASTY bug.  I put
it there on purpose as a debugging exercise, but
you DO NOT want to emulate this example!

"""


class kangaroo(object):
    """a Kangaroo is a marsupial"""

    def __init__(self, contents=[]):
        """initialize the pouch contents; the default value is
        an empty list"""
        self.pouch_contents = contents

    def __str__(self):
        name = str(self)
        print name, "the contents inside  %s's pouch are:" % name,
        for item in self.pouch_contents:
            print item,

    def put_in_pouch(self, item):
        """
        Put item to pouch_contents
        :param item: An object of any type
        :return: None
        """

        self.pouch_contents.append(item)

if __name__ == "__main__":
    kanga = kangaroo()
    roo = kangaroo()
    kanga.put_in_pouch(roo)
    print kanga