# Instruções

O projeto contém os dados CSV para possibilitar a implementação do que é proposto na _issue_ [#3](https://github.com/tmpsantos/IBGETools/issues/3):

```bash
$ program.py --query "São Paulo"
AM  1303908     São Paulo de Olivença
RN  2412609     São Paulo do Potengi
SP  3550308     São Paulo
RS  4319307     São Paulo das Missões
$ program.py --download "3550308"
```

## Precauções

```bash
$ mkdir -p csv
$ mkdir -p pdf
$ mkdir -p zip
```
Há um **FIXME** de criação de diretório na linha 147 de `ibge_query.py`.

## Importação de códigos de municípios

Você provavelmente **NÃO** precisará refazê-la! `ibge_query.py` só precisou de ser executado uma vez:

```bash
$ python ibge_query.py
Processing AC ← http://www.rais.gov.br/mun_ac.asp
Processing AL ← http://www.rais.gov.br/mun_al.asp
Processing AP ← http://www.rais.gov.br/mun_ap.asp
Processing AM ← http://www.rais.gov.br/mun_am.asp
Processing BA ← http://www.rais.gov.br/mun_ba.asp
Processing CE ← http://www.rais.gov.br/mun_ce.asp
<tr>
<td>          SAO BENEDIT<o>td>
        <td>          23-12304<</o>td>
      </td></tr>
Processing DF ← http://www.rais.gov.br/mun_df.asp
Processing ES ← http://www.rais.gov.br/mun_es.asp
Processing GO ← http://www.rais.gov.br/mun_go.asp
Processing MA ← http://www.rais.gov.br/mun_ma.asp
Processing MT ← http://www.rais.gov.br/mun_mt.asp
Processing MS ← http://www.rais.gov.br/mun_ms.asp
Processing MG ← http://www.rais.gov.br/mun_mg.asp
Processing PA ← http://www.rais.gov.br/mun_pa.asp
Processing PB ← http://www.rais.gov.br/mun_pb.asp
Processing PR ← http://www.rais.gov.br/mun_pr.asp
Processing PE ← http://www.rais.gov.br/mun_pe.asp
Processing PI ← http://www.rais.gov.br/mun_pi.asp
Processing RJ ← http://www.rais.gov.br/mun_rj.asp
Processing RN ← http://www.rais.gov.br/mun_rn.asp
Processing RS ← http://www.rais.gov.br/mun_rs.asp
Processing RO ← http://www.rais.gov.br/mun_ro.asp
Processing RR ← http://www.rais.gov.br/mun_rr.asp
Processing SC ← http://www.rais.gov.br/mun_sc.asp
Processing SP ← http://www.rais.gov.br/mun_sp.asp
Processing SE ← http://www.rais.gov.br/mun_se.asp
Processing TO ← http://www.rais.gov.br/mun_to.asp
$ 
```
Todos os arquivos `*.csv` foram criados. Apenas `ce.csv` teve um erro isolado. Ele foi corrigido manualmente. Por causa disso, e para facilitar utilização e correção dos dados, os arquivos CSV foram versionados como texto no diretório `csv`, e não foram destinados a um empacotamento ZIP.

Dificilmente alguém precisará de `ibge_query.py`. Esse código está aqui apenas como exemplo e fonte de conhecimento, principalmente para o caso de eventual necessidade de reescrita.
