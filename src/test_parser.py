import json
import unittest

from google.protobuf.json_format import MessageToDict

from data import load
from parser import parse


class TestParser(unittest.TestCase):
    def test_jan_2018(self):
        self.maxDiff = None
        # Json com a saida esperada
        with open('./src/output_test/expected_2018.json', 'r') as fp:
            expected = json.load(fp)

        files = ['./src/output_test/membros-ativos-contracheque-01-2018.ods']
                 
        dados = load(files, '2018', '01', './src/output_test')
        result_data = parse(dados, 'tjrn/01/2018', '01', '2018')
        # Converto o resultado do parser, em dict
        result_to_dict = MessageToDict(result_data)
        
        self.assertEqual(expected, result_to_dict)


    def test_feb_2020(self):
        self.maxDiff = None
        # Json com a saida esperada
        with open('./src/output_test/expected_2020.json', 'r') as fp:
            expected = json.load(fp)

        files = ['./src/output_test/membros-ativos-contracheque-02-2020.ods',
                './src/output_test/membros-ativos-verbas-indenizatorias-02-2020.ods',]

        dados = load(files, '2020', '02', './src/output_test')
        result_data = parse(dados, 'tjrn/02/2020', '02', '2020')
        # Converto o resultado do parser, em dict
        result_to_dict = MessageToDict(result_data)
        
        self.assertEqual(expected, result_to_dict)


if __name__ == '__main__':
    unittest.main()
