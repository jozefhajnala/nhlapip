import unittest
from nhlapip.nhl_minor_endpoints import *
from nhlapip.const import NHLAPI_BASEURL

class TestDivisions(unittest.TestCase):

    def test_divisions_constructor(self):
       divisions = Divisions()
       self.assertEqual(divisions.url, NHLAPI_BASEURL + "divisions")
       self.assertEqual(divisions.endpoint, "divisions")
       self.assertEqual(divisions.suffixes, None)
       self.assertEqual(divisions.data, None)

    def test_divisions_getdata(self):
       divisions = Divisions()
       divisions.get_data()
       self.assertIsInstance(divisions.data, list)
       self.assertTrue(len(divisions.data) > 3)
   
    def test_divisions_getdata_one_division(self):
       divisions = Divisions(15)
       divisions.get_data()
       self.assertIsInstance(divisions.data, list)
       self.assertEqual(len(divisions.data), 1)


class TestConferences(unittest.TestCase):

    def test_conferences_constructor(self):
       conferences = Conferences()
       self.assertEqual(conferences.url, NHLAPI_BASEURL + "conferences")
       self.assertEqual(conferences.endpoint, "conferences")
       self.assertEqual(conferences.suffixes, None)
       self.assertEqual(conferences.data, None)

    def test_conferences_getdata(self):
       conferences = Conferences()
       conferences.get_data()
       self.assertIsInstance(conferences.data, list)
       self.assertTrue(len(conferences.data) > 1)
   
    def test_conferences_getdata_one_conference(self):
       conferences = Conferences(5)
       conferences.get_data()
       self.assertIsInstance(conferences.data, list)
       self.assertEqual(len(conferences.data), 1)



class TestDrafts(unittest.TestCase):

    def test_drafts_constructor(self):
       drafts = Drafts()
       self.assertEqual(drafts.url, NHLAPI_BASEURL + "draft")
       self.assertEqual(drafts.endpoint, "draft")
       self.assertEqual(drafts.suffixes, None)
       self.assertEqual(drafts.data, None)

    def test_drafts_getdata(self):
       drafts = Drafts()
       drafts.get_data()
       self.assertIsInstance(drafts.data, list)
   
    def test_drafts_getdata_one_year(self):
       drafts = Drafts(2019)
       drafts.get_data()
       self.assertIsInstance(drafts.data, list)
       self.assertEqual(len(drafts.data), 1)


class TestSeasons(unittest.TestCase):

    def test_seasons_constructor(self):
       seasons = Seasons()
       self.assertEqual(seasons.url, NHLAPI_BASEURL + "seasons")
       self.assertEqual(seasons.endpoint, "seasons")
       self.assertEqual(seasons.suffixes, None)
       self.assertEqual(seasons.data, None)

    def test_seasons_getdata(self):
       seasons = Seasons()
       seasons.get_data()
       self.assertIsInstance(seasons.data, list)
   
    def test_seasons_getdata_one_season(self):
       seasons = Seasons("20182019")
       seasons.get_data()
       self.assertIsInstance(seasons.data, list)
       self.assertEqual(len(seasons.data), 1)


class TestVenues(unittest.TestCase):

    def test_venues_constructor(self):
       venues = Venues()
       self.assertEqual(venues.url, NHLAPI_BASEURL + "venues")
       self.assertEqual(venues.endpoint, "venues")
       self.assertEqual(venues.suffixes, None)
       self.assertEqual(venues.data, None)

    def test_venues_getdata(self):
       venues = Venues()
       venues.get_data()
       self.assertIsInstance(venues.data, list)
       self.assertTrue(len(venues.data) > 15)
   
    def test_venues_getdata_one_venue(self):
       venues = Venues(5017)
       venues.get_data()
       self.assertIsInstance(venues.data, list)
       self.assertEqual(len(venues.data), 1)


class TestAwards(unittest.TestCase):

    def test_awards_constructor(self):
       awards = Awards()
       self.assertEqual(awards.url, NHLAPI_BASEURL + "awards")
       self.assertEqual(awards.endpoint, "awards")
       self.assertEqual(awards.suffixes, None)
       self.assertEqual(awards.data, None)

    def test_awards_getdata(self):
       awards = Awards()
       awards.get_data()
       self.assertIsInstance(awards.data, list)
       self.assertTrue(len(awards.data) > 20)
   
    def test_awards_getdata_one_award(self):
       awards = Awards(1)
       awards.get_data()
       self.assertIsInstance(awards.data, list)
       self.assertEqual(len(awards.data), 1)



class TestDraftProspects(unittest.TestCase):

    def test_draft_prospects_constructor(self):
       draft_prospects = DraftProspects()
       self.assertEqual(draft_prospects.url, NHLAPI_BASEURL + "draft/prospects")
       self.assertEqual(draft_prospects.endpoint, "draft/prospects")
       self.assertEqual(draft_prospects.suffixes, None)
       self.assertEqual(draft_prospects.data, None)

    def test_draft_prospects_getdata(self):
       draft_prospects = DraftProspects()
       draft_prospects.get_data()
       self.assertIsInstance(draft_prospects.data, list)
       self.assertTrue(len(draft_prospects.data) > 20)
