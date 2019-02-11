import tatsu

grammar = '''
    @@grammar::dooble

    start = { layer } $ ;

    layer
    =
    | obs:observable
    | op:operator
    ;


    observable = {skipspan}* {lifetime}* completion ;
    operator = '[' description ']' ;

    lifetime 
    =
    | ts:timespan
    | item:item
    ;

    completion = /[>|\*]/ ;

    skipspan = ' ' ;
    timespan = '-' ;
    item = /[a-zA-Z0-9]+/ ;

    description = /[a-zA-Z0-9,:+*() ]+/ ;
'''


class Idl(object):
    def __init__(self):
        self.model = tatsu.compile(grammar)

    def parse(self, text):
        ast = self.model.parse(text, whitespace='\n')
        return ast
