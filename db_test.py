import unittest
from uuid import uuid4

from logs_db import LogsDbInterface

if __name__ == '__main__':
    unittest.main()


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.db = LogsDbInterface("test")

    def tearDown(self) -> None:
        self.db.purge()
        self.db.terminate()

    @unittest.expectedFailure
    def sanity(self):
        self.assertEqual(True, False)

    def test_add_log(self):
        self.db.add_log(uuid4(), 'add_log_test', 0, 0)
        self.assertGreater(self.db.get_logs(0, 0).count(), 0)

    def test_get_log(self):
        self.test_add_log()
        for doc in self.db.get_logs(0,0):
            self.assertEqual(doc, self.db.get_log(doc['uuid']))
