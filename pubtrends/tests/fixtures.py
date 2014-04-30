#-*- encoding: utf8 -*-
__author__ = 'nacim'


dummy_error="""
<eSearchResult>
<ERROR>Invalid db name specified: toto</ERROR>
</eSearchResult>
"""


dummy_search_result="""<?xml version="1.0" ?>
<!DOCTYPE eSearchResult PUBLIC "-//NLM//DTD esearch 20060628//EN" "http://eutils.ncbi.nlm.nih.gov/eutils/dtd/20060628/esearch.dtd">
<eSearchResult><Count>2</Count><RetMax>2</RetMax><RetStart>0</RetStart>

<QueryKey>1</QueryKey>
<WebEnv>NCID_1_336197449_130.14.22.215_9001_1398861081_1235573448</WebEnv>
<IdList><Id>23263953</Id><Id>24772497</Id></IdList>

<TranslationSet><Translation><From>test</From><To>"research design"[MeSH Terms] OR ("research"[All Fields] AND "design"[All Fields]) OR "research design"[All Fields] OR "test"[All Fields]</To></Translation></TranslationSet>
<TranslationStack><TermSet><Term>"research design"[MeSH Terms]</Term><Field>MeSH Terms</Field><Count>328509</Count><Explode>Y</Explode></TermSet>
<TermSet><Term>"research"[All Fields]</Term><Field>All Fields</Field><Count>8312980</Count><Explode>N</Explode></TermSet><TermSet><Term>"design"[All Fields]</Term>
<Field>All Fields</Field><Count>957976</Count><Explode>N</Explode></TermSet><OP>AND</OP><OP>GROUP</OP><OP>OR</OP><TermSet><Term>"research design"[All Fields]</Term>
<Field>All Fields</Field><Count>95487</Count><Explode>N</Explode></TermSet><OP>OR</OP><TermSet><Term>"test"[All Fields]</Term><Field>All Fields</Field>
<Count>1091004</Count><Explode>N</Explode></TermSet><OP>OR</OP><OP>GROUP</OP></TranslationStack><QueryTranslation>"research design"[MeSH Terms] OR ("research"[All Fields] AND "design"[All Fields]) OR "research design"[All Fields] OR "test"[All Fields]
</QueryTranslation></eSearchResult>
"""

