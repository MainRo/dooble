import tatsu

grammar = '''
    @@grammar::dooble

    start = { layer } $ ;

    layer
    =
    | obs:observable
    | op:operator
    ;


    observable = {skipspan}* [prefix] {lifetime}* completion ;
    operator = '[' description ']' ;

    prefix = '+' | label ;

    label = /[a-z]/ ;

    lifetime
    =
    | ts:timespan
    | item:item
    ;

    completion = /[>|\*]/ ;

    skipspan = ' ' ;
    timespan = '-' ;
    item = /[a-zA-Z0-9+]+/ ;


    description = /[a-zA-Z0-9,:+*() ]+/ ;
'''


class Idl(object):
    def __init__(self):
        self.model = tatsu.compile(grammar)

    def parse(self, text):
        ast = self.model.parse(text, whitespace='\n')
        return ast
