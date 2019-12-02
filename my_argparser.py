import argparse

def argParserTest():
    parser = argparse.ArgumentParser()
    parser.add_argument('--foo',help='%(prog)s help information')
    args = parser.parse_args()

def argParserTest_PROG():
    pparser = argparse.ArgumentParser(add_help=False)
    pparser.add_argument('--foo',help='%(prog)s help information')
    parser = argparse.ArgumentParser(prog='argParserTest_PROG',
                                     # usage='%(prog)s dirs',
                                     description='this program use for switch dirs',
                                     epilog='and this is the epilog info',parents=[pparser])
    parser.add_argument('--first',help='%(prog)s first args')
    parser.add_argument('--second',type=str,help='%(prog)s second args')
    parser.add_argument('-s',action='store_const',const=1)
    parser.add_argument('-t',action='store_true')
    parser.add_argument('-f',action='store_false')
    parser.add_argument('--some_list',action='append')
    parser.add_argument('--verbose','-v',action='count',default=0)
    parser.add_argument('--version',action='version',version='%(prog)s 1.0')
    parser.add_argument('position_p')
    args = parser.parse_args()
    # parser.print_help()

if __name__ == '__main__':
    # argParserTest()
    print('**************************')
    argParserTest_PROG()