dummy_fetch_result = """<?xml version="1.0"?>
<!DOCTYPE PubmedArticleSet PUBLIC "-//NLM//DTD PubMedArticle, 1st January 2014//EN" "http://www.ncbi.nlm.nih.gov/corehtml/query/DTD/pubmed_140101.dtd">
<PubmedArticleSet>
<PubmedArticle>
    <MedlineCitation Owner="NLM" Status="MEDLINE">
        <PMID Version="1">23263953</PMID>
        <DateCreated>
            <Year>2013</Year>
            <Month>02</Month>
            <Day>14</Day>
        </DateCreated>
        <DateCompleted>
            <Year>2013</Year>
            <Month>07</Month>
            <Day>26</Day>
        </DateCompleted>
        <DateRevised>
            <Year>2013</Year>
            <Month>11</Month>
            <Day>14</Day>
        </DateRevised>
        <Article PubModel="Print-Electronic">
            <Journal>
                <ISSN IssnType="Electronic">1098-5336</ISSN>
                <JournalIssue CitedMedium="Internet">
                    <Volume>79</Volume>
                    <Issue>5</Issue>
                    <PubDate>
                        <Year>2013</Year>
                        <Month>Mar</Month>
                    </PubDate>
                </JournalIssue>
                <Title>Applied and environmental microbiology</Title>
                <ISOAbbreviation>Appl. Environ. Microbiol.</ISOAbbreviation>
            </Journal>
            <ArticleTitle>Detection of Borrelia burgdorferi sensu stricto ospC alleles associated with human lyme borreliosis worldwide in non-human-biting tick Ixodes affinis and rodent hosts in Southeastern United States.</ArticleTitle>
            <Pagination>
                <MedlinePgn>1444-53</MedlinePgn>
            </Pagination>
            <ELocationID EIdType="doi" ValidYN="Y">10.1128/AEM.02749-12</ELocationID>
            <Abstract>
                <AbstractText>Comparative analysis of ospC genes from 127 Borrelia burgdorferi sensu stricto strains collected in European and North American regions where Lyme disease is endemic and where it is not endemic revealed a close relatedness of geographically distinct populations. ospC alleles A, B, and L were detected on both continents in vectors and hosts, including humans. Six ospC alleles, A, B, L, Q, R, and V, were prevalent in Europe; 4 of them were detected in samples of human origin. Ten ospC alleles, A, B, D, E3, F, G, H, H3, I3, and M, were identified in the far-western United States. Four ospC alleles, B, G, H, and L, were abundant in the southeastern United States. Here we present the first expanded analysis of ospC alleles of B. burgdorferi strains from the southeastern United States with respect to their relatedness to strains from other North American and European localities. We demonstrate that ospC genotypes commonly associated with human Lyme disease in European and North American regions where the disease is endemic were detected in B. burgdorferi strains isolated from the non-human-biting tick Ixodes affinis and rodent hosts in the southeastern United States. We discovered that some ospC alleles previously known only from Europe are widely distributed in the southeastern United States, a finding that confirms the hypothesis of transoceanic migration of Borrelia species.</AbstractText>
            </Abstract>
            <AuthorList CompleteYN="Y">
                <Author ValidYN="Y">
                    <LastName>Rudenko</LastName>
                    <ForeName>Nataliia</ForeName>
                    <Initials>N</Initials>
                    <Affiliation>Biology Centre v.v.i., Institute of Parasitology AS CR, České Budějovice, Czech Republic. natasharudenko@hotmail.com</Affiliation>
                </Author>
                <Author ValidYN="Y">
                    <LastName>Golovchenko</LastName>
                    <ForeName>Maryna</ForeName>
                    <Initials>M</Initials>
                </Author>
                <Author ValidYN="Y">
                    <LastName>Hönig</LastName>
                    <ForeName>Václav</ForeName>
                    <Initials>V</Initials>
                </Author>
                <Author ValidYN="Y">
                    <LastName>Mallátová</LastName>
                    <ForeName>Nadja</ForeName>
                    <Initials>N</Initials>
                </Author>
                <Author ValidYN="Y">
                    <LastName>Krbková</LastName>
                    <ForeName>Lenka</ForeName>
                    <Initials>L</Initials>
                </Author>
                <Author ValidYN="Y">
                    <LastName>Mikulásek</LastName>
                    <ForeName>Peter</ForeName>
                    <Initials>P</Initials>
                </Author>
                <Author ValidYN="Y">
                    <LastName>Fedorova</LastName>
                    <ForeName>Natalia</ForeName>
                    <Initials>N</Initials>
                </Author>
                <Author ValidYN="Y">
                    <LastName>Belfiore</LastName>
                    <ForeName>Natalia M</ForeName>
                    <Initials>NM</Initials>
                </Author>
                <Author ValidYN="Y">
                    <LastName>Grubhoffer</LastName>
                    <ForeName>Libor</ForeName>
                    <Initials>L</Initials>
                </Author>
                <Author ValidYN="Y">
                    <LastName>Lane</LastName>
                    <ForeName>Robert S</ForeName>
                    <Initials>RS</Initials>
                </Author>
                <Author ValidYN="Y">
                    <LastName>Oliver</LastName>
                    <ForeName>James H</ForeName>
                    <Initials>JH</Initials>
                    <Suffix>Jr</Suffix>
                </Author>
            </AuthorList>
            <Language>eng</Language>
            <DataBankList CompleteYN="Y">
                <DataBank>
                    <DataBankName>GENBANK</DataBankName>
                    <AccessionNumberList>
                        <AccessionNumber>AY597021</AccessionNumber>
                        <AccessionNumber>AY597028</AccessionNumber>
                        <AccessionNumber>FJ932732</AccessionNumber>
                        <AccessionNumber>FJ932733</AccessionNumber>
                        <AccessionNumber>FJ932734</AccessionNumber>
                        <AccessionNumber>FJ932736</AccessionNumber>
                        <AccessionNumber>JF723215</AccessionNumber>
                        <AccessionNumber>JF723216</AccessionNumber>
                        <AccessionNumber>JF723217</AccessionNumber>
                        <AccessionNumber>JF723218</AccessionNumber>
                        <AccessionNumber>JF723219</AccessionNumber>
                        <AccessionNumber>JF723220</AccessionNumber>
                        <AccessionNumber>JF723221</AccessionNumber>
                        <AccessionNumber>JF723222</AccessionNumber>
                        <AccessionNumber>JF723223</AccessionNumber>
                        <AccessionNumber>JF723224</AccessionNumber>
                        <AccessionNumber>JF723226</AccessionNumber>
                        <AccessionNumber>JF723228</AccessionNumber>
                        <AccessionNumber>JF723229</AccessionNumber>
                        <AccessionNumber>JF723231</AccessionNumber>
                        <AccessionNumber>JF723232</AccessionNumber>
                        <AccessionNumber>JF723233</AccessionNumber>
                        <AccessionNumber>JF723234</AccessionNumber>
                        <AccessionNumber>JF723235</AccessionNumber>
                        <AccessionNumber>JF723236</AccessionNumber>
                        <AccessionNumber>JF723237</AccessionNumber>
                        <AccessionNumber>JF723238</AccessionNumber>
                        <AccessionNumber>JF723239</AccessionNumber>
                        <AccessionNumber>JF723240</AccessionNumber>
                        <AccessionNumber>JF723241</AccessionNumber>
                        <AccessionNumber>JF723242</AccessionNumber>
                        <AccessionNumber>JF723243</AccessionNumber>
                        <AccessionNumber>JF723244</AccessionNumber>
                        <AccessionNumber>JF723245</AccessionNumber>
                        <AccessionNumber>JF723246</AccessionNumber>
                        <AccessionNumber>JF723247</AccessionNumber>
                        <AccessionNumber>JF723248</AccessionNumber>
                        <AccessionNumber>JF723249</AccessionNumber>
                        <AccessionNumber>JF723250</AccessionNumber>
                        <AccessionNumber>JF723251</AccessionNumber>
                        <AccessionNumber>JF723252</AccessionNumber>
                        <AccessionNumber>JF723253</AccessionNumber>
                        <AccessionNumber>JF723254</AccessionNumber>
                        <AccessionNumber>JF723255</AccessionNumber>
                        <AccessionNumber>JF723256</AccessionNumber>
                        <AccessionNumber>JF723257</AccessionNumber>
                        <AccessionNumber>JF723258</AccessionNumber>
                        <AccessionNumber>JF723259</AccessionNumber>
                        <AccessionNumber>JF723260</AccessionNumber>
                        <AccessionNumber>JF723261</AccessionNumber>
                        <AccessionNumber>JF723262</AccessionNumber>
                        <AccessionNumber>JF723263</AccessionNumber>
                        <AccessionNumber>JF723264</AccessionNumber>
                        <AccessionNumber>JF723265</AccessionNumber>
                        <AccessionNumber>JF723266</AccessionNumber>
                        <AccessionNumber>JF723267</AccessionNumber>
                        <AccessionNumber>JF723268</AccessionNumber>
                        <AccessionNumber>JF723269</AccessionNumber>
                        <AccessionNumber>JF723270</AccessionNumber>
                        <AccessionNumber>JF754968</AccessionNumber>
                        <AccessionNumber>JF754969</AccessionNumber>
                        <AccessionNumber>JF754971</AccessionNumber>
                        <AccessionNumber>JQ219681</AccessionNumber>
                        <AccessionNumber>JQ219682</AccessionNumber>
                        <AccessionNumber>JQ219683</AccessionNumber>
                        <AccessionNumber>JQ219684</AccessionNumber>
                        <AccessionNumber>JQ236853</AccessionNumber>
                        <AccessionNumber>JQ236854</AccessionNumber>
                        <AccessionNumber>JQ253799</AccessionNumber>
                        <AccessionNumber>JQ253800</AccessionNumber>
                        <AccessionNumber>JQ253801</AccessionNumber>
                        <AccessionNumber>JQ253802</AccessionNumber>
                        <AccessionNumber>JQ253803</AccessionNumber>
                        <AccessionNumber>JQ253804</AccessionNumber>
                        <AccessionNumber>JQ253805</AccessionNumber>
                        <AccessionNumber>JQ308215</AccessionNumber>
                        <AccessionNumber>JQ308216</AccessionNumber>
                        <AccessionNumber>JQ308217</AccessionNumber>
                        <AccessionNumber>JQ308218</AccessionNumber>
                        <AccessionNumber>JQ308219</AccessionNumber>
                        <AccessionNumber>JQ308220</AccessionNumber>
                        <AccessionNumber>JQ308221</AccessionNumber>
                        <AccessionNumber>JQ308222</AccessionNumber>
                        <AccessionNumber>JQ308223</AccessionNumber>
                        <AccessionNumber>JQ308224</AccessionNumber>
                        <AccessionNumber>JQ308225</AccessionNumber>
                        <AccessionNumber>JQ308226</AccessionNumber>
                        <AccessionNumber>JQ308227</AccessionNumber>
                        <AccessionNumber>JQ308228</AccessionNumber>
                        <AccessionNumber>JQ308229</AccessionNumber>
                        <AccessionNumber>JQ308230</AccessionNumber>
                        <AccessionNumber>JQ308231</AccessionNumber>
                        <AccessionNumber>JQ308232</AccessionNumber>
                        <AccessionNumber>JQ308233</AccessionNumber>
                        <AccessionNumber>JQ308234</AccessionNumber>
                        <AccessionNumber>JQ308235</AccessionNumber>
                    </AccessionNumberList>
                </DataBank>
            </DataBankList>
            <GrantList CompleteYN="Y">
                <Grant>
                    <GrantID>R37AI-24899</GrantID>
                    <Acronym>AI</Acronym>
                    <Agency>NIAID NIH HHS</Agency>
                    <Country>United States</Country>
                </Grant>
                <Grant>
                    <GrantID>U50/CCU410282</GrantID>
                    <Agency>PHS HHS</Agency>
                    <Country>United States</Country>
                </Grant>
            </GrantList>
            <PublicationTypeList>
                <PublicationType>Journal Article</PublicationType>
                <PublicationType>Research Support, N.I.H., Extramural</PublicationType>
                <PublicationType>Research Support, Non-U.S. Gov't</PublicationType>
                <PublicationType>Research Support, U.S. Gov't, P.H.S.</PublicationType>
            </PublicationTypeList>
            <ArticleDate DateType="Electronic">
                <Year>2012</Year>
                <Month>12</Month>
                <Day>21</Day>
            </ArticleDate>
        </Article>
        <MedlineJournalInfo>
            <Country>United States</Country>
            <MedlineTA>Appl Environ Microbiol</MedlineTA>
            <NlmUniqueID>7605801</NlmUniqueID>
            <ISSNLinking>0099-2240</ISSNLinking>
        </MedlineJournalInfo>
        <ChemicalList>
            <Chemical>
                <RegistryNumber>0</RegistryNumber>
                <NameOfSubstance>Antigens, Bacterial</NameOfSubstance>
            </Chemical>
            <Chemical>
                <RegistryNumber>0</RegistryNumber>
                <NameOfSubstance>Bacterial Outer Membrane Proteins</NameOfSubstance>
            </Chemical>
            <Chemical>
                <RegistryNumber>0</RegistryNumber>
                <NameOfSubstance>DNA, Bacterial</NameOfSubstance>
            </Chemical>
            <Chemical>
                <RegistryNumber>0</RegistryNumber>
                <NameOfSubstance>OspC protein</NameOfSubstance>
            </Chemical>
        </ChemicalList>
        <CitationSubset>IM</CitationSubset>
        <CommentsCorrectionsList>
            <CommentsCorrections RefType="Cites">
                <RefSource>MMWR CDC Surveill Summ. 2000 Apr 28;49(3):1-11</RefSource>
                <PMID Version="1">10817483</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>Science. 2001 May 11;292(5519):1109-12</RefSource>
                <PMID Version="1">11352066</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>Infect Immun. 2001 Jul;69(7):4303-12</RefSource>
                <PMID Version="1">11401967</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>Genetics. 2002 Mar;160(3):833-49</RefSource>
                <PMID Version="1">11901105</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>J Infect Dis. 2002 Sep 15;186(6):782-91</RefSource>
                <PMID Version="1">12198612</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>J Clin Invest. 2004 Apr;113(8):1093-101</RefSource>
                <PMID Version="1">15085185</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>Microbiology. 2004 Jun;150(Pt 6):1741-55</RefSource>
                <PMID Version="1">15184561</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>Genetics. 2004 Oct;168(2):713-22</RefSource>
                <PMID Version="1">15514047</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>Ann N Y Acad Sci. 1988;539:180-91</RefSource>
                <PMID Version="1">3056198</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>J Clin Microbiol. 1989 Jan;27(1):13-20</RefSource>
                <PMID Version="1">2913024</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>Conn Med. 1989 Jun;53(6):343-6</RefSource>
                <PMID Version="1">2667888</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>J Wildl Dis. 1990 Jan;26(1):1-10</RefSource>
                <PMID Version="1">2304189</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>Annu Rev Entomol. 1991;36:587-609</RefSource>
                <PMID Version="1">2006870</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>J Med Entomol. 1991 Sep;28(5):719-25</RefSource>
                <PMID Version="1">1941942</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>Science. 1992 Jun 5;256(5062):1439-42</RefSource>
                <PMID Version="1">1604318</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>Science. 1993 Jun 11;260(5114):1610-6</RefSource>
                <PMID Version="1">8503006</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>Proc Natl Acad Sci U S A. 1993 Aug 1;90(15):7371-5</RefSource>
                <PMID Version="1">8346258</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>J Parasitol. 1995 Feb;81(1):30-6</RefSource>
                <PMID Version="1">7876974</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>J Clin Microbiol. 1995 Mar;33(3):589-95</RefSource>
                <PMID Version="1">7751362</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>J Bacteriol. 1995 Jun;177(11):3036-44</RefSource>
                <PMID Version="1">7768799</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>J Clin Microbiol. 1995 Dec;33(12):3270-4</RefSource>
                <PMID Version="1">8586715</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>J Parasitol. 1996 Dec;82(6):926-35</RefSource>
                <PMID Version="1">8973401</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>J Parasitol. 1996 Dec;82(6):936-40</RefSource>
                <PMID Version="1">8973402</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>Int J Syst Bacteriol. 1997 Jan;47(1):11-8</RefSource>
                <PMID Version="1">8995796</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>Mol Biol Evol. 1997 Jul;14(7):685-95</RefSource>
                <PMID Version="1">9254330</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>Int J Syst Bacteriol. 1997 Oct;47(4):1112-7</RefSource>
                <PMID Version="1">9336916</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>Folia Parasitol (Praha). 1997;44(4):309-14</RefSource>
                <PMID Version="1">9437846</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>Hereditas. 1997;127(3):203-16</RefSource>
                <PMID Version="1">9474903</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>J Parasitol. 1998 Feb;84(1):29-34</RefSource>
                <PMID Version="1">9488334</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>Appl Environ Microbiol. 1998 Apr;64(4):1169-74</RefSource>
                <PMID Version="1">9546150</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>Am J Epidemiol. 1998 Nov 15;148(10):1018-26</RefSource>
                <PMID Version="1">9829875</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>Genetics. 1999 Jan;151(1):15-30</RefSource>
                <PMID Version="1">9872945</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>J Clin Microbiol. 1999 Mar;37(3):565-9</RefSource>
                <PMID Version="1">9986813</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>Infect Immun. 1999 Jul;67(7):3518-24</RefSource>
                <PMID Version="1">10377134</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>J Clin Microbiol. 1999 Sep;37(9):3010-2</RefSource>
                <PMID Version="1">10449492</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>FEMS Microbiol Lett. 1999 Aug 15;177(2):289-96</RefSource>
                <PMID Version="1">10474195</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>J Clin Microbiol. 2005 Apr;43(4):1879-84</RefSource>
                <PMID Version="1">15815012</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>Parasitology. 2004;129 Suppl:S191-220</RefSource>
                <PMID Version="1">15938512</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>Appl Environ Microbiol. 2006 Jan;72(1):976-9</RefSource>
                <PMID Version="1">16391149</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>Emerg Infect Dis. 2006 Jul;12(7):1087-95</RefSource>
                <PMID Version="1">16836825</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>Appl Environ Microbiol. 2006 Aug;72(8):5331-41</RefSource>
                <PMID Version="1">16885284</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>Nat Rev Microbiol. 2006 Sep;4(9):660-9</RefSource>
                <PMID Version="1">16894341</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>Bioinformatics. 2007 Nov 1;23(21):2947-8</RefSource>
                <PMID Version="1">17846036</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>Appl Environ Microbiol. 2008 Mar;74(6):1780-90</RefSource>
                <PMID Version="1">18245258</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>Am J Trop Med Hyg. 2008 May;78(5):806-10</RefSource>
                <PMID Version="1">18458317</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>Emerg Infect Dis. 2008 Jul;14(7):1097-104</RefSource>
                <PMID Version="1">18598631</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>Appl Environ Microbiol. 2008 Aug;74(16):5008-14</RefSource>
                <PMID Version="1">18539816</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>Parasite. 2008 Sep;15(3):244-7</RefSource>
                <PMID Version="1">18814688</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>J Clin Microbiol. 2008 Oct;46(10):3540-3</RefSource>
                <PMID Version="1">18650352</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>J Clin Microbiol. 2009 Jan;47(1):134-41</RefSource>
                <PMID Version="1">19020062</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>FEMS Microbiol Lett. 2009 Mar;292(2):274-81</RefSource>
                <PMID Version="1">19187198</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>Curr Probl Dermatol. 2009;37:31-50</RefSource>
                <PMID Version="1">19367096</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>Clin Immunol. 2009 Sep;132(3):393-400</RefSource>
                <PMID Version="1">19576856</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>Int J Syst Evol Microbiol. 2011 Feb;61(Pt 2):381-3</RefSource>
                <PMID Version="1">20305062</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>J Clin Microbiol. 2011 Mar;49(3):945-54</RefSource>
                <PMID Version="1">21177909</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>Appl Environ Microbiol. 2011 Mar;77(6):1999-2007</RefSource>
                <PMID Version="1">21257811</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>Appl Environ Microbiol. 2011 May;77(10):3244-54</RefSource>
                <PMID Version="1">21421790</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>Am J Pathol. 2011 Jun;178(6):2726-39</RefSource>
                <PMID Version="1">21641395</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>Ticks Tick Borne Dis. 2010 Dec;1(4):168-71</RefSource>
                <PMID Version="1">21771524</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>PLoS One. 2011;6(8):e22926</RefSource>
                <PMID Version="1">21829670</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>Ticks Tick Borne Dis. 2011 Sep;2(3):123-8</RefSource>
                <PMID Version="1">21890064</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>Zoonoses Public Health. 2012 Sep;59 Suppl 2:48-64</RefSource>
                <PMID Version="1">22958250</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>Appl Environ Microbiol. 2013 Feb;79(4):1403-6</RefSource>
                <PMID Version="1">23220965</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>Appl Environ Microbiol. 2009 Nov;75(22):7243-52</RefSource>
                <PMID Version="1">19783741</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>J Clin Microbiol. 2009 Dec;47(12):3875-80</RefSource>
                <PMID Version="1">19846628</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>Vector Borne Zoonotic Dis. 2010 Apr;10(3):223-30</RefSource>
                <PMID Version="1">19492952</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>Emerg Infect Dis. 2010 Jun;16(6):911-7</RefSource>
                <PMID Version="1">20507740</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>J Vector Ecol. 2010 Jun;35(1):124-39</RefSource>
                <PMID Version="1">20618658</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>J Vector Ecol. 2010 Jun;35(1):174-9</RefSource>
                <PMID Version="1">20618664</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>MBio. 2010;1(4). pii: e00153-10. doi: 10.1128/mBio.00153-10</RefSource>
                <PMID Version="1">20877579</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>Evolution. 2010 Sep;64(9):2653-63</RefSource>
                <PMID Version="1">20394659</PMID>
            </CommentsCorrections>
            <CommentsCorrections RefType="Cites">
                <RefSource>Clin Microbiol Infect. 2011 Jan;17(1):69-79</RefSource>
                <PMID Version="1">20132258</PMID>
            </CommentsCorrections>
        </CommentsCorrectionsList>
        <MeshHeadingList>
            <MeshHeading>
                <DescriptorName MajorTopicYN="Y">Alleles</DescriptorName>
            </MeshHeading>
            <MeshHeading>
                <DescriptorName MajorTopicYN="N">Animals</DescriptorName>
            </MeshHeading>
            <MeshHeading>
                <DescriptorName MajorTopicYN="N">Antigens, Bacterial</DescriptorName>
                <QualifierName MajorTopicYN="Y">genetics</QualifierName>
            </MeshHeading>
            <MeshHeading>
                <DescriptorName MajorTopicYN="N">Bacterial Outer Membrane Proteins</DescriptorName>
                <QualifierName MajorTopicYN="Y">genetics</QualifierName>
            </MeshHeading>
            <MeshHeading>
                <DescriptorName MajorTopicYN="N">Borrelia burgdorferi</DescriptorName>
                <QualifierName MajorTopicYN="Y">genetics</QualifierName>
                <QualifierName MajorTopicYN="N">isolation &amp; purification</QualifierName>
            </MeshHeading>
            <MeshHeading>
                <DescriptorName MajorTopicYN="N">DNA, Bacterial</DescriptorName>
                <QualifierName MajorTopicYN="N">chemistry</QualifierName>
                <QualifierName MajorTopicYN="N">genetics</QualifierName>
            </MeshHeading>
            <MeshHeading>
                <DescriptorName MajorTopicYN="N" Type="Geographic">Europe</DescriptorName>
            </MeshHeading>
            <MeshHeading>
                <DescriptorName MajorTopicYN="N">Genetic Variation</DescriptorName>
            </MeshHeading>
            <MeshHeading>
                <DescriptorName MajorTopicYN="N">Genotype</DescriptorName>
            </MeshHeading>
            <MeshHeading>
                <DescriptorName MajorTopicYN="N">Humans</DescriptorName>
            </MeshHeading>
            <MeshHeading>
                <DescriptorName MajorTopicYN="N">Ixodes</DescriptorName>
                <QualifierName MajorTopicYN="Y">microbiology</QualifierName>
            </MeshHeading>
            <MeshHeading>
                <DescriptorName MajorTopicYN="N">Molecular Sequence Data</DescriptorName>
            </MeshHeading>
            <MeshHeading>
                <DescriptorName MajorTopicYN="N" Type="Geographic">North America</DescriptorName>
            </MeshHeading>
            <MeshHeading>
                <DescriptorName MajorTopicYN="N">Rodentia</DescriptorName>
                <QualifierName MajorTopicYN="Y">microbiology</QualifierName>
            </MeshHeading>
            <MeshHeading>
                <DescriptorName MajorTopicYN="N">Sequence Analysis, DNA</DescriptorName>
            </MeshHeading>
        </MeshHeadingList>
        <OtherID Source="NLM">PMC3591949</OtherID>
    </MedlineCitation>
    <PubmedData>
        <History>
            <PubMedPubDate PubStatus="aheadofprint">
                <Year>2012</Year>
                <Month>12</Month>
                <Day>21</Day>
            </PubMedPubDate>
            <PubMedPubDate PubStatus="entrez">
                <Year>2012</Year>
                <Month>12</Month>
                <Day>25</Day>
                <Hour>6</Hour>
                <Minute>0</Minute>
            </PubMedPubDate>
            <PubMedPubDate PubStatus="pubmed">
                <Year>2012</Year>
                <Month>12</Month>
                <Day>25</Day>
                <Hour>6</Hour>
                <Minute>0</Minute>
            </PubMedPubDate>
            <PubMedPubDate PubStatus="medline">
                <Year>2013</Year>
                <Month>7</Month>
                <Day>28</Day>
                <Hour>6</Hour>
                <Minute>0</Minute>
            </PubMedPubDate>
        </History>
        <PublicationStatus>ppublish</PublicationStatus>
        <ArticleIdList>
            <ArticleId IdType="pii">AEM.02749-12</ArticleId>
            <ArticleId IdType="doi">10.1128/AEM.02749-12</ArticleId>
            <ArticleId IdType="pubmed">23263953</ArticleId>
            <ArticleId IdType="pmc">PMC3591949</ArticleId>
        </ArticleIdList>
    </PubmedData>
</PubmedArticle>


<PubmedArticle>
    <MedlineCitation Owner="NLM" Status="In-Process">
        <PMID Version="1">24772497</PMID>
        <DateCreated>
            <Year>2014</Year>
            <Month>04</Month>
            <Day>28</Day>
        </DateCreated>
        <Article PubModel="Print">
            <Journal>
                <ISSN IssnType="Print">8755-0229</ISSN>
                <JournalIssue CitedMedium="Print">
                    <Volume>29</Volume>
                    <Issue>3</Issue>
                    <PubDate>
                        <MedlineDate>2013 Nov-Dec</MedlineDate>
                    </PubDate>
                </JournalIssue>
                <Title>The Journal of medical practice management : MPM</Title>
                <ISOAbbreviation>J Med Pract Manage</ISOAbbreviation>
            </Journal>
            <ArticleTitle>The Health of Healthcare, Part III: Dissolving (curing) the cancer in healthcare.</ArticleTitle>
            <Pagination>
                <MedlinePgn>184-6</MedlinePgn>
            </Pagination>
            <Abstract>
                <AbstractText>In a previous part of this &quot;The Health of Healthcare&quot; series, the etiology of sickness in our healthcare system was established as cancer. This article offers a method to &quot;cure&quot; healthcare, taken from strategic management thinking called VOSIE. In this article, the use of VOSIE is described as well as who needs to apply this cure: the public. A unifying mantra is suggested: Think and decide.</AbstractText>
            </Abstract>
            <AuthorList CompleteYN="Y">
                <Author ValidYN="Y">
                    <LastName>Waldman</LastName>
                    <ForeName>Deane</ForeName>
                    <Initials>D</Initials>
                </Author>
            </AuthorList>
            <Language>eng</Language>
            <PublicationTypeList>
                <PublicationType>Journal Article</PublicationType>
            </PublicationTypeList>
        </Article>
        <MedlineJournalInfo>
            <Country>United States</Country>
            <MedlineTA>J Med Pract Manage</MedlineTA>
            <NlmUniqueID>8605494</NlmUniqueID>
            <ISSNLinking>8755-0229</ISSNLinking>
        </MedlineJournalInfo>
        <CitationSubset>T</CitationSubset>
    </MedlineCitation>
    <PubmedData>
        <History>
            <PubMedPubDate PubStatus="entrez">
                <Year>2014</Year>
                <Month>4</Month>
                <Day>29</Day>
                <Hour>6</Hour>
                <Minute>0</Minute>
            </PubMedPubDate>
            <PubMedPubDate PubStatus="pubmed">
                <Year>2010</Year>
                <Month>4</Month>
                <Day>29</Day>
                <Hour>6</Hour>
                <Minute>0</Minute>
            </PubMedPubDate>
            <PubMedPubDate PubStatus="medline">
                <Year>2014</Year>
                <Month>4</Month>
                <Day>29</Day>
                <Hour>6</Hour>
                <Minute>0</Minute>
            </PubMedPubDate>
        </History>
        <PublicationStatus>ppublish</PublicationStatus>
        <ArticleIdList>
            <ArticleId IdType="pubmed">24772497</ArticleId>
        </ArticleIdList>
    </PubmedData>
</PubmedArticle>

</PubmedArticleSet>
"""




