import unittest
from contract import Contract, EmptyStackException

class TestContract(unittest.TestCase):

    def setUp(self):
        self.contract = Contract()
        self.contract.contracts = [1,2,3]

    def test_size(self):
        self.assertEqual(self.contract.size(), 3)

    def test_push(self):
        self.contract.push(4)
        self.assertEqual(self.contract.size(), 4)

    def test_pop(self):
        contract = self.contract.pop()
        self.assertEqual(self.contract.size(),2)
        self.assertEqual(contract, 3)

    def test_peek(self):
        contract = self.contract.peek()
        self.assertEqual(contract, 3)
        self.assertEqual(self.contract.size(), 3)
        self.contract.contracts = []
        with self.assertRaises(EmptyStackException):
            self.contract.peek()

    def test_empty(self):
        self.assertEqual(self.contract.empty(), False)
        self.contract.contracts = []
        self.assertEqual(self.contract.empty(), True)