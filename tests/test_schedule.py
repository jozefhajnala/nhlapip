import unittest
from nhlapip.url import NhlUrl
from nhlapip.schedule import Schedule
from nhlapip.const import NHLAPI_BASEURL

class TestSchedule(unittest.TestCase):

    def test_schedule_constructor(self):
        schedule = Schedule()
        self.assertEqual(schedule.url, NHLAPI_BASEURL + "schedule")
        self.assertEqual(schedule.endpoint, "schedule")
        self.assertEqual(schedule.suffixes, None)
        self.assertEqual(schedule.params, None)
        self.assertEqual(schedule.data, None)

    def test_schedule_constructor_with_season(self):
         schedule = Schedule(season="19931994")
         self.assertEqual(schedule.url, NHLAPI_BASEURL + "schedule?season=19931994")
         self.assertEqual(schedule.endpoint, "schedule")
         self.assertEqual(schedule.suffixes, None)
         self.assertEqual(schedule.params, ["season=19931994"])
         self.assertEqual(schedule.data, None)

    def test_schedule_constructor_with_daterange(self):
         schedule = Schedule(startDate="2018-01-02", endDate="2018-01-02")
         self.assertEqual(schedule.url, NHLAPI_BASEURL + "schedule?startDate=2018-01-02&endDate=2018-01-02")
         self.assertEqual(schedule.endpoint, "schedule")
         self.assertEqual(schedule.suffixes, None)
         self.assertEqual(schedule.params, ["startDate=2018-01-02", "endDate=2018-01-02"])
         self.assertEqual(schedule.data, None)
