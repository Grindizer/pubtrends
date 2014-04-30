__author__ = 'nacim'


from eutils.client import Client

class QueryError(Exception):
    pass

class EutilsQueries(object):
    def __init__(self, client=None):
        self.client = client or Client(cache_path=None, )

    def pubmed_count_per_year(self, start, stop, term,
                              db='pubmed', datetype='pdat'):

        for dt in xrange(start, stop + 1):
            result = self.client.esearch(db=db, term=term, datetype=datetype,
                                         mindate=dt, maxdate=dt,
                                         retmax=1)

            res = {'year': dt, 'count': result.count}
            yield res

    def pubmed_locations(self, start, stop, term,
                         db='pubmed', datetype='pdat'):

        return self._pubmed_attributes(start, stop, term,
                                       db=db, datetype=datetype,
                                       attribute='country')

    def _pubmed_attributes(self, start, stop, term,
                              db='pubmed', datetype='pdat',
                              attribute='country'):
        try:
            # check result count.
            result = self.client.esearch(db=db, term=term, datetype=datetype,
                                         mindate=start, maxdate=stop,
                                         retmax=1, usehistory='y')
            count = result.count
            webenv = result.webenv
            qk = result.query_key

            # max ret value 10000
            data = {}
            for retstart in xrange(0, count, 10000):
                pubs = self.client.efetch(db=db, webenv=webenv, query_key=qk,
                                          retmax=10000, retstart=retstart)
                for article in pubs:
                    value = getattr(article, attribute)
                    year = int(article.year)
                    if start <= year <= stop and value:
                        value = value.lower()
                        if value in data:
                            data[value] += 1
                        else:
                            data[value] = 1

            for key, occ in data.items():
                yield {attribute: key, 'count': occ}

        except Exception as e:
            raise QueryError(str(e))


queries = EutilsQueries()