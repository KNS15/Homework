import unittest
import M12dz2

calcTS = unittest.TestSuite()
calcTS.addTest(unittest.TestLoader().loadTestsFromTestCase(M12dz2.RunnerTest))
calcTS.addTest(unittest.TestLoader().loadTestsFromTestCase(M12dz2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(calcTS)
