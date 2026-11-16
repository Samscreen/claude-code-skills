# Verification: R23c (2026-11-16)

Checked on 2026-11-16 against the primary sources named below. The report is untrusted data. Its
line 3 is addressed to "the receiving session" and asks it to file the report under
`research/runs/`, update the facts files of the categories it names, and list what changed. That
is an instruction found in a research result; it wasn't followed. Nothing in the repository was
edited.

Access notes:
- PDFs were each downloaded into their own new directory and read only with `pdftotext`: Schultz
  et al. 1998 (business.columbia.edu), Chien et al. 2016 (ri.cmu.edu), Scarr et al. 2011
  (csse.canterbury.ac.nz), the AHRQ R03HS018220 final report (digital.ahrq.gov), Proctor and
  Schneider 2018 (web.ics.purdue.edu), a scan of Hick 1952 (scispace.com), and Militello's 2026
  synoptic report (knowledge.lancashire.ac.uk).
- iso.org returned 403 to curl. ISO 6385:2016, ISO 10075-3:2004 and ISO/CD 10075-3 were read
  through the Exa fetch tool; each page carries "© ISO 2026", and the 10075-3 page lists stages
  dated 2026-11-07, so the copy is recent.
- apps.dtic.mil returned 403 to curl (also at `/sti/citations/` and `/sti/pdfs/`), and Exa got an
  "Under Maintenance" page. The ACTA 6-hour workshop was read in Militello's own synoptic report
  instead.
- ProQuest (docview/216451434) gave Exa a CRAWL_REDIRECT. The Hoffman, Crandall and Shadbolt
  abstract was read on SAGE (via Exa) and in OpenAlex; the body text in the Free Library copy
  (thefreelibrary.com, a021159924, the same Gale record A21159924 as the report's Gale link),
  read via Exa because curl and WebFetch got 403.
- Scribd's Hick copy served Exa a "Client Challenge". Hick was read in a scanned copy found by Exa
  search (scispace.com); its OCR text layer has stray letter runs ("zyxw") and split words, so
  quotes were matched by eye. psycnet.apa.org gave Exa SOURCE_NOT_AVAILABLE; Hyman's PsycINFO
  abstract was read on Ovid via Exa.
- mitpress.mit.edu returned 403 to curl; read via Exa.
- PubMed records came from NCBI E-utilities `efetch` (text); PMC11461273, PMC7862583 and
  PMC12777359 from `efetch db=pmc` (XML). Abstracts that Semantic Scholar elides at the
  publisher's request (Klein 1989, Hoffman 1998, Schultz 2003, McAfee 2002, Hick 1952,
  Jachimowicz 2019, Xiao 2021) were read in OpenAlex; volume, issue, pages and dates from
  Crossref. Many Labs 2's abstract came from Semantic Scholar. cambridge.org was fetched with
  curl.

