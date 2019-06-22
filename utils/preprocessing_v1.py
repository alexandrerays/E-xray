import pandas as pd
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

'''
Gera as series de Ideb por ano para serem usadas na analise cluster que vou fazer
'''

class Preprocessing(object):
    def __init__(self, file_name, encoding='utf-8'):
        self.file = file_name
        self.encoding = encoding
        self.dados = None
        self.dados_temporais = None
    @property
    def campos_validos(self):
        return ['Co_UF', 'Cod_Municipio_Completo', 'Cod_Escola_Completo', 'Rede',
                'Ideb2005', 'Ideb2007', 'Ideb2009','Ideb2011', 'Ideb2013', 'Ideb2015', 'Ideb2017',
                'TaxaAprovacao2005_1ao5ano','TaxaAprovacao2007_1ao5ano','TaxaAprovacao2009_1ao5ano','TaxaAprovacao2011_1ao5ano','TaxaAprovacao2013_1ao5ano','TaxaAprovacao2015_1ao5ano','TaxaAprovacao2017_1ao5ano',
                'TaxaAprovacao2005_1ano','TaxaAprovacao2007_1ano','TaxaAprovacao2009_1ano','TaxaAprovacao2011_1ano','TaxaAprovacao2013_1ano','TaxaAprovacao2015_1ano','TaxaAprovacao2017_1ano',
                'TaxaAprovacao2005_2ano','TaxaAprovacao2007_2ano','TaxaAprovacao2009_2ano','TaxaAprovacao2011_2ano','TaxaAprovacao2013_2ano','TaxaAprovacao2015_2ano','TaxaAprovacao2017_2ano',
                'TaxaAprovacao2005_3ano','TaxaAprovacao2007_3ano','TaxaAprovacao2009_3ano','TaxaAprovacao2011_3ano','TaxaAprovacao2013_3ano','TaxaAprovacao2015_3ano','TaxaAprovacao2017_3ano',
                'TaxaAprovacao2005_4ano','TaxaAprovacao2007_4ano','TaxaAprovacao2009_4ano','TaxaAprovacao2011_4ano','TaxaAprovacao2013_4ano','TaxaAprovacao2015_4ano','TaxaAprovacao2017_4ano',
                'TaxaAprovacao2005_5ano','TaxaAprovacao2007_5ano','TaxaAprovacao2009_5ano','TaxaAprovacao2011_5ano','TaxaAprovacao2013_5ano','TaxaAprovacao2015_5ano','TaxaAprovacao2017_5ano',
                'IndicadorRendimento_2005','IndicadorRendimento_2007','IndicadorRendimento_2009','IndicadorRendimento_2011','IndicadorRendimento_2013','IndicadorRendimento_2015','IndicadorRendimento_2017',
                'NotaProvaBrasil_MT_2005','NotaProvaBrasil_MT_2007','NotaProvaBrasil_MT_2009','NotaProvaBrasil_MT_2011','NotaProvaBrasil_MT_2013','NotaProvaBrasil_MT_2015','NotaProvaBrasil_MT_2017',
                'NotaProvaBrasil_LP_2005','NotaProvaBrasil_LP_2007','NotaProvaBrasil_LP_2009','NotaProvaBrasil_LP_2011','NotaProvaBrasil_LP_2013','NotaProvaBrasil_LP_2015','NotaProvaBrasil_LP_2017',
                'NotaProvaBrasil_NotaMedia_2005','NotaProvaBrasil_NotaMedia_2007','NotaProvaBrasil_NotaMedia_2009','NotaProvaBrasil_NotaMedia_2011','NotaProvaBrasil_NotaMedia_2013','NotaProvaBrasil_NotaMedia_2015','NotaProvaBrasil_NotaMedia_2017']
        
    def load_file(self):
        df = pd.read_csv(self.file, encoding=self.encoding)
        df = df[self.campos_validos].copy()
        df.columns = ['uf', 'cod_mun', 'cod_escola', 'tp_rede', 
                      'i05', 'i07', 'i09', 'i11', 'i13', 'i15', 'i17',
                      'tx_aprov_1ao5ano_2005','tx_aprov_1ao5ano_2007','tx_aprov_1ao5ano_2009','tx_aprov_1ao5ano_2011','tx_aprov_1ao5ano_2013','tx_aprov_1ao5ano_2015','tx_aprov_1ao5ano_2017',
                      'tx_aprov_1ano_2005','tx_aprov_1ano_2007','tx_aprov_1ano_2009','tx_aprov_1ano_2011','tx_aprov_1ano_2013','tx_aprov_1ano_2015','tx_aprov_1ano_2017',
                      'tx_aprov_2ano_2005','tx_aprov_2ano_2007','tx_aprov_2ano_2009','tx_aprov_2ano_2011','tx_aprov_2ano_2013','tx_aprov_2ano_2015','tx_aprov_2ano_2017',
                      'tx_aprov_3ano_2005','tx_aprov_3ano_2007','tx_aprov_3ano_2009','tx_aprov_3ano_2011','tx_aprov_3ano_2013','tx_aprov_3ano_2015','tx_aprov_3ano_2017',
                      'tx_aprov_4ano_2005','tx_aprov_4ano_2007','tx_aprov_4ano_2009','tx_aprov_4ano_2011','tx_aprov_4ano_2013','tx_aprov_4ano_2015','tx_aprov_4ano_2017',
                      'tx_aprov_5ano_2005','tx_aprov_5ano_2007','tx_aprov_5ano_2009','tx_aprov_5ano_2011','tx_aprov_5ano_2013','tx_aprov_5ano_2015','tx_aprov_5ano_2017',
                      'ind_rend_2005','ind_rend_2007','ind_rend_2009','ind_rend_2011','ind_rend_2013','ind_rend_2015','ind_rend_2017',
                      'nota_prova_MT_2005','nota_prova_MT_2007','nota_prova_MT_2009','nota_prova_MT_2011','nota_prova_MT_2013','nota_prova_MT_2015','nota_prova_MT_2017',
                      'nota_prova_LP_2005','nota_prova_LP_2007','nota_prova_LP_2009','nota_prova_LP_2011','nota_prova_LP_2013','nota_prova_LP_2015','nota_prova_LP_2017',
                      'nota_prova_nota_media_2005','nota_prova_nota_media_2007','nota_prova_nota_media_2009','nota_prova_nota_media_2011','nota_prova_nota_media_2013','nota_prova_nota_media_2015','nota_prova_nota_media_2017']
        df['cod_escola'] = df['cod_escola'].astype(int)
        df['cod_mun'] = df['cod_mun'].astype(int)
        if self.dados is None:
            self.dados = df   
        
    
    def fill_missing(self):
        lista_col = ['i05', 'i07', 'i09', 'i11', 'i13', 'i15', 'i17',
                     'tx_aprov_1ao5ano_2005','tx_aprov_1ao5ano_2007','tx_aprov_1ao5ano_2009','tx_aprov_1ao5ano_2011','tx_aprov_1ao5ano_2013','tx_aprov_1ao5ano_2015','tx_aprov_1ao5ano_2017',
                      'tx_aprov_1ano_2005','tx_aprov_1ano_2007','tx_aprov_1ano_2009','tx_aprov_1ano_2011','tx_aprov_1ano_2013','tx_aprov_1ano_2015','tx_aprov_1ano_2017',
                      'tx_aprov_2ano_2005','tx_aprov_2ano_2007','tx_aprov_2ano_2009','tx_aprov_2ano_2011','tx_aprov_2ano_2013','tx_aprov_2ano_2015','tx_aprov_2ano_2017',
                      'tx_aprov_3ano_2005','tx_aprov_3ano_2007','tx_aprov_3ano_2009','tx_aprov_3ano_2011','tx_aprov_3ano_2013','tx_aprov_3ano_2015','tx_aprov_3ano_2017',
                      'tx_aprov_4ano_2005','tx_aprov_4ano_2007','tx_aprov_4ano_2009','tx_aprov_4ano_2011','tx_aprov_4ano_2013','tx_aprov_4ano_2015','tx_aprov_4ano_2017',
                      'tx_aprov_5ano_2005','tx_aprov_5ano_2007','tx_aprov_5ano_2009','tx_aprov_5ano_2011','tx_aprov_5ano_2013','tx_aprov_5ano_2015','tx_aprov_5ano_2017',
                      'ind_rend_2005','ind_rend_2007','ind_rend_2009','ind_rend_2011','ind_rend_2013','ind_rend_2015','ind_rend_2017',
                      'nota_prova_MT_2005','nota_prova_MT_2007','nota_prova_MT_2009','nota_prova_MT_2011','nota_prova_MT_2013','nota_prova_MT_2015','nota_prova_MT_2017',
                      'nota_prova_LP_2005','nota_prova_LP_2007','nota_prova_LP_2009','nota_prova_LP_2011','nota_prova_LP_2013','nota_prova_LP_2015','nota_prova_LP_2017',
                      'nota_prova_nota_media_2005','nota_prova_nota_media_2007','nota_prova_nota_media_2009','nota_prova_nota_media_2011','nota_prova_nota_media_2013','nota_prova_nota_media_2015','nota_prova_nota_media_2017']
        for el in lista_col:
            self.dados[el] = self.dados.apply(lambda x : '0' if x[el]=='-' else x[el], axis=1)
    
    def formata_serie(self):
        frames = []
        for escola in self.dados['cod_escola'].tolist():
            dfesc = self.dados[self.dados['cod_escola'] == escola]
            _df = dfesc.iloc[:, 4:].T
            _df.columns = ['ideb']
            lista_ideb = _df['ideb'].tolist()
            frames.append(pd.DataFrame({'cod_escola' : [dfesc['cod_escola'].iloc[0]]*7,
                                       'cod_mun' : [dfesc['cod_mun'].iloc[0]]*7,
                                       'uf' : [dfesc['uf'].iloc[0]]*7,
                                       'tp_rede' : [dfesc['tp_rede'].iloc[0]]*7,
                                       'ano' : [2005, 2007, 2009, 2011, 2013, 2015, 2017],
                                       'ideb' : lista_ideb}))
        resp = pd.concat(frames)
        resp['ideb'] = resp.apply(lambda x : float(x['ideb']), axis=1)
        if self.dados_temporais is None:
            self.dados_temporais = resp
    
    
    
    
    
    def dados_finais(self):
        self.load_file()
        self.fill_missing()
        self.formata_serie()
        return self.dados_temporais
    
if __name__ == '__main__':
    pp = Preprocessing('ideb_escolas_anosiniciais2005_2017.csv', 'latin-1')
    resp2 = pp.dados_finais()
    
    
    
    
    
