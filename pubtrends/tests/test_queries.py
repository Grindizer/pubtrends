# -*- encoding: utf8 -*-
__author__ = 'nacim'


from eutils.queryservice import QueryService
import types
from pubtrends.queries import queries, QueryError
from mock import patch
import unittest
import fixtures as fx

class QueriesTest(unittest.TestCase):

    def test_pub_locations_ok(self):
        with patch.object(QueryService, 'esearch') as mock_search:
            with patch.object(QueryService, 'efetch') as mock_fetch:
                mock_search.return_value = fx.dummy_search_result
                mock_fetch.return_value = fx.dummy_fetch_result

                result = queries.pubmed_locations(start=2008, stop=2014, term='test')

                self.assertIsInstance(result, types.GeneratorType)
                res = list(result)
                self.assertEqual(len(res), 1)
                expected = [{'count': 2, 'country': 'united states'}]
                self.assertEqual(res, expected)

    def test_pub_locations_error(self):
        with patch.object(QueryService, 'esearch') as mock:
            mock.return_value = fx.dummy_error
            result = queries.pubmed_locations(start=2010,
                                                   stop=2012,
                                                   term='test')

            try:
                next(result)
            except QueryError as e:
                pass
            else:
                self.assertFalse(True, "Exception should be Raised as QueryError")


