expected = """\
              {InputFile} "example_01.o"
[0x0000000b]     {CompileUnit} "example_01.cpp"

              {Source} "example_01.cpp"
[0x00000026]  2    {Function} "foo" -> [0x00000000]"void"
                       - No declaration
[0x00000043]  2      {Parameter} "c" -> [0x00000060]"char"
[0x00000051]  4      {Variable} "i" -> [0x00000067]"int"
"""


def test(diva):
    assert diva('--show-DWARF-offset example_01.o') == expected
