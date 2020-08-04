import unittest
from time import sleep

from timers import *


class MyTestCase(unittest.TestCase):
    def test_timer_start(self):
        uid = start_timer('start test')
        self.assertGreater(timers[uid][-1], 0)
        self.assertGreater(datetime.now().timestamp(), timers[uid][-1])

    def test_timer(self):
        uid = start_timer('timer test')
        sleep(10)
        res = stop_timer(uid)[-1]
        self.assertEqual(res, 11.0)

    def test_pause_resume(self):
        uid = start_timer('pause resume test')
        sleep(3)
        pause_timer(uid)
        sleep(3)
        resume_timer(uid)
        sleep(3)
        res = stop_timer(uid)[-1]
        self.assertEqual(res, 7.0)

    def test_resume(self):
        uid = start_timer('resume test')
        self.assertFalse(resume_timer(uid))

    def test_pause(self):
        uid = start_timer('pause test')
        self.assertTrue(pause_timer(uid))
        self.assertFalse(pause_timer(uid))



if __name__ == '__main__':
    unittest.main()
