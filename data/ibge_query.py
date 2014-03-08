# -*- coding: utf-8 -*-

import sys
import urllib2

from BeautifulSoup import BeautifulSoup
Soup = BeautifulSoup

import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf8')

class NameGenerator:

    def __init__(self):

        self._pattern = '%s.csv'

        self.__uf_s = [
            'ac',# Acre
            'al',# Alagoas
            'ap',# Amapá
            'am',# Amazonas
            'ba',# Bahia
            'ce',# Ceará
            'df',# Distrito Federal
            'es',# Espírito Santo
            'go',# Goiás
            'ma',# Maranhão
            'mt',# Mato Grosso
            'ms',# Mato Grosso do Sul
            'mg',# Minas Gerais
            'pa',# Pará
            'pb',# Paraíba
            'pr',# Paraná
            'pe',# Pernambuco
            'pi',# Piauí
            'rj',# Rio de Janeiro
            'rn',# Rio Grande do Norte
            'rs',# Rio Grande do Sul
            'ro',# Rondônia
            'rr',# Roraima
            'sc',# Santa Catarina
            'sp',# São Paulo
            'se',# Sergipe
            'to']# Tocantins

        self.__cursor = 0
    
    def __gen__(self):
        self.__cursor += 1
        return self._pattern % ( self.__uf_s[self.__cursor-1] )
    
    def __open__(self):
        return self.__cursor < len(self.__uf_s)
    
    def next(self):
        return self.__gen__() if self.__open__() else None # FIXME
    
    @property
    def uf(self):
        if self.__open__() or self.__cursor == len(self.__uf_s):
            return self.__uf_s[self.__cursor-1]
        else:
            return None # FIXME throws exception


class URLgen(NameGenerator):

    def __init__(self):
        NameGenerator.__init__(self)
        self._pattern = 'http://www.rais.gov.br/mun_%s.asp'


class Record():

    def __init__(self, name, code, uf=None):
        self.__name = name
        self.__code = code
        self.__uf = uf
    
    @property
    def uf(self):
        return self.__uf.upper() if self.__uf else None
    
    @property
    def name(self):
        name = self.__name.title()
        name = name.replace(' De ', ' de ')
        name = name.replace(' Da ', ' da ')
        name = name.replace(' Das ', ' das ')
        name = name.replace(' Do ', ' do ')
        name = name.replace(' Dos ', ' dos ')
        return name.strip()
    
    @property
    def code(self):
        code = self.__code.replace('-', '')   # ex.: 31-71709
        return code.strip()
    
    def __str__(self):
        if self.uf:
            return '%s  %s    %s' % (self.uf, self.code, self.name)
        else:
            return '%s  %s' % (self.code, self.name)


class Reader(): 

    def __init__(self,
            url='http://www.rais.gov.br/mun_mg.asp',    # test value
            filename='test.htm',                        # test value
            uf=None,
            local=False            
    ):
        self.uf = uf #FIXME checks
        try:
            if local:
                self.soup = Soup( open(filename, 'r') )
            else:
                self.soup = Soup( urllib2.urlopen(url) )
        except KeyboardInterrupt:
            print 'Aborted'
            sys.exit(0)
        except Exception, e:
            print e
            sys.exit(1)
        self.records = []

    def execute(self):
        table = self.soup.findAll(id=["content"])[0].table
        tr_s = table.findAll('tr')
        for tr in tr_s:
            if tr.th: continue
            try:          
                name = tr.td.string                
                code = tr.td.nextSibling.nextSibling.string # take care
                #print Record(name, code)
                self.records.append(Record(name, code, self.uf))
            except Exception, e:
                print tr
                pass
    
    def exportCSV(self):
        import csv
        #FIXME mkdir -p http://stackoverflow.com/a/600612/3391915
        filename = 'csv/%s.csv' % (self.uf)
        with open(filename, 'w') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter='|',
                quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for r in self.records:
                spamwriter.writerow([r.code, r.name])


if __name__ == "__main__":
    #reader = Reader(local=True)
    #reader.execute()

    links = URLgen()
    link = links.next()
    #print links.__cursor
    while link:
        #print link + ' → ' + str(links.uf)
        reader = Reader(url=link, uf=links.uf, local=False) # t:True
        # make: wget -c http://www.rais.gov.br/mun_ce.asp -O test.htm
        print 'Processing %s ← %s' % (links.uf.upper(), link)
        reader.execute()
        reader.exportCSV()
        #break # if testing
        link = links.next()


'''
    TODO
     
    program.py --get-codes
    program.py --get-codes "rn"
    program.py --zip-codes
    program.py --query "São Paulo"
    program.py --download "3550308"
    
    see:
    
    http://docs.python.org/3/library/csv.html AND/OR
    http://www.pythonforbeginners.com/systems-programming/using-the-csv-module-in-python/
'''