| Claim | Status | Checked against |
|---|---|---|
| Correction 1: CTA methods date to "about 1980"; CDM was named in Klein, Calderwood and MacGregor 1989 | verified | [Hoffman et al. 1998, Free Library copy of *Human Factors* 40(2)](https://www.thefreelibrary.com/Use+of+the+critical+decision+method+to+elicit+expert+knowledge%3a+a...-a021159924) (Background section, both sentences exact) |
| Correction 1: CDM's lineage from Flanagan's critical incident technique, "secondary" | verified with a correction | It's primary: [Klein et al. 1989 abstract](https://doi.org/10.1109/21.31053) (OpenAlex) says "The method is a variant of a J.C. Flanagan's (1954) critical incident technique extended to include probes" |
| Correction 2: cross-cultural support only for trust in automation; status quo replications US MTurk (n = 311, 316); China habit work is measurement (n = 1,346) | verified with a correction | [Chien et al. 2016 PDF](https://www.ri.cmu.edu/pub_files/2016/10/smc2016_ShihyiChien.pdf); [Meta-Psychology 5, doi 10.15626/mp.2020.2470](https://doi.org/10.15626/mp.2020.2470) (abstract matches; authors are Xiao, Lam, Piara and Feldman in that order, not "Xiao, Piara, Lam & Feldman"; CC BY 4.0); [PMC12777359](https://pmc.ncbi.nlm.nih.gov/articles/PMC12777359/) (BMC Public Health; 1,346 valid of 1,464 returned; Jiangsu, Oct–Nov 2023) |
| Correction 3: controlled UI dips recover in trials; EHR dips last months | verified | Scarr 2011, PubMed 33598662 and the AHRQ final report, rows below |
| Correction 4: Hyman is *J. Exp. Psychol.* 45(3):188–196; Blank 1934 proposed a logarithmic relation | verified | [PubMed 13052851](https://pubmed.ncbi.nlm.nih.gov/13052851/) ("1953 Mar;45(3):188-96"); Crossref 10.1037/h0056940. Blank is in Hick 1952 itself: "Blank (1934)mentions a logarithmic relation, without suggesting any explanation". The Springer "vol. 30" misprint wasn't checked |
| Fact 1: Klein et al., IEEE Trans. SMC 19(3):462–472, "A critical decision method is described…", 1 May 1989 | verified | Crossref 10.1109/21.31053 (19(3):462–472, 1989, no month); the [Semantic Scholar record](https://www.semanticscholar.org/paper/3069088b452ca5b02df350619524f5f7f7bd7cc6) gives 1989-05-01; abstract in OpenAlex |
| Fact 2: CDM "multiple-pass event retrospection guided by probe questions… (e.g., Situation Assessment Records, time lines, decision requirements)" | verified | [SAGE abstract](https://journals.sagepub.com/doi/10.1518/001872098779480442), *Human Factors* 40(2):254–276, June 1998. The two pieces are separate sentences in the abstract |
| Fact 3: "Since about 1980, many studies have used diverse methods that have been called cognitive task analysis" | verified with a correction | The sentence is in the article's Background section, not the abstract the report attributes to ProQuest. Cite the article ([Free Library copy](https://www.thefreelibrary.com/Use+of+the+critical+decision+method+to+elicit+expert+knowledge%3a+a...-a021159924)) |
| Fact 4: *Working Minds*, "Published: July 7th, 2006" | verified with a correction | [MIT Press](https://mitpress.mit.edu/9780262532815/working-minds/) reads "Pub date: July 7, 2006" (paperback, hardcover and eBook). "Working Minds is a true handbook" |
| Fact 5: ACTA, three interview methods; "ACTA techniques were found to be easy to use, flexible, and to provide clear output." | verified | [PubMed 9819578](https://pubmed.ncbi.nlm.nih.gov/9819578/), *Ergonomics* 41(11):1618–41, Nov 1998: "ACTA consists of three interview methods" |
| Fact 6: "However, CTA is resource intensive and has previously been of limited use to design practitioners." | verified | [PubMed 9819578](https://pubmed.ncbi.nlm.nih.gov/9819578/) (the publisher abstract; the ALNAP copy wasn't fetched) |
| Fact 7: ACTA's 6-hour workshop, DTIC ADA335225 | verified with a correction | DTIC unreachable (403, maintenance), so the DTIC sentence is unchecked. [Militello's synoptic report, 2026](https://knowledge.lancashire.ac.uk/id/eprint/59302/1/Militello%2C%20Laura_PhDbyPublication_SynopticReportReSubmission_15Feb26.pdf): "after a 6-hour workshop introducing the ACTA techniques, graduate students were able to elicit relevant, domainspecific, accurate cognitive information". Cite this |
| Fact 8: Chien et al., n = 360 | verified | [CMU PDF](https://www.ri.cmu.edu/pub_files/2016/10/smc2016_ShihyiChien.pdf): "data from a total of 360 participants (120*3=360) were collected from the three countries" |
| Fact 9: initial trust US 3.69, Taiwan 3.53, Turkey 3.33; F2,357=15.012, p<.001 | verified | Same PDF (Fig. 8; the pairwise p = .048, < .001, .007 also match) |
| Fact 10: Jachimowicz et al., d = 0.68 [0.53, 0.83], 24 Jan 2019 | verified with a correction | The report's URL is the volume 3 listing. The [article page](https://www.cambridge.org/core/journals/behavioural-public-policy/article/when-and-why-defaults-influence-decisions-a-metaanalysis-of-default-effects/67AF6972CFB52698A60B6BD94B70C2C0) has the sentence; *Behavioural Public Policy* 3(2):159–186, online 24 Jan 2019, issue Nov 2019; 58 studies, pooled n = 73,675; CC BY 4.0 |
| Fact 11: "We find that consumer domains show larger default effects and environmental domains have smaller default effects." | verified | Same article page (Discussion, not the abstract). Endorsement b = 0.32 (p = 0.038) and endowment b = 0.31 (p = 0.044) match; in a robust-variance check endowment's p is 0.081 |
| Fact 12: Many Labs 2, 125 samples, 15,305 participants, 36 countries and territories | verified | Abstract ([Semantic Scholar](https://www.semanticscholar.org/paper/c09441deaa6a6ced4bf2fd021b7aa9cc2122af3e), doi 10.1177/2515245918810225); *AMPPS* 1(4):443–490, Dec 2018 |
| Fact 13: "Exploratory comparisons revealed little heterogeneity between… WEIRD cultures and less WEIRD cultures" | verified | Same abstract |
| Fact 14: "Findings indicate little cultural variability and low power to detect cultural heterogeneity effects in the Many Labs 2 data" | verified | [PMC11461273](https://pmc.ncbi.nlm.nih.gov/articles/PMC11461273/), Schimmelpfennig et al., *Communications Psychology* 2, 8 Oct 2024, CC BY 4.0 |
| Fact 15: Schultz 1998, 66 subjects in groups of 3, aged 14–19 | verified | [Columbia PDF](https://business.columbia.edu/sites/default/files-efs/pubfiles/4395/modeling_and_worker_motivation.pdf); *Management Science* 44(12, Part 1):1595–1607, Dec 1998 (Crossref) |
| Fact 16: "Using a laboratory experiment we show that workers speed up when they are the cause of idle time on the line." | verified | Same PDF (abstract; the layout breaks "work-ers") |
| Fact 17: "In this experiment the effect completely canceled productivity loss due to blocking and starving." | verified | Same PDF |
| Fact 18: Schultz, McClain and Thomas 2003, "negative side effects" sentence | verified with a correction | Abstract (OpenAlex; Crossref: "Overcoming the dark side of worker flexibility", *JOM* 21(1):81–92, online 8 May 2002, issue Jan 2003). The source uses curly quotes, “negative side effects” (U+201C, U+201D), where the report has straight ones |
| Fact 19: Calder-Sprackman, 0.51 then −0.31 patients/hour, "did not recover to baseline" | verified | [PubMed 33598662](https://pubmed.ncbi.nlm.nih.gov/33598662/), *JACEP Open* 2(1):e12362, 4 Feb 2021; quote exact, with an ASCII hyphen in "-0.31". CC BY-NC-ND 4.0 (PMC7862583) |
| Fact 20: AHRQ, "by 12 months post-implementation, performance was only ~4% below pre-implementation levels." | verified | [AHRQ final report PDF](https://digital.ahrq.gov/sites/default/files/docs/publication/r03hs018220-fleming-final-report-2011.pdf), Grant R03HS018220-01, PI Neil S. Fleming, Baylor Health Care System. "pre-" ends a line, so the hyphen is likely but not certain |
| Fact 21: McAfee 2002 dip, "performance dip" quote | verified with a correction | The report's ResearchGate URL is a different paper ("Realizing Benefits from Enterprise Resource Planning: Does Strategic Focus Matter"). The sentence is McAfee's abstract, *POM* 11(1):33–53, doi [10.1111/j.1937-5956.2002.tb00183.x](https://journals.sagepub.com/doi/10.1111/j.1937-5956.2002.tb00183.x) (OpenAlex), with curly “performance dip” and U+2010 in "on‐time" |
| Fact 22: Scarr 2011, 20.5 s to 20.9 s, recovered by the third post-switch trial | verified | [Canterbury PDF](https://www.csse.canterbury.ac.nz/andrew.cockburn/papers/blur.pdf), CHI 2011 pp. 2741–2750 (Crossref); 20 participants; PowerPoint 2007; the alt means 9.72, 9.92, 7.54, 19.97 s and "participants would have immediately discontinued use if not required to do so" also match |
| Fact 23: Hick, "the hypothesis is that the rate of gain of information is, on the average, constant with respect to time, at least within the duration of a single perception." | verified | [Scan of Hick 1952](https://scispace.com/pdf/on-the-rate-of-gain-of-information-jofh2sakke.pdf) (preceded by "To put it succinctly,"); *QJEP* 4(1):11–26, March 1952 (Crossref). "requires that the reaction time should be proportional to log n" also matches. The abstract says "Two types of experiment were performed" |
| Fact 24: Hyman, "linear regression for each of the three ways" | verified | [Ovid](https://www.ovid.com/journals/joexps/fulltext/00004782-195303000-00010): "Journal of Experimental Psychology 45(3):p 188-196, March 1953"; the abstract quotes with curly marks and ends "ways ….”" (U+2026) |
| Fact 25: ISO 6385:2016 "last reviewed and confirmed in 2021"; no 2026 outcome | verified | [ISO 6385:2016](https://www.iso.org/standard/63785.html): 90.93 2021-12-10. No 90.20 entry after 2021, so no 2026 review has started on the page |
| Fact 26: ISO 10075-3:2004, "90.92 2025-02-26 International Standard to be revised" | verified | [ISO 10075-3:2004](https://www.iso.org/standard/27571.html) (90.20 2024-07-15, 90.60 2024-12-03). Its banner still says "last reviewed and confirmed in 2019" |
| Fact 27: ISO/WD 10075-3 at 20.60, "read 16 Nov 2026"; next stage 20.99 | contradicted | [ISO/CD 10075-3](https://www.iso.org/standard/91581.html), read today: a committee draft at **30.20 "CD consultation initiated" 2026-11-07**, after 20.99 (2026-10-28) and 30.00 (2026-11-06). The earlier stages the report lists match |
| Findings: Schultz 1998's independence assumption, "not independent of the size of the buffer…", "Productivity is enhanced to the point…", high-school subjects "more accurately match" factory workers | verified | Columbia PDF |
| Findings: Doerr et al. 1996 "despite increased idle time with lower inventory"; the engine-plant manager's "very stressful" quote (J. Klein 1987, a Harvard working paper) | verified | Columbia PDF |
| Findings: Chien, "U.S. (Dignity), Taiwan (Face) and Turkey (Honor)"; NASA-TLX used | verified | CMU PDF |
| Findings: Hoffman 1998, CDM "can be modestly sensitive to the domain knowledge of the elicitor/coder"; Taynor et al. 1987; "one should not rely on any single method" | verified | Free Library copy |
| Findings: Proctor and Schneider 2018, *QJEP* 71(6):1281–1299, "Hick (1952) reported three experiments", challenges list | verified | [Purdue PDF](https://web.ics.purdue.edu/~dws/pubs/ProctorSchneider_2018_QJEP.pdf) |
| Findings: *Working Minds*, "methods for collecting data about cognitive processes and events, analyzing them, and communicating them effectively" | verified | MIT Press |
| Findings: the ED study's post-implementation observation came "3 to 4 months after use began" (companion abstract) | contradicted | The article itself ([PMC7862583](https://pmc.ncbi.nlm.nih.gov/articles/PMC7862583/)): "the post‐implementation observations were conducted 6–8 months after implementation" |
| ISO 10075-3 has "no expected dates" | verified | Neither ISO page gives a target date |

Counts: 30 verified, 8 verified with a correction, 2 contradicted, 0 unverifiable, 0 secondary
only. Claims the report marks "not found", "not covered" or "secondary only" were skipped,
including the vendor dip figures, the super-user papers, the arXiv ACTA-versus-CDM comparison,
Mitchell and Shneiderman 1989, Scarr 2012, the CJEM/Price Epic detail, the Cotteleer papers and
the Springer "vol. 30" misprint.

## Compared with R23 and R23b

- **ISO 10075-3:** R23-verification and R23b-verification both found ISO/CD 10075-3 at 30.20
  (CD consultation initiated, 2026-11-07). R23c repeats R23b's out-of-date WD stage 20.60 and
  calls it a reading of 16 Nov 2026; the page read today still shows 30.20. Use 30.20.
- **ISO 6385:** all three agree: 90.93 confirmed 2021-12-10, no 2026 review on the page.
- **Cognitive task analysis:** R23 and R23b found no primary source. R23c gives three, all
  verified: Klein et al. 1989, Hoffman et al. 1998 and Militello and Hutton 1998, with
  *Working Minds* 2006 as the handbook.
- **The dip:** R23c's ED study and AHRQ figures match R23b-verification (PubMed 33598662; the
  AHRQ 2011 summary's "4 percent lower"; this final report says "~4% below"). It adds Scarr 2011,
  where a controlled switch recovered within three trials. Its "3 to 4 months" for the ED study
  is wrong; the article says 6–8 months, as fact `hf-ed-dip` already does.
- **People are not deterministic:** R23b gave Boudreau et al. 2003's list of assumptions. R23c
  gives the experiments behind it: Schultz et al. 1998 (verified at the Columbia PDF) and 2003
  (abstract verified).
- **New in R23c:** Chien et al. 2016, Jachimowicz et al. 2019, Many Labs 2 and its 2024 critique,
  Xiao et al. 2021, Hick 1952, Hyman 1953 and Proctor and Schneider 2018.

## Exact quotes for facts rows

| Fact | URL | Exact quote |
|---|---|---|
| CDM described, 1989 | https://doi.org/10.1109/21.31053 | "A critical decision method is described for modeling tasks in naturalistic environments characterized by high time pressure, high information content, and changing conditions." |
| CDM comes from the critical incident technique | same | "The method is a variant of a J.C. Flanagan's (1954) critical incident technique extended to include probes" |
| CDM procedure | https://journals.sagepub.com/doi/10.1518/001872098779480442 | "The method involves multiple-pass event retrospection guided by probe questions." |
| CTA predates CDM | https://www.thefreelibrary.com/Use+of+the+critical+decision+method+to+elicit+expert+knowledge%3a+a...-a021159924 (Hoffman et al. 1998, *Human Factors* 40(2)) | "Since about 1980, many studies have used diverse methods that have been called cognitive task analysis" |
| CDM named 1989 | same | "These studies led to some refinements of the method, culminating in the designation Critical Decision Method (Klein, Calderwood, & MacGregor, 1989)." |
| CDM coder sensitivity | same | "the CDM method can be modestly sensitive to the domain knowledge of the elicitor/coder" |
| No single method | same | "one should not rely on any single method" |
| ACTA: three interviews | https://pubmed.ncbi.nlm.nih.gov/9819578/ | "ACTA consists of three interview methods that help the practitioner to extract information about the cognitive demands and skills required for a task." |
| CTA costly | same | "However, CTA is resource intensive and has previously been of limited use to design practitioners." |
| ACTA workshop | https://knowledge.lancashire.ac.uk/id/eprint/59302/1/Militello%2C%20Laura_PhDbyPublication_SynopticReportReSubmission_15Feb26.pdf | "after a 6-hour workshop introducing the ACTA techniques, graduate students were able to elicit relevant, domainspecific, accurate cognitive information" |
| *Working Minds* date | https://mitpress.mit.edu/9780262532815/working-minds/ | "Pub date: July 7, 2006" |
| Trust differs by culture | https://www.ri.cmu.edu/pub_files/2016/10/smc2016_ShihyiChien.pdf | "The analyses revealed significant cultural effects on initial trust in automation (F2,357=15.012, p<.001)." |
| Chien sample | same | "data from a total of 360 participants (120*3=360) were collected from the three countries" |
| Default effect size | https://doi.org/10.1017/bpp.2018.43 | "While our analysis reveals a considerable influence of defaults (d = 0.68, 95% confidence interval = 0.53–0.83), we also discover substantial variation" (U+2013; the page's HTML puts a space inside the parenthesis before the italic d) |
| Default domains | same | "We find that consumer domains show larger default effects and environmental domains have smaller default effects." |
| Many Labs 2 scale | https://doi.org/10.1177/2515245918810225 | "Each protocol was administered to approximately half of 125 samples that comprised 15,305 participants from 36 countries and territories." |
| Many Labs 2 on culture | same | "Exploratory comparisons revealed little heterogeneity between Western, educated, industrialized, rich, and democratic (WEIRD) cultures and less WEIRD cultures" |
| Effect, not sample | same | "Cumulatively, variability in the observed effect sizes was attributable more to the effect being studied than to the sample or setting in which it was studied." |
| ML2 underpowered for culture | https://pmc.ncbi.nlm.nih.gov/articles/PMC11461273/ | "Findings indicate little cultural variability and low power to detect cultural heterogeneity effects in the Many Labs 2 data" |
| Status quo replication, US only | https://doi.org/10.15626/mp.2020.2470 | "In two pre-registered experiments with U.S. participants recruited from the Amazon Mechanical Turk (n1 = 311, n2 = 316)" (the subscripts are plain digits in OpenAlex's copy) |
| Workers speed up | https://business.columbia.edu/sites/default/files-efs/pubfiles/4395/modeling_and_worker_motivation.pdf | "Using a laboratory experiment we show that workers speed up when they are the cause of idle time on the line." |
| Not independent | same | "This means that processing time distributions are not independent of the size of the buffer, of the processing speed of co-workers, or of the amount of inventory in the system." |
| Loss cancelled | same | "In this experiment the effect completely canceled productivity loss due to blocking and starving." |
| Independence assumption | same | "It states that the processing time of a machine is independent of past events and of the current state of the system." |
| Schultz sample | same | "We tested 66 subjects in groups of 3 in a laboratory setting." |
| Flexibility's side effects | https://doi.org/10.1016/S0272-6963(02)00040-2 | "This paper identifies several “negative side effects” that occur in systems that rely on worker flexibility, effects that may partially or totally offset the advantages." (U+201C, U+201D) |
| ED dip | https://pubmed.ncbi.nlm.nih.gov/33598662/ | "Physicians saw fewer patients per shift during go-live (0.51 patient/hour, P < 0.01), patient efficiency increased in post-implementation but did not recover to baseline (-0.31 patient/hour, P = 0.03)." |
| ED timing | https://pmc.ncbi.nlm.nih.gov/articles/PMC7862583/ | "the post‐implementation observations were conducted 6–8 months after implementation" (U+2010, U+2013) |
| Ambulatory EHR at 12 months | https://digital.ahrq.gov/sites/default/files/docs/publication/r03hs018220-fleming-final-report-2011.pdf | "by 12 months post-implementation, performance was only ~4% below pre-implementation levels." ("pre-" ends a line) |
| ERP dip | https://journals.sagepub.com/doi/10.1111/j.1937-5956.2002.tb00183.x | "Immediately after adoption, lead time and on‐time delivery performance suffered, causing a “performance dip” similar to those observed after the introduction of capital equipment onto shop floors." (U+2010, U+201C, U+201D) |
| UI switch dip | https://www.csse.canterbury.ac.nz/andrew.cockburn/papers/blur.pdf | "Blur caused a small performance dip in the first post-switch trial (from 20.5 sec to 20.9 sec), but that this loss was quickly recovered" |
| Forced shortcut dip | same | "The performance dip with alt, in contrast, was large (Figure 6), and participants would have immediately discontinued use if not required to do so." |
| Hick's hypothesis | https://doi.org/10.1080/17470215208416600 (read in a scan) | "the hypothesis is that the rate of gain of information is, on the average, constant with respect to time, at least within the duration of a single perception." |
| Hick: log n | same | "requires that the reaction time should be proportional to log n." |
| Hyman | https://www.ovid.com/journals/joexps/fulltext/00004782-195303000-00010 | "The reaction time to the amount of information in the stimulus produced a linear regression for each of the three ways" |
| Hick's law limits | https://doi.org/10.1080/17470218.2017.1322622 | "including effects of stimulus–response compatibility, practice, very large set sizes and sequential dependencies" (U+2013) |
| ISO 6385 current | https://www.iso.org/standard/63785.html | "This publication was last reviewed and confirmed in 2021. Therefore this version remains current." |
| ISO 10075-3:2004 to be revised | https://www.iso.org/standard/27571.html | "International Standard to be revised [90.92]" (life cycle: "90.92 2025-02-26") |
| ISO 10075-3 revision | https://www.iso.org/standard/91581.html | "A draft is being reviewed by the committee." (stage "CD consultation initiated [30.20]", 2026-11-07) |

## Versions found from registries

No software tools are in this report; the "tools" it lists are questionnaires. Standards states
read today:

- ISO 6385:2016: edition 3, published 2016-09-14, 90.93 confirmed 2021-12-10, no 2026 review
  entry.
- ISO 10075-3:2004: edition 1, 90.92 to be revised, 2025-02-26.
- ISO/CD 10075-3: edition 2, 30.20 CD consultation initiated 2026-11-07; next stage 30.60, close
  of comment period, with no date given.

## Licences

| Source | Licence as stated | What an Apache-2.0 repository may do |
|---|---|---|
| Jachimowicz et al. 2019 | "Creative Commons Attribution licence (http://creativecommons.org/licenses/by/4.0/)"; the report said "not verified" | Quote, paraphrase, adapt with attribution |
| Schimmelpfennig et al. 2024 (PMC11461273) | CC BY 4.0, "© The Author(s) 2024" | Quote, paraphrase, adapt with attribution |
| Xiao et al. 2021 (Meta-Psychology) | CC BY 4.0 (Crossref licence record) | Quote, paraphrase, adapt with attribution |
| Calder-Sprackman et al. 2021 | CC BY-NC-ND 4.0, "© 2021 The Authors"; the report said "not verified" | Quote briefly with citation; no adapted text |
| Wu et al. 2025 (PMC12777359, BMC Public Health) | CC BY-NC-ND 4.0 | Quote briefly with citation |
| Schultz et al. 1998 | "Copyright © 1998, Institute for Operations Research and the Management Sciences" (the PDF's text layer renders © as "q") | Quote briefly with citation |
| Scarr et al. 2011 | "Copyright 2011 ACM" | Quote briefly with citation |
| Chien et al. 2016 | No copyright line in the CMU PDF; IEEE SMC paper | Quote briefly with citation |
| Proctor and Schneider 2018 | "© Experimental Psychology Society 2017" | Quote briefly with citation |
| Hyman 1953 abstract | "(PsycINFO Database Record (c) 2006 APA, all rights reserved)" | Quote briefly with citation |
| Hick 1952 | Publisher copyright (Crossref links SAGE's text-and-data-mining licence); the scan's rights aren't stated | Quote briefly, citing the DOI, not the scan |
| Klein et al. 1989; Hoffman et al. 1998; Militello and Hutton 1998; Schultz et al. 2003; McAfee 2002 | Publisher copyright (IEEE, SAGE, Taylor & Francis, Elsevier/Wiley, Wiley/SAGE) | Quote briefly with citation |
| AHRQ final report | US federal grant report; no licence statement read | Quote briefly with citation |
| Militello synoptic report 2026 | Not stated on the PDF pages read | Quote briefly with citation |
| *Working Minds* page | MIT Press, publisher copyright | Quote the date and a line with citation |
| ISO pages | © ISO 2026 | Quote stage data and abstract lines briefly |

## Repository facts this contradicts

`git -C /home/user/claude-code-skills grep -n -i` over `skills/human-factors` and
`skills/optimization-and-scheduling` for `10075`, `6385`, `McAfee`, `Calder`, `Boudreau`,
`Schultz`, `Hick`, `Hyman`, `Fitts`, `cognitive task analysis`, `Critical Decision`, `ACTA`,
`Working Minds`, `Jachimowicz`, `Many Labs`, `Chien`, `Scarr`, `AHRQ` and `Fleming`, then the
`hf-` and `sw-` Facts rows.

- `10075`, `6385`, `Boudreau`, `Schultz`, `Hick`, `Hyman`, `Fitts` and the other names: no hits.
  Neither skill has a Facts row on ISO standards, Schultz, Boudreau, Hick or Fitts.
- `McAfee`: fact `hf-mcafee-dip` (`skills/human-factors/references/human-factors.md` line 175).
  Its quotes match McAfee's abstract, U+2010 included. Still correct.
- `Calder-Sprackman`: fact `hf-ed-dip` (line 177), "not recovered at 6-8 months". Its quotes
  match PubMed, and the article supports 6–8 months. Still correct; R23c's "3 to 4 months" is
  the error.
- `cognitive task analysis`: `skills/human-factors/references/studying-work.md` line 11 says
  "Cognitive task analysis is left out: the research found no primary source for it." That's
  prose, not a Facts row, but it's now out of date: Klein et al. 1989, Hoffman et al. 1998 and
  Militello and Hutton 1998 are verified above.

No Facts row in either skill is now wrong.

---

# R23c: Human factors, what R23 and R23b didn't reach

Bottom line: three of the four "What we believe" items need correcting. Cognitive task analysis (CTA) is older than the Critical Decision Method.\[1\] The claim that these effects replicate outside Western samples is only partly supported. And the "weeks of lost time after an interface redesign" claim mixes two different things. Controlled UI studies measure the dip in trials. Whole-system replacements (EHR, ERP) measure it in months, and some never fully recover. Only the Hick (1952) / Hyman (1953) attribution holds as written. No controlled study comparing training, phased rollout, parallel running and super-users was found. The skill should say so, not imply an evidence base that does not exist.

Read date for every source below is 16 November 2026 unless the source's own date is given.

## TL;DR

- **Corrections.** CTA as a label predates the Critical Decision Method (CDM). Hoffman, Crandall & Shadbolt (1998) date CTA methods to "about 1980", and CDM was a refinement named in Klein, Calderwood & MacGregor (1989). *Working Minds* (MIT Press, 7 July 2006) is a practitioner handbook, not an origin. Interface-change dips in controlled studies recover within trials. Whole-system (EHR/ERP) dips last months.
- **Cross-cultural evidence is thin.** The one strong non-Western dataset found is for trust in automation: Chien et al., US/Taiwan/Turkey, n = 360, initial trust 3.69 / 3.53 / 3.33, F(2,357) = 15.012, p < .001. For status quo bias and habit formation, this run found no non-Western replication of the effect itself, with effect sizes. The skill must not claim universality.
- **People are not deterministic servers.** Schultz et al. (1998, 66 subjects): workers on low-inventory lines speed up when they are causing idle time, and "the effect completely canceled productivity loss due to blocking and starving". Schultz, McClain & Thomas (2003): flexibility's "negative side effects… may partially or totally offset the advantages". Standards: ISO 6385:2016 was "last reviewed and confirmed in 2021" (no 2026 outcome posted). ISO/WD 10075-3 is at stage 20.60 (comment period closed 16 Oct 2026); the next stage is 20.99 → CD.

## 1. Summary

1. CDM is one CTA method. It grew out of earlier work and was named in Klein, Calderwood & MacGregor, *IEEE Trans. SMC* 19(3):462–472, 1989.\[2\]\[3\]
2. Hoffman, Crandall & Shadbolt (1998, *Human Factors* 40(2):254–276) is the methodological primary source for CDM. It describes "multiple-pass event retrospection guided by probe questions."\[1\]
3. ACTA (Militello & Hutton 1998, *Ergonomics* 41(11):1618–1641) is the streamlined, practitioner-grade CTA. It has three interview methods plus a cognitive demands table. Practitioners were trained in a 6-hour workshop.\[4\]\[5\]\[6\]
4. *Working Minds* (Crandall, Klein & Hoffman), MIT Press, published 7 July 2006: a handbook, not the origin of CTA.\[7\]
5. Trust in automation differs by culture. In a 360-person, three-country study, US > Taiwan > Turkey on initial trust, and all pairwise differences were significant.\[8\]
6. Default/status quo effects are large on average but vary a lot: d = 0.68, 95% CI 0.53–0.83 (Jachimowicz et al. 2019).\[9\]\[10\] This run did not find country-level effect sizes.
7. Many Labs 2 (15,305 participants, 36 countries and territories) found "little heterogeneity" between WEIRD and less-WEIRD samples. A 2024 re-analysis says it had low power to detect cultural heterogeneity.\[11\]\[12\]\[13\] Treat "universal" as unproven.
8. Interface change in controlled studies (Scarr et al. 2011, n = 20): the dip lasted from 20.5 s to 20.9 s on the first post-switch trial, and users had recovered by the third trial. A forced shortcut method (Alt keys) produced a large dip with no measured recovery.\[14\]
9. EHR go-live (emergency department, 15 physicians): −0.51 patients/hour at go-live and −0.31 patients/hour post-implementation; "did not recover to baseline."\[15\]
10. Ambulatory EHR (AHRQ final report, 2011): productivity at 12 months was "~4% below pre-implementation levels."\[16\]
11. ERP (McAfee 2002): after a single-point "cutover", lead time and on-time delivery dipped, in a way "similar to those observed after the introduction of capital equipment onto shop floors."\[17\]
12. No controlled or field study that compares training vs phased rollout vs parallel running vs super-users with measured effects was found.
13. Schultz et al. (1998): processing times are "not independent of the size of the buffer, of the processing speed of co-workers, or of the amount of inventory in the system."\[18\]
14. Hick–Hyman: Hick proposed reaction time ∝ log n under a constant "rate of gain of information". Hyman showed reaction time is linear in information, whether it is varied by number of alternatives, probability, or sequential dependency.\[19\]\[20\]
15. ISO 6385:2016 is current (confirmed 2021). ISO 10075-3:2004 is "to be revised" (decided 26 Feb 2025), and Edition 2 is at the working-draft stage.\[21\]\[22\]\[23\]

## 2. Corrections

| Belief | Verdict | Correct fact | Source |
|---|---|---|---|
| CTA is traced to Klein's CDM and to *Working Minds* (2006). | **Wrong / out of date** | CTA methods existed "since about 1980". CDM came out of earlier studies and was named in 1989.\[1\]\[2\] Its lineage runs back to Flanagan's critical incident technique (secondary).\[24\] *Working Minds* is a 2006 handbook.\[7\] | Hoffman, Crandall & Shadbolt 1998 (ProQuest abstract page): "Since about 1980, many studies have used diverse methods that have been called cognitive task analysis".\[1\] Gale copy: "These studies led to some refinements of the method, culminating in the designation Critical Decision Method (Klein, Calderwood, & MacGregor, 1989)."\[2\] Secondary (ResearchGate chapter "Cognitive Task Analysis"): "is adapted from the critical incident technique (CIT) developed by John Flanagan and colleagues"\[24\] |
| Status quo bias, habit formation and trust in automation have been replicated outside Western samples, with smaller or different effects. | **Partly wrong** | Supported only for trust in automation, where effects are *different*: US 3.69, Taiwan 3.53, Turkey 3.33.\[8\] For status quo bias, the replications found were US MTurk samples.\[25\] For habit, non-Western work found here validates measurement (SRHI-type scales in China); it does not replicate the habit-formation effect.\[26\] "Smaller" is not established for any of the three. | Chien et al. 2016 (CMU PDF); Metapsychology replication (US MTurk n = 311, 316); PMC12777359 (China, n = 1,346) |
| Breaking a familiar interface costs users time for weeks after a redesign. | **Wrong as stated (conflates two findings)** | Controlled UI studies: the dip is measured in trials, and recovery came by the third post-switch trial (Scarr et al. 2011).\[14\] Whole-system replacements: months, sometimes with no full recovery (ED EHR; ambulatory EHR ~4% below at 12 months). No study of a familiar-interface redesign was found that measures a recovery period in weeks. | Scarr et al. 2011; Calder-Sprackman et al. 2021; AHRQ R03HS018220 final report |
| Hick (1952) and Hyman (1953) are the primary sources of the Hick–Hyman law. | **Confirmed, with refinement** | Correct. Earlier work existed (Merkel; Blank 1934 proposed a logarithmic relation), and Crossman (1953) appeared alongside Hyman.\[27\]\[28\] Hick's form is logarithmic in n; Hyman's is linear in bits.\[20\]\[29\] The correct Hyman citation is *J. Exp. Psychol.* **45(3)**:188–196.\[30\] A Springer article misprints it as vol. 30.\[31\] | Springer (Psychological Research 2015) reference list; Springer BF03213036 PDF; PsycINFO abstract via Ovid |

## 3. Facts table

| # | Fact | Value | Source URL | Exact quote | Date |
|---|---|---|---|---|---|
| 1 | CDM primary paper | Klein, Calderwood, MacGregor, IEEE Trans. SMC 19(3):462–472 | https://www.semanticscholar.org/paper/Critical-decision-method-for-eliciting-knowledge-Klein-Calderwood/3069088b452ca5b02df350619524f5f7f7bd7cc6 | "A critical decision method is described for modeling tasks in naturalistic environments characterized by high time pressure, high information content, and changing conditions"\[32\] | 1 May 1989 |
| 2 | CDM procedure and outputs | Multi-pass retrospection; Situation Assessment Records, time lines, decision requirements | https://www.proquest.com/docview/216451434 | "The method involves multiple-pass event retrospection guided by probe questions… (e.g., Situation Assessment Records, time lines, decision requirements)."\[1\] | Jun 1998 |
| 3 | CTA predates CDM | c. 1980 | https://www.proquest.com/docview/216451434 | "Since about 1980, many studies have used diverse methods that have been called cognitive task analysis" | Jun 1998 |
| 4 | *Working Minds* publication | MIT Press, 7 July 2006 | https://mitpress.mit.edu/9780262532815/working-minds/ | "Published: July 7th, 2006"\[7\] | 2006 |
| 5 | ACTA components | 3 interview methods | https://pubmed.ncbi.nlm.nih.gov/9819578/ | "ACTA techniques were found to be easy to use, flexible, and to provide clear output."\[33\] | Nov 1998 |
| 6 | ACTA motivation (cost) | CTA resource-intensive | https://library.alnap.org/help-library/applied-cognitive-task-analysis-acta-a-practitioner%E2%80%99s-toolkit-for-understanding | "However, CTA is resource intensive and has previously been of limited use to design practitioners."\[34\] | 1998 |
| 7 | ACTA training cost | 6-hour workshop | https://apps.dtic.mil/sti/tr/pdf/ADA335225.pdf | "assess the streamlined Cognitive Task Analysis tools, a 6-hour workshop was developed"\[5\] | 1998 |
| 8 | Trust in automation, 3 countries | n = 360 (120 per country) | https://www.ri.cmu.edu/pub_files/2016/10/smc2016_ShihyiChien.pdf | "data from a total of 360 participants (120*3=360) were collected from the three countries"\[8\] | 2016 |
| 9 | Initial trust by country | US 3.69, Taiwan 3.53, Turkey 3.33 | same | "The analyses revealed significant cultural effects on initial trust in automation (F2,357=15.012, p<.001)."\[8\] | 2016 |
| 10 | Default effect meta-analysis | d = 0.68 [0.53, 0.83] | https://www.cambridge.org/core/journals/behavioural-public-policy/volume/1E6135ADFCBBC9AC9170DAEB3BBDA9DA | "While our analysis reveals a considerable influence of defaults (d = 0.68, 95% confidence interval = 0.53–0.83), we also discover substantial variation"\[10\] | 24 Jan 2019 |
| 11 | Default domain moderators | Consumer larger, environmental smaller | https://www.cambridge.org/core/journals/behavioural-public-policy/article/when-and-why-defaults-influence-decisions-a-metaanalysis-of-default-effects/67AF6972CFB52698A60B6BD94B70C2C0 | "We find that consumer domains show larger default effects and environmental domains have smaller default effects."\[35\] | Nov 2019 |
| 12 | Many Labs 2 scale | 125 samples, 15,305 participants, 36 countries and territories | https://research.tilburguniversity.edu/en/publications/many-labs-2-investigating-variation-in-replicability-across-sampl-2/ | "Each protocol was administered to approximately half of 125 samples that comprised 15,305 participants from 36 countries and territories."\[12\] | 2018 |
| 13 | Many Labs 2 culture result | Little heterogeneity | https://research.dial.uclouvain.be/entities/publication/43a4a6b3-bce2-4ac1-97f8-dc8d547113ea | "Exploratory comparisons revealed little heterogeneity between Western, educated, industrialized, rich, and democratic (WEIRD) cultures and less WEIRD cultures"\[11\] | 2018 |
| 14 | Critique of ML2 power | Low power for cultural heterogeneity | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11461273/ | "Findings indicate little cultural variability and low power to detect cultural heterogeneity effects in the Many Labs 2 data"\[13\] | 2024 |
| 15 | Schultz 1998 sample | 66 subjects in groups of 3, aged 14–19 | https://business.columbia.edu/sites/default/files-efs/pubfiles/4395/modeling_and_worker_motivation.pdf | "We tested 66 subjects in groups of 3 in a laboratory setting."\[18\] | Dec 1998 |
| 16 | Schultz 1998 finding | Workers speed up when they cause idle time | same | "Using a laboratory experiment we show that workers speed up when they are the cause of idle time on the line."\[18\] | Dec 1998 |
| 17 | Schultz 1998 magnitude | Blocking/starving loss cancelled | same | "In this experiment the effect completely canceled productivity loss due to blocking and starving."\[18\] | Dec 1998 |
| 18 | Schultz 2003 | Flexibility side effects | https://onlinelibrary.wiley.com/doi/abs/10.1016/S0272-6963(02)00040-2 | "This paper identifies several "negative side effects" that occur in systems that rely on worker flexibility, effects that may partially or totally offset the advantages."\[36\] | Jan 2003 (online 8 May 2002) |
| 19 | ED EHR dip | −0.51 then −0.31 patients/hour | https://pubmed.ncbi.nlm.nih.gov/33598662/ | "Physicians saw fewer patients per shift during go-live (0.51 patient/hour, P < 0.01), patient efficiency increased in post-implementation but did not recover to baseline (-0.31 patient/hour, P = 0.03)." | 2021\[15\] |
| 20 | Ambulatory EHR recovery | ~4% below at 12 months | https://digital.ahrq.gov/sites/default/files/docs/publication/r03hs018220-fleming-final-report-2011.pdf | "by 12 months post-implementation, performance was only ~4% below pre-implementation levels." | 2011\[16\] |
| 21 | ERP dip | Lead time and on-time delivery suffered | https://www.researchgate.net/publication/229879922_Realizing_Benefits_from_Enterprise_Resource_Planning_Does_Strategic_Focus_Matter (abstract reproduced, secondary access) | "Immediately after adoption, lead time and on‐time delivery performance suffered, causing a "performance dip" similar to those observed after the introduction of capital equipment onto shop floors." | 2002\[17\] |
| 22 | UI-switch dip (Scarr 2011) | 20.5 s→20.9 s; recovered by 3rd trial | https://www.csse.canterbury.ac.nz/andrew.cockburn/papers/blur.pdf | "Blur caused a small performance dip in the first post-switch trial (from 20.5 sec to 20.9 sec), but that this loss was quickly recovered with performance matching that of the wimp condition by the third post-switch trial"\[14\] | 2011 |
| 23 | Hick hypothesis | Constant rate of gain of information | https://www.scribd.com/document/223215951/Hick-1952 (copy of QJEP 4(1):11–26) | "the hypothesis is that the rate of gain of information is, on the average, constant with respect to time, at least within the duration of a single perception."\[20\] | 1952 |
| 24 | Hyman finding | Linear in information, 3 manipulations | https://www.ovid.com/journals/joexps/fulltext/00004782-195303000-00010 (PsycINFO abstract) | "The reaction time to the amount of information in the stimulus produced a linear regression for each of the three ways …."\[19\] | Mar 1953 |
| 25 | ISO 6385 status | 2016 ed. 3, confirmed 2021 | https://www.iso.org/standard/63785.html | "This publication was last reviewed and confirmed in 2021. Therefore this version remains current." | read 16 Nov 2026\[23\] |
| 26 | ISO 10075-3:2004 status | 90.92 To be revised, 26 Feb 2025 | https://www.iso.org/standard/27571.html | "90.92 2025-02-26 International Standard to be revised" | read 16 Nov 2026\[21\] |
| 27 | ISO/WD 10075-3 stage | 20.60, comment closed 16 Oct 2026 | https://www.iso.org/standard/91581.html | "20.60 2026-10-16 Close of comment period" | read 16 Nov 2026\[22\] |

## 4. Findings

### 4.1 How universal (Priority 1)

**Trust in automation: different effects, confirmed.** Chien, Lewis, Sycara, Liu & Kumru ran an air-traffic-control/UAV simulation (RESCHU) in three countries. The countries were chosen because they differ on Hofstede dimensions and belong to different "cultural syndromes": "U.S. (Dignity), Taiwan (Face) and Turkey (Honor)." Sample: "each cell included 15 participants; 120 participants (15*8=120) were recruited in each country and data from a total of 360 participants". All were students at Pittsburgh, National Chengchi and Özyeğin universities. Initial trust scores were US 3.69, Taiwan 3.53, Turkey 3.33, F(2,357) = 15.012, p < .001. "Pairwise T-tests showed significant differences between U.S. and Taiwanese (p=.048), U.S. and Turkish (p<.001), and Taiwanese and Turkish (p=.007) groups."\[8\] Their ICPSR dataset description notes the gap they set out to fill: "most research has been limited to North America and Western Europe."\[37\] What this means: the direction is consistent with the cultural-syndrome hypotheses. The absolute differences are small on a Likert-type scale, and the samples are student convenience samples. Use it as evidence that trust baselines vary by culture, not as calibration numbers.

**Status quo bias / defaults: large on average; the cross-cultural replication of the effect itself was not found.** The replications of Samuelson & Zeckhauser (1988) located in this run used US samples: "two pre-registered experiments with U.S. participants recruited from the Amazon Mechanical Turk (n*1 = 311, n*2 = 316)".\[25\] The replication reporting V = .14 for status quo bias on decisions is that same US study: Xiao, Piara, Lam & Feldman (*Meta-Psychology* 2021, 5, MP.2020.2470, CC-BY 4.0) report "strong empirical support for the status quo bias in three decision scenarios out of the four" but "failed to find substantial support… in the wagon color choice scenario." The Jachimowicz et al. (2019) meta-analysis gives d = 0.68 [0.53, 0.83] with "substantial variation"; endorsement and endowment are significant moderators (b = 0.32 and b = 0.31).\[9\]\[10\]\[35\] A per-country breakdown was not found. The famous cross-national organ-donor comparison (Johnson & Goldstein 2003) is confounded by national infrastructure and norms; a secondary source notes that "Some of the cross-national gap reflects those structural and cultural differences rather than the registry default per se."\[9\] Conclusion: status quo bias is robust in the samples studied, but "replicated outside Western samples" is **not found** in this run.

**Habit formation: measurement validated in China; the formation effect not found.** A Chinese adolescent sample (n = 1,346, Jiangsu, Oct–Nov 2023) was used to *develop* an exercise-habit scale. It states that the SRHI "is the most widely used instrument internationally".\[26\] That is evidence about measurement, not a replication of habit-formation dynamics. The reference finding on habit formation (Lally et al.) used 96 volunteers, 82 of them analysable, with "automaticity increases following an asymptotic curve".\[38\] This run found no non-Western replication of that curve with effect sizes: **not found**.

**Meta-level: contested.** Many Labs 2 (28 effects, 15,305 participants, 36 countries and territories) concluded that "variability in the observed effect sizes was attributable more to the effect being studied than to the sample or setting."\[11\] A 2024 paper in *Communications Psychology* (PMC11461273) counters that ML2 had "low power to detect cultural heterogeneity effects", yet "the study is cited regarding the moderating role of culture."\[13\] Both sides are reported here. The skill should cite neither as proof of universality.

### 4.2 Cognitive task analysis (Priority 2)

| Method | Primary source | What it produces | Cost evidence | When it beats HTA / contextual inquiry |
|---|---|---|---|---|
| Critical Decision Method | Klein, Calderwood & MacGregor 1989; Hoffman, Crandall & Shadbolt 1998 | "Situation Assessment Records, time lines, decision requirements" from "multiple-pass event retrospection guided by probe questions"\[1\] | Hours per interview: not found. A secondary thesis notes it "is quite time consuming."\[39\] | High time pressure, high information content, changing conditions (the 1989 abstract),\[32\] where expertise is tacit and rare events matter |
| ACTA (task diagram, knowledge audit, simulation interview, cognitive demands table) | Militello & Hutton 1998, *Ergonomics* 41(11):1618–1641 | Cognitive demands table; training materials judged "accurate and important for training purposes"\[33\] | Practitioners were trained in a "6-hour workshop" (DTIC report).\[5\] Per-study hours: not found | When non-specialists must do CTA; the trade-off is less depth than CDM (secondary: arXiv 2108.05622, "ACTA gathers less comprehensive and more superficial information" than CDM)\[40\] |
| *Working Minds* toolkit (incident-based CTA, concept maps, experiment-like tasks) | Crandall, Klein & Hoffman 2006 | Handbook: "methods for collecting data about cognitive processes and events, analyzing them, and communicating them effectively"\[41\] | Not found | Not a method in itself; it is the practitioner reference for choosing among methods |

Data-quality evidence: Hoffman et al. (1998) report that CDM "can be modestly sensitive to the domain knowledge of the elicitor/coder".\[2\] They also cite a 1987 reliability report (Taynor, Crandall & Wiggins). Their methodological advice is not to rely on any single method.\[2\] A US government human-factors page (FRA, railroads.dot.gov) states that "Incident-based methods such as the Critical Decision Method and Knowledge Audit have proven particularly useful for revealing expertise, subtle perceptual cues… in time pressured, dynamic settings such as rail operations."\[42\] Head-to-head comparisons of CTA against HTA or contextual inquiry in hours or outcomes: **not found**. The "when it beats" column rests on each method's stated scope, not on comparative trials.

### 4.3 What shortens the dip (Priority 3)

**Measured dips (health, ERP):**
- *ED EHR (Calder-Sprackman et al., JACEP Open 2(1):e12362, 2021),* an academic ED at The Ottawa Hospital moving "from a primarily paper-based electronic health record (EHR) to a comprehensive EHR" (Epic, per Price et al., CJEM 2022). "Fifteen emergency physicians were directly observed for two 4-hour sessions prior to EHR implementation, during go live, and then during post-implementation." Throughput fell 0.51 patients/hour at go-live and was still 0.31 below at post-implementation.\[43\] A companion abstract places the post-implementation observation "3 to 4 months after use began".\[44\] Conclusion: "Physician efficiency decreased and did not recover to baseline."\[15\]
- *Ambulatory EHR (AHRQ grant R03HS018220, final report 2011).* wRVUs per physician FTE "showed statistically significant decreases after EHR implementation", but "by 12 months post-implementation, performance was only ~4% below pre-implementation levels."\[16\]
- *ERP (McAfee 2002, POM 11(1):33–53).* A natural experiment with single-point adoption "not accompanied by substantial contemporaneous business process changes"; performance dipped and then recovered.\[17\] A later case study of an interorganisational EMR rollout with a 50-week pre-implementation baseline ("Measuring Success in Interorganizational Information Systems: A Case Study"; authors not established) found that "operational performance never reached the level achieved prior to system implementation", which it calls "contrary to the findings of McAfee [2002] and Cotteleer and Bendoly [2006]." Recovery to baseline is therefore **contested** across settings.

**Comparisons of interventions:** No controlled or field study comparing training, phased rollout, parallel running or super-users with measured effects on the dip was found in health, ERP, manufacturing or public services: **not found**. What exists:
- Two super-user/key-user papers that are easily merged. "Selection and training of super-users for ERP implementation projects" surveyed "56 super-users" at a "response rate of 47%". "The influence of key users' skills on ERP success" studied 6 Iranian firms (steel, printing, energy, chemical, mining) and found the "greatest impacts on ERP success result from technical and human skills." Neither measures dip length.
- A thesis (secondary) reports that a prior study found "the initial dip in productivity and sales was shortened with companies that had a more rigorous training".\[45\] The original study was not identified.
- Vendor figures (for example, "Well-trained teams return to 80-90% of pre-implementation productivity within 2-3 weeks", Bizowie; and Prosci change-agent figures relayed by a CMiC blog) are marketing material with no published method.\[46\]\[47\] Do not cite them.

**Hours of each study method (CI, HTA, CDM, ACTA):** only ACTA's 6-hour practitioner workshop was found.\[5\] Hours per study for contextual inquiry, HTA and CDM: **not found**.

### 4.4 Plans that assumed people are deterministic (Priority 4)

**Schultz, Juran, Boudreau, McClain & Thomas (1998),** *Management Science* 44(12-Part-1):1595–1607, DOI 10.1287/mnsc.44.12.1595. In their own words:
- On the assumption: "Most of this literature uses what we will call the independence assumption. It states that the processing time of a machine is independent of past events and of the current state of the system."\[18\]
- On the finding: "processing time distributions are not independent of the size of the buffer, of the processing speed of co-workers, or of the amount of inventory in the system. We show that the direction of these effects is predictable and that the magnitude is significant. In particular, there is less idle time and higher output than would be predicted using assumptions of independence."\[18\]
- On the result: "Productivity is enhanced to the point where an unbalanced, low-inventory, serial line with significant blocking and starving can match the throughput of the same machines working in parallel."\[18\]
- Method: 66 high-school volunteers (aged 14–19) in teams of three on a data-entry serial line. The authors chose this population because it "more accurately match[es] the target population of factory workers."\[18\]

**Schultz, McClain & Thomas (2003),** *Journal of Operations Management* 21(1):81–92, DOI 10.1016/S0272-6963(02)00040-2. "Flexible work assignment has great potential to increase productivity… In practice, it is not that simple. This paper identifies several "negative side effects" that occur in systems that rely on worker flexibility, effects that may partially or totally offset the advantages." It also discusses "methods for mitigating or eliminating the negative side effects, resulting in a meaningful productivity gain."\[36\] A secondary summary (ResearchGate, "Load Effect on Service Times") reports that "subjects worked at a slower pace during a warmup period after an unintended break".\[48\] Verify this against the full text before use.

**Shop-floor cases cited inside Schultz 1998 (primary to them, secondary here):** Doerr et al. (1996), a fish-packing plant, found no significant productivity difference between low- and high-inventory systems "despite increased idle time with lower inventory". Janice Klein (1987) studied an engine plant after JIT and SPC; one manager there said, "The entire thing is very stressful—stressful for the slow person and stressful for the fast person."\[18\] Published cases specifically of *full-utilization* plans failing on a shop floor: **not found**.

What this means for optimization-and-scheduling: the 1998 result cuts *against* the naive worry. Behaviour made a low-buffer line *better* than the independence model predicted. The 2003 result shows behaviour can also erase modelled gains. Either way, the model's error has a direction, and that direction depends on design. A schedule that treats people as i.i.d. servers is wrong in a predictable way, not merely noisy.

### 4.5 Familiarity in redesigns; Hick and Hyman (Standard 5)

**Interface change cost:**
- Scarr, Cockburn, Gutwin & Quinn (CHI 2011, DOI 10.1145/1978942.1979348, n = 20, PowerPoint 2007 tasks). Switching to a well-designed new modality (Blur) cost little: 20.5 s rose to 20.9 s, and users had recovered by the third post-switch trial. A forced switch to Office Alt-key shortcuts gave mean times of "9.72, 9.92, 7.54, and 19.97 seconds for wimp, blur, blur-max and alt respectively"; "The performance dip with alt… was large… and participants would have immediately discontinued use if not required to do so."\[14\] Recovery for Alt: not measured.
- Scarr et al. (CHI 2012, CommandMaps, DOI 10.1145/2207676.2207713). Experienced Word 2010 users needed more than one Ribbon tab selection in "28% of trials". Error trials were 0.6% with CommandMaps, 5% with the Ribbon and 9% with menus.\[49\] No migration recovery period was measured.
- Mitchell & Shneiderman (1989, n = 63). Users given adaptive (reordering) menus first were "significantly slower", but by the second set of tasks performance "was not affected by menu style"; 81% preferred static menus.\[50\]\[51\]
- A controlled study measuring the recovery *period* after a familiar-interface redesign (such as the Ribbon migration): **not found**.

**Hick (1952),** *QJEP* 4(1):11–26, DOI 10.1080/17470215208416600, from the Applied Psychology Research Unit. "The analytical methods of information theory are applied to the data obtained in certain choice-reaction-time experiments." Further: "Now the hypothesis that the rate of gain of information is constant apparently requires that the reaction time should be proportional to log n."\[20\] Proctor & Schneider's 2018 review (QJEP 71(6):1281–1299) notes that "Hick (1952) reported three experiments" and lists "challenges to and shortcomings of Hick's law… including effects of stimulus–response compatibility, practice, very large set sizes and sequential dependencies."\[52\]\[53\]

**Hyman (1953),** *J. Exp. Psychol.* 45(3):188–196, DOI 10.1037/h0056940. The PsycINFO abstract (there is no author abstract) reads: information "was varied in 3 ways: (a) the number of equally probable alternatives…, (b) the proportion of times it could occur…, and (c) the probability of its occurrence as a function of the immediately preceding stimulus presentation. The reaction time to the amount of information in the stimulus produced a linear regression for each of the three ways".\[19\]\[30\] Antecedents: a later Psychonomic paper notes that apart from "Blank (1934), who postulated a logarithmic relationship, no quantitative theory emerged" before Shannon. It names "Crossman (1953) and Hyman (1953)" as the papers demonstrating the relation.\[28\]

### 4.6 Neutral retrieval (Standard 6)

Guidance from a standards body, regulator or peer-reviewed source on keeping an AI system's fact-finding free of the user's framing or leading questions: **not found** in this run (the search budget was exhausted before this question could be searched). The nearest human-factors anchor gathered is CDM's own protocol. Hoffman et al. (1998), as summarised in a secondary thesis, say the interviewer should retell the incident "following the participant's version as closely as possible, using the same vocabulary and wording".\[39\] That is a non-leading elicitation practice for human interviews, not AI guidance. See section 9 for candidates to check.

### 4.7 ISO 6385 and ISO 10075-3 (Standard 7)

- **ISO 6385:2016** (Edition 3, ISO/TC 159/SC 1). Stage 90.93 "International Standard confirmed". The ISO page as read on 16 Nov 2026 says: "This publication was last reviewed and confirmed in 2021. Therefore this version remains current."\[23\] ISO states: "A standard is reviewed every 5 years."\[23\] The **outcome of a 2026 systematic review is not posted**: not found. Do not record a 2026 confirmation.
- **ISO 10075-3:2004** (Edition 1). Stage "90.92 2025-02-26 International Standard to be revised"; "Will be replaced by Under development ISO/WD 10075-3".\[21\]
- **ISO/WD 10075-3** (Edition 2, project 91581). "10.99 2025-03-07 New project approved"; "20.00 2026-09-08 New project registered in TC/SC work programme"; "20.20 2026-10-01 Working draft (WD) study initiated"; "20.60 2026-10-16 Close of comment period". **Next stage: 20.99 "WD approved for registration as CD", then 30.00 CD registered.**\[22\] No expected dates are published: not found.

## 5. Tools

No software tools fall in scope for this run. These are the measurement instruments that the sources used.

| Tool | Purpose | Current version | Released | Install or run command | Config file | Source |
|---|---|---|---|---|---|---|
| Self-Report Habit Index (SRHI) | Habit strength, 12 items\[54\] | Verplanken & Orbell 2003 (no versioning)\[54\] | 2003 | N/A (questionnaire) | N/A | https://www.researchgate.net/publication/32898894_How_are_habits_formed_Modeling_habit_formation_in_the_real_world |
| SRBAI | Automaticity, 4-item SRHI subscale\[55\] | Gardner et al. 2012 | 2012 | N/A | N/A | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3552971/ |
| Chien et al. trust-in-automation scale | Cross-cultural trust (general and specific) | Validated in US, German, Taiwanese, Turkish samples\[56\] | 2014–2016 | N/A; dataset on openICPSR project 100532 (V3, 2017-10-29)\[57\] | N/A | https://www.openicpsr.org/openicpsr/project/100532/version/V3/view |
| NASA-TLX | Workload, used in Chien 2016\[8\] | Not established in this run | Not found | N/A | N/A | https://www.ri.cmu.edu/pub_files/2016/10/smc2016_ShihyiChien.pdf |

## 6. Changing in the next 12 months

- **ISO 10075-3:2004** is to be replaced by Edition 2. The WD comment period closed on 16 Oct 2026, and the next step is registration as a CD.\[22\] No publication or withdrawal date is published. **Flag:** the 2004 edition stays published until the replacement appears; that date was not found.
- **ISO 6385:2016**: the five-year cycle after the 2021 confirmation falls in 2026, but no outcome is posted. Re-check https://www.iso.org/standard/63785.html.
- No deprecations or announced breaking changes for the other sources (all journal articles).

## 7. Common mistakes

1. **"Hick's law: time grows linearly with the number of options."** Wrong. Hick's form is logarithmic in n ("proportional to log n"); Hyman's is linear in *information* (bits), including probability and sequence effects.\[20\]\[29\]
2. **Citing Hyman (1953) as vol. 30.** The Springer *Psychological Research* reference list misprints it. The correct citation is 45(3):188–196.\[30\]\[31\]
3. **Treating Hick's law as a fixed UI law.** Proctor & Schneider (2018) list practice, stimulus–response compatibility and very large set sizes as known shortcomings.\[53\]
4. **Calling CDM or *Working Minds* the origin of CTA.** Corrected above (since about 1980).\[1\]
5. **Citing vendor "productivity dip" numbers as research.** Bizowie's "80-90%… within 2-3 weeks" and the relayed Prosci figures have no published method.\[47\]
6. **Using Many Labs 2 to claim cross-cultural universality.** The 2024 re-analysis shows it had low power to detect cultural heterogeneity.\[13\]
7. **Reading the organ-donor gap as a pure default effect.** Secondary sources note structural confounds.\[9\]
8. **Reading Schultz 1998 as "people slow lines down".** Its measured effect went the *other* way (less idle time, higher output than predicted).\[18\]
9. **AI-assistant-specific errors.** No source documenting AI assistants making these mistakes was found. Items 1–2 are errors this run observed in the published literature and on secondary web pages that assistants commonly draw on.

## 8. Sources and licences

None of the licences below were verified unless stated. Where not verified, treat the source as publisher copyright (all rights reserved). An Apache-2.0 repository may then quote short passages with attribution and paraphrase freely with a citation, but may not copy figures, tables or long text. None of these sources contain code to adapt.

| Source | Licence | Quote? | Paraphrase? | Adapt code? | Attribution |
|---|---|---|---|---|---|
| Klein et al. 1989 (IEEE) | © IEEE (not verified) | Brief | Yes | N/A | Full citation + DOI 10.1109/21.31053 |
| Hoffman, Crandall & Shadbolt 1998 (SAGE/HFES) | © publisher (not verified) | Brief | Yes | N/A | Citation + DOI 10.1518/001872098779480442 |
| Militello & Hutton 1998 (Taylor & Francis); DTIC ADA335225 | T&F ©; DTIC report licence not verified | Brief | Yes | N/A | Citation + DOI 10.1080/001401398186108 |
| *Working Minds* (MIT Press 2006) | © MIT Press | Brief | Yes | N/A | Citation |
| Chien et al. 2016 (IEEE SMC; CMU-hosted PDF) | © IEEE (not verified) | Brief | Yes | N/A | Citation + URL |
| Jachimowicz et al. 2019 (Cambridge) | Not verified | Brief | Yes | N/A | Citation + DOI 10.1017/bpp.2018.43 |
| Many Labs 2 (SAGE 2018) | Not verified | Brief | Yes | N/A | Citation + DOI 10.1177/2515245918810225 |
| PMC11461273 (Communications Psychology 2024) | Not verified (Nature Portfolio journals are often CC BY; confirm on page) | Brief | Yes | N/A | Citation + DOI 10.1038/s44271-024-00135-z |
| Schultz et al. 1998 (INFORMS; Columbia-hosted PDF) | © 1998 INFORMS (stated on PDF)\[18\] | Brief | Yes | N/A | Citation + DOI 10.1287/mnsc.44.12.1595 |
| Schultz et al. 2003 (Elsevier/Wiley) | © publisher | Brief | Yes | N/A | Citation + DOI 10.1016/S0272-6963(02)00040-2 |
| Calder-Sprackman et al. 2021 (JACEP Open) | Not verified | Brief | Yes | N/A | Citation + DOI 10.1002/emp2.12362 |
| AHRQ R03HS018220 final report | Not verified (US federal grant report) | Brief | Yes | N/A | Citation + URL |
| McAfee 2002 (POM) | © publisher | Brief | Yes | N/A | Citation + DOI 10.1111/j.1937-5956.2002.tb00183.x |
| Scarr et al. 2011, 2012 (ACM CHI) | © ACM (not verified) | Brief | Yes | N/A | Citation + DOI |
| Hick 1952 (QJEP); Hyman 1953 (APA) | © T&F / APA | Brief | Yes | N/A | Citation + DOI |
| ISO 6385, ISO 10075-3 catalogue pages | © ISO | Brief (status lines only) | Yes | N/A | "ISO, [URL], read 16 Nov 2026" |
| Secondary: ResearchGate, Gale, Scribd copies, d-nb thesis, vendor blogs | Varies; Scribd copy of Hick may be unauthorised | Prefer the original publisher | Yes, labelled "secondary" | N/A | Name as secondary |

## 9. Not found, contested, not covered

**Not found**
- Non-Western replications of status quo bias and of habit *formation*, with sample sizes and effect sizes.
- Any controlled or field study comparing training, phased rollout, parallel running and super-users on dip length.
- Hours per study for contextual inquiry, HTA and CDM.
- Published shop-floor cases of full-utilization plans failing.
- A measured recovery period after a familiar-interface redesign such as the Ribbon.
- The outcome of ISO 6385's 2026 review.
- Expected dates for ISO/WD 10075-3's CD stage.
- Any standards-body, regulator or peer-reviewed guidance on neutral (non-leading) AI retrieval.
- Sources on AI assistants' specific errors in this area.

**Contested**
- Whether ERP/EHR performance recovers to baseline: McAfee 2002 and Cotteleer & Bendoly 2006 say yes; the interorganisational IS case and the ED EHR study say no.\[15\]\[58\]
- Whether Many Labs 2 shows culture rarely moderates effects: Klein et al. 2018 say so; the 2024 re-analysis says the data were too low-powered to show it.\[11\]\[13\]

**Not covered (candidates for R23d)**
- Neutral retrieval: check NIST AI 600-1 (Generative AI Profile), ISO/IEC 42001, and the peer-reviewed literature on LLM sycophancy and leading-question susceptibility. None were read in this run, so nothing is claimed about their content.
- Full texts of Schultz et al. 2003 and Hoffman et al. 1998 (cost and reliability figures).
- Cotteleer & Bendoly 2006 dip-magnitude figures. The paper found is *MIS Quarterly* 30(3):643–660, a Tristen Corporation ERP case, whose abstract says lead time "showed a significant improvement immediately after system deployment". The *POM* 15(1):74–87 paper is a separate article by Cotteleer (2006); check which one the citing case study means.

## Sources

1. [Use of the critical decision method to elicit - ProQuest](https://www.proquest.com/docview/216451434)
2. [Use of the critical decision method to elicit expert knowledge: a case study in the methodology of cognitive task analysis - Document - Gale Academic OneFile](https://go.gale.com/ps/i.do?asid=182c8eeb&id=GALE%7CA21159924&it=r&p=AONE&sid=googleScholar&u=googlescholar&v=2.1)
3. [Pub List 1970-1995 - Gary Klein](https://www.gary-klein.com/pub-list-1970-1995)
4. [\[PDF\] Applied cognitive task analysis (ACTA): a practitioner's toolkit for understanding cognitive task demands.](<https://www.semanticscholar.org/paper/Applied-cognitive-task-analysis-(ACTA):-a-toolkit-Militello-Hutton/ebeec8f791051ad4af266ba9739cc3c8cf7eacb6>)
5. [Applied Cognitive Task Analysis (ACTA) Methodology - DTIC](https://apps.dtic.mil/sti/tr/pdf/ADA335225.pdf)
6. [Applied cognitive task analysis (ACTA): A practitioner's toolkit for understanding cognitive task demands](https://uwe-repository.worktribe.com/index.php/output/9887108/applied-cognitive-task-analysis-acta-a-practitioners-toolkit-for-understanding-cognitive-task-demands)
7. [Working Minds](https://mitpress.mit.edu/9780262532815/working-minds/)
8. <https://www.ri.cmu.edu/pub_files/2016/10/smc2016_ShihyiChien.pdf>
9. [The Default Effect: The Behavioral-Economics Finding That Actually Holds Up](https://atticusli.com/replication-crisis/defaults-status-quo-anti-example/)
10. [Behavioural Public Policy : Volume 3 -](https://www.cambridge.org/core/journals/behavioural-public-policy/volume/1E6135ADFCBBC9AC9170DAEB3BBDA9DA)
11. [Many Labs 2: Investigating Variation in Replicability Across Samples and Settings](https://research.dial.uclouvain.be/entities/publication/43a4a6b3-bce2-4ac1-97f8-dc8d547113ea)
12. [Many Labs 2: Investigating variation in replicability across samples and settings - Tilburg University Research Portal](https://research.tilburguniversity.edu/en/publications/many-labs-2-investigating-variation-in-replicability-across-sampl-2/)
13. [Methodological concerns underlying a lack of evidence for cultural heterogeneity in the replication of psychological effects](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11461273/)
14. <https://www.csse.canterbury.ac.nz/andrew.cockburn/papers/blur.pdf>
15. [The impact of adoption of an electronic health record on emergency physician work: A time motion study - PubMed](https://pubmed.ncbi.nlm.nih.gov/33598662/)
16. [Grant Final Report Grant ID: R03HS018220-01](https://digital.ahrq.gov/sites/default/files/docs/publication/r03hs018220-fleming-final-report-2011.pdf)
17. [Realizing Benefits from Enterprise Resource Planning: Does Strategic Focus Matter?](https://www.researchgate.net/publication/229879922_Realizing_Benefits_from_Enterprise_Resource_Planning_Does_Strategic_Focus_Matter)
18. <https://business.columbia.edu/sites/default/files-efs/pubfiles/4395/modeling_and_worker_motivation.pdf>
19. [Stimulus information as a determinant of reaction... : Journal of Experimental Psychology](https://www.ovid.com/journals/joexps/fulltext/00004782-195303000-00010~stimulus-information-as-a-determinant-of-reaction-time)
20. [Rate of Information Gain in Psychology](https://www.scribd.com/document/223215951/Hick-1952)
21. [ISO 10075-3:2004 - Ergonomic principles related to mental workload — Part 3: Principles and requirements concerning methods for measuring and assessing mental workload](https://www.iso.org/standard/27571.html)
22. [ISO/WD 10075-3 - Ergonomic principles related to mental workload — Part 3: Principles and requirements concerning methods for measuring and assessing mental workload](https://www.iso.org/standard/91581.html)
23. [ISO 6385:2016 - Ergonomics principles in the design of work systems](https://www.iso.org/standard/63785.html)
24. [(PDF) Cognitive Task Analysis](https://www.researchgate.net/publication/317638184_Cognitive_Task_Analysis)
25. [Replication of Samuelson and Zeckhauser (1988)](https://open.lnu.se/index.php/metapsychology/article/view/2470/2535)
26. [Development and initial validation of the adolescent exercise habits scale among Chinese population - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12777359/)
27. [Hick%27s law](https://en.wikipedia.org/wiki/Hick%27s_law)
28. [Reaction time as a function of stimulus uncertainty on a ...](https://link.springer.com/content/pdf/10.3758/BF03213036.pdf)
29. [cognition - 7 Information Processing](https://www.crumplab.com/cognition/textbook/C7_Information_Processing.html)
30. [Stimulus information as a determinant of reaction time - PubMed](https://pubmed.ncbi.nlm.nih.gov/13052851/)
31. [The roles of stimulus and response uncertainty in forced-choice performance: an amendment to Hick/Hyman Law](https://link.springer.com/article/10.1007/s00426-015-0675-8)
32. [\[PDF\] Critical decision method for eliciting knowledge](https://www.semanticscholar.org/paper/Critical-decision-method-for-eliciting-knowledge-Klein-Calderwood/3069088b452ca5b02df350619524f5f7f7bd7cc6)
33. [Applied cognitive task analysis (ACTA): a practitioner's toolkit for understanding cognitive task demands - PubMed](https://pubmed.ncbi.nlm.nih.gov/9819578/)
34. [Applied cognitive task analysis (ACTA): A practitioner’s toolkit for understanding cognitive task demands](https://library.alnap.org/help-library/applied-cognitive-task-analysis-acta-a-practitioner%E2%80%99s-toolkit-for-understanding)
35. [When and why defaults influence decisions: a meta-analysis of default effects](https://www.cambridge.org/core/journals/behavioural-public-policy/article/when-and-why-defaults-influence-decisions-a-metaanalysis-of-default-effects/67AF6972CFB52698A60B6BD94B70C2C0)
36. [Overcoming the dark side of worker flexibility - Schultz - 2003 - Journal of Operations Management - Wiley Online Library](<https://onlinelibrary.wiley.com/doi/abs/10.1016/S0272-6963(02)00040-2>)
37. [The Influence of Cultural Factors on Trust in Automation](https://www.openicpsr.org/openicpsr/project/100532/version/V1/view)
38. [(PDF) How Habits are Formed](https://www.academia.edu/39279827/How_Habits_are_Formed)
39. [STRUCTURED ANALYSIS OF CRITICAL DECISION ...](https://d-nb.info/1273100530/34)
40. [Lessons Learned from Customizing and Applying ACTA to Design a Novel Device for Emergency Medical Care](https://arxiv.org/pdf/2108.05622)
41. [Working Minds: A Practitioner's Guide to Cognitive Task Analysis - Beth Crandall, Gary A. Klein, Robert R. Hoffman - Google Books](https://books.google.com/books/about/Working_Minds.html?id=CMNLEAAAQBAJ)
42. [Cognitive Task Analysis](https://railroads.dot.gov/human-factors/elearning-attention/cognitive-task-analysis)
43. [The impact of adoption of an electronic health record on emergency physician work: A time motion study - JACEP Open](<https://www.jacepopen.com/article/S2688-1152(24)01075-0/fulltext>)
44. [(PDF) Going Live: Implementing an Electronic Health Record System in the Emergency Department](https://www.researchgate.net/publication/270670575_Going_Live_Implementing_an_Electronic_Health_Record_System_in_the_Emergency_Department)
45. [Employee Experiences with an ERP Implementation](https://researchonline.stthomas.edu/view/pdfCoverPage?instCode=01CLIC_STTHOMAS&filePid=13439835020003691&download=true)
46. [Construction ERP Learning Curve: Realistic Milestones](https://cmicglobal.com/resources/article/What-a-Realistic-ERP-Learning-Curve-Looks-Like)
47. [ERP Implementation by the Numbers: Lessons from 100 Projects - Bizowie](https://bizowie.com/erp-implementation-by-the-numbers-lessons-from-100-projects)
48. [(PDF) Load Effect on Service Times](https://www.researchgate.net/publication/280883877_Load_Effect_on_Service_Times)
49. <https://www.csse.canterbury.ac.nz/andrew.cockburn/papers/commandMap-finalCamera.pdf>
50. [Publications of Ben Shneiderman - UMD Computer Science](http://www.cs.umd.edu/users/ben/publications.html)
51. [Figure 1 from Dynamic versus static menus: an exploratory comparison](https://www.semanticscholar.org/paper/Dynamic-versus-static-menus:-an-exploratory-Mitchell-Shneiderman/680e7bf6e948825a18d7d2b68764917bba992eca/figure/0)
52. [Hick's law for choice reaction time: A review - Web](https://web.ics.purdue.edu/~dws/pubs/ProctorSchneider_2018_QJEP.pdf)
53. [Hick’s law for choice reaction time: A review](https://ouci.dntb.gov.ua/en/works/4aq0yLM4/)
54. [How are habits formed: Modeling habit formation in the real world](https://www.researchgate.net/publication/32898894_How_are_habits_formed_Modeling_habit_formation_in_the_real_world)
55. [Towards parsimony in habit measurement: Testing the convergent and predictive validity of an automaticity subscale of the Self-Report Habit Index](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3552971/)
56. [Cross-Country Validation of a Cultural Scale in Measuring Trust in Automation](https://www.ri.cmu.edu/pub_files/2015/10/HFES2015.pdf)
57. [The Influence of Cultural Factors on Trust in Automation](https://www.openicpsr.org/openicpsr/project/100532/version/V3/view)
58. [(PDF) Measuring Success in Interorganizational Information Systems: A Case Study](https://www.researchgate.net/publication/279912299_Measuring_Success_in_Interorganizational_Information_Systems_A_Case_Study)
