import unittest
import statements

class Test(unittest.TestCase):

    def test_Lexicon(self):
        m1 = statements.Lexicon()

        # base cases
        m1.add("John", "P")
        m1.add("Mary", "P")
        m1.add("duck", "N")
        m1.add("student", "N")
        m1.add("purple", "A")
        m1.add("old", "A")
        m1.add("fly", "I")
        m1.add("swim", "I")
        m1.add("like", "T")
        m1.add("hit", "T")

        self.assertEquals(m1.getAll("P"), ["John", "Mary"])
        self.assertEquals(m1.getAll("N"), ["duck", "student"])
        self.assertEquals(m1.getAll("A"), ["purple", "old"])
        self.assertEquals(m1.getAll("I"), ["fly", "swim"])
        self.assertEquals(m1.getAll("T"), ["like", "hit"])

        # additional testing
        m1.add("dog", "NN")
        m1.add("cat", "NN")
        m1.add("frog", "NN")
        m1.add("student", "NN")

        m1.add("walk", "VB")
        m1.add("cook", "VB")
        m1.add("smile", "VB")
        m1.add("study", "VB")

        self.assertEquals(m1.getAll("NN"), ["dog", "cat", "frog", "student"])
        self.assertEquals(m1.getAll("VB"), ["walk", "cook", "smile", "study"])
        self.assertEquals(m1.getAll("VBZ"), [])

    def test_FactBase(self):
        fb = statements.FactBase()

        # base cases
        fb.addBinary("love", "John", "Mary")
        fb.addUnary("duck", "John")

        self.assertEquals(fb.queryBinary("love", "Mary", "John"), False)
        self.assertEquals(fb.queryBinary("love", "John", "Mary"), True)
        self.assertEquals(fb.queryUnary("duck", "John"), True)

    def test_verb_stem(self):
        # Rule 1
        self.assertEqual(statements.verb_stem("eats"), "eat")
        self.assertEqual(statements.verb_stem("tells"), "tell")
        self.assertEqual(statements.verb_stem("shows"), "show")

        # Rule 2
        self.assertEqual(statements.verb_stem("pays"), "pay")
        self.assertEqual(statements.verb_stem("buys"), "buy")

        # Rule 3
        self.assertEqual(statements.verb_stem("flies"), "fly")
        self.assertEqual(statements.verb_stem("tries"), "try")
        self.assertEqual(statements.verb_stem("unifies"), "unify")

        # Rule 4
        self.assertEqual(statements.verb_stem("dies"), "die")
        self.assertEqual(statements.verb_stem("lies"), "lie")
        self.assertEqual(statements.verb_stem("ties"), "tie")
        self.assertNotEqual(statements.verb_stem("unties"), "unities")

        # Rule 5
        self.assertEqual(statements.verb_stem("goes"), "go")
        self.assertEqual(statements.verb_stem("boxes"), "box")
        self.assertEqual(statements.verb_stem("attaches"), "attach")
        self.assertEqual(statements.verb_stem("washes"), "wash")
        self.assertEqual(statements.verb_stem("dresses"), "dress")
        #self.assertEqual(statements.verb_stem("fizzes"), "fizz")

        # Rule 6
        self.assertEqual(statements.verb_stem("loses"), "lose")
        # self.assertEqual(statements.verb_stem("dazes"), "daze")
        self.assertEqual(statements.verb_stem("lapses"), "lapse")
        self.assertEqual(statements.verb_stem("analyzes"), "analyze")

        # Rule 7
        # self.assertEqual(statements.verb_stem("has"), "have")

        # Rule 8
        self.assertEqual(statements.verb_stem("likes"), "like")
        self.assertEqual(statements.verb_stem("hates"), "hate")
        self.assertEqual(statements.verb_stem("bathes"), "bathe")

        # Base Case
        self.assertEqual(statements.verb_stem("flys"), "")
        self.assertEqual(statements.verb_stem("inchs"), "")


        # Check whether point 4 of Part 1 was implemented
        self.assertEqual(statements.verb_stem("cats"), "")
        self.assertEqual(statements.verb_stem("Johns"), "")
        self.assertEqual(statements.verb_stem("Marys"), "")
        # self.assertEqual(statements.verb_stem("dogs"), "dog")
        self.assertEqual(statements.verb_stem("doggies"), "")


if __name__ == '__main__':
    unittest.main()
