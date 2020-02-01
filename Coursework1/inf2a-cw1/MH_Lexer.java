
// File:   MH_Lexer.java
// Date:   October 2013, subsequently modified each year.

// Java template file for lexer component of Informatics 2A Assignment 1.
// Concerns lexical classes and lexer for the language MH (`Micro-Haskell').


import java.io.* ;

class MH_Lexer extends GenLexer implements LEX_TOKEN_STREAM {

static class VarAcceptor extends Acceptor implements DFA {
    public String lexClass() { return "VAR"; }
    public int numberOfStates() {return 3 ;}
    
    int next (int state, char c) {
    	switch(state) {
    	case 0: if(CharTypes.isSmall(c)) return 1 else return 2 ; //small
    	case 1: if (CharTypes.isSmall(c)||
    			    CharTypes.isLarge(c)||
    			    CharTypes.isDigit(c)|| 
    			    c == '\'') return 1 else return 2 ;  //(small +large+digit + ')*
               default: return 2 ; //garbage state
    	}
    }
    boolean accepting (int state) {return (state == 2) ;}
    int dead () {return 2 ;}//garabge state
}

static class NumAcceptor extends Acceptor implements DFA {
    public String lexClass() { return "NUM" ; }
    public int numberOfStates( ) {return 3 ;}
    
    int next (int state, char c) {
    	switch(state) {
    	case 0: if(c =='0') return 1 else return 2 ; //0
    	case 0: if (CharTypes.isDigit(c) && c!= '0') return 1 else return 2 ; //nonZeroDigit digit *
    	case 1: if (CharTypes.isDigit(c)) return 1 else return 2 ;                                     
        	default: return 2 ; //garbage state
    	}
    }
    boolean accepting (int state) {return (state == 1) ;}
    int dead () {return 2 ;}//garabge state
    
}

static class BooleanAcceptor extends Acceptor implements DFA {
	public String lexClass() { return "BOOLEAN" ; }
    public int numberOfStates() {return 10 ;}
    
    int next (int state, char c) {
    	switch(state) {
    	case 0: if(c=='T') return 1 else return 9 ; //T
    	case 0: if(c=='F') return 5 else return 9 ; //F
    	case 1: if(c=='r') return 2 else return 9 ; //Tr
    	case 2: if(c=='u') return 3 else return 9 ; //Tru
    	case 3: if(c=='e') return 4 else return 9 ; //True
    	case 5 :if(c=='a') return 6 else return 9 ; //Fa
    	case 6: if(c=='l') return 7 else return 9 ; //Fal
    	case 7: if(c=='s') return 8 else return 9 ; //Fals
    	case 8: if(c=='e') return 4 else return 9 ; //False
    	}
    }
    boolean accepting (int state) {return (state == 4) ;}
    int dead () {return 9 ;}//garabge state
}
	
}

static class SymAcceptor extends Acceptor implements DFA {
	public String lexClass() { return "SYM" ; }
    public int numberOfStates() {return 3 ;}
    
    int next (int state, char c) {
    	switch(state) {
    	case 0: if(CharTypes.isSymbolic(c)) return 1 else return 2 ; //symbolic
    	case 1: if(CharTypes.isSymbolic(c)) return 1 else return 2 ;// symbolic*                            
        	default: return 2 ; //garbage state
    	}
    }
    boolean accepting (int state) {return (state == 1) ;}
    int dead () {return 2 ;}//garabge state
}

static class WhitespaceAcceptor extends Acceptor implements DFA {
    public String lexClass() { return "WHITESPACE" ; }
    public int numberOfStates() {return 3 ; }
    
    int next(int state, char c) {
    	switch(state) {
    	case 0: if(CharTypes.isWhitespace(c)) return 1 else return 2 ; //whitespace
    	case 1: if(CharTypes.isWhiteSpace(c)) return 1 else return 2 ;//whitespace*
        	default: return 2 ;
    	}
    }
    boolean accepting(int state) {return (state==1) ;}
    int dead () {return 2 ;} //garabge state
}

static class CommentAcceptor extends Acceptor implements DFA {
	public String lexClass() { return "COMMENT" ; }
    public int numberOfStates() { return 5 ; }
    
    int next(int state, char c) {
    	switch(state) {
    	case 0: if(c== '-') return 1 else return 4 ; //-
    	case 1: if(c== '-') return 2 else return 4 ; //-
    	case 2: if(c== '-') return 2 else return 4 ; //-*
    	case 2: if(String.valueOf(c)== "")   return 3 else return 4 ; //emptystring
    	case 2: if(!CharTypes.isSymbolic(c)) return 3 else return 4 ; //nonSymbolNewline
    	case 3: if(!CharTypes.isNewLine(c))  return 3 else return 4 ; //nonNewline*
        	default: return 4 ;
    	}
    }
    boolean accepting(int state) {return (state==3) ;}
    int dead () {return 4 ;} //garabge state
}
}

static class TokAcceptor extends Acceptor implements DFA {

    String tok ;
    int tokLen ;
    TokAcceptor (String tok) {this.tok = tok ; tokLen = tok.length() ;}
    public String lexClass() { return tok ; }
    public int numberOfStates() { return tokLen+2 ;} // include garabge state and accepting state
    
    int next (int state, char c) {
    	if(c == tok.charAt(state))) return state +1 else return tok.length +1 ;
    	
    }
    boolean accpeting(int state) { return (state==tok.length) ;}  //when the string is completed
    int dead () {return tok.length+1;}//garbage state

}

	static DFA integerAcc = new TokenAcceptor("Integer") ;
	static DFA boolAcc = new TokenAcceptor("Bool") ;
	static DFA ifAcc = new TokenAcceptor("if") ;
	static DFA thenAcc = new TokenAcceptor("then") ;
	static DFA elseAcc = new TokenAcceptor("else") ;
	static DFA oBracketAcc = new TokenAcceptor("(") ;
	static DFA cBracketAcc = new TokenAcceptor(")") ;
	static DFA sColonAcc = new TokenAcceptor(";") ;
	static DFA varAcc = new VarAcceptor() ;
	static DFA numAcc = new NumAcceptor() ;
	static DFA booleanAcc = new BooleanAcceptor() ;
	static DFA whitespaceAcc = new WhitespaceAcceptor() ;
	static DFA commentAcc = new CommentAcceptor() ;
    static DFA[] acceptors = 
	
    DFA[] MH_acceptors = new DFA[] {integerAcc, boolAcc, ifAcc, thenAcc, elseAcc, oBracketAcc, cBracketAcc, sColonAcc, varAcc, numAcc, booleanAcc, whitespaceAcc, commentAcc   } ;
    DemoLexer (Reader reader) {
	super(reader,acceptors) ;
    }


    MH_Lexer (Reader reader) {
	super(reader,MH_acceptors) ;
    }

}

