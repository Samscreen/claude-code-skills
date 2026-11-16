# Cognitive task analysis

Read this for finding the judgment, cues and decisions behind expert work when watching it and
breaking it into goals don't show them: the Critical Decision Method, ACTA, what each produces
and costs, when to choose one over a visit or a goal hierarchy, and asking about an incident
without leading the person.

Watching and interviewing people at their work, goal hierarchies and where to stop are the
`studying-work` module's. What to do with a purpose once found, such as keep, change gradually
or override, is the `human-factors` module's. Interfaces are the `user-experience` skill's.

## Rules

1. **Use cognitive task analysis when the step turns on judgment you can't watch:** time
   pressure, rare events, or cues an expert notices and can't name. The Critical Decision Method
   was built for that ground (fact `cta-cdm-scope`). No study comparing it with a visit or a
   goal hierarchy was found, so this rests on each method's stated scope.
2. **Ground each interview in one real incident from the person's own experience,** then go
   back through it in passes (facts `cta-cdm-passes`, `cta-cdm-sweeps`). Questions about what
   they usually do get the procedure back.
3. **Don't lead.** Let them tell the incident first, retell it to them in their own words, and
   hold your theory back until the probes. An interview built on a personal account may cut
   interviewer bias, an open question (fact `cta-interviewer-bias`); the retelling is our
   practice.
4. **Choose ACTA when the team is new to this or time is short, the Critical Decision Method
   when depth matters.** ACTA was made for practitioners and is easy to learn (facts
   `cta-acta`, `cta-acta-workshop`).
5. **Have someone who knows the domain run or code the interviews,** or check the coding with
   one who does (fact `cta-cdm-coder`).
6. **Never rely on one method** (fact `cta-one-method`). Pair the interviews with a visit, the
   records, or a second method.
7. **Budget about two hours per Critical Decision Method interview** (fact `cta-cdm-sweeps`).
   No figure for a whole study was found.
8. **Label each finding by its evidence.** An incident retold is told, not seen: it holds what
   the person noticed and believed then, recalled now.

### Where it came from

Methods called cognitive task analysis date from about 1980 (fact `cta-since-1980`). The
Critical Decision Method grew from Flanagan's 1954 critical incident technique, adding probes
(fact `cta-cdm-flanagan`), and was named in 1989 (fact `cta-cdm-named`). *Working Minds*
(Crandall, Klein and Hoffman) is the handbook, published in 2006 (fact `cta-working-minds`),
not the origin.

### The full incident interview

The Critical Decision Method, step by step:

1. **Pick the incident:** a hard, non-routine case the person handled themselves, where their
   judgment changed the outcome.
2. **First telling:** they tell it start to finish. Don't interrupt.
3. **Retell it** to them in their words, and let them correct it.
4. **Time line:** build it together and mark each decision point.
5. **Deepen:** at each decision point, what did you notice, what did it tell you, what did you
   expect, what did you consider and reject?
6. **What-if:** what would have gone wrong here, and what would a less experienced person have
   missed?

It yields time lines, situation assessment records, decision requirements (fact
`cta-cdm-passes`) and, across many interviews, a cue inventory: each cue an expert reads, with
how it shows.

### The streamlined method

Applied cognitive task analysis (ACTA) is three interviews and a table (facts `cta-acta`,
`cta-acta-methods`):

- **Task diagram:** the person breaks the task into three to six steps and circles the ones
  that take hard thinking. About 20 minutes; it aims the rest.
- **Knowledge audit:** probes for short examples of expertise, such as spotting an anomaly,
  predicting, a trick of the trade, or working around poor equipment, then for the cues behind
  each.
- **Simulation interview:** the person works through a prepared scenario, then names its major
  events and is probed on each. It stands in for a rare incident nobody can recall well.
- **Cognitive demands table:** the findings in a form a designer or trainer can use.

### Which method

| The step | Use | Why |
|---|---|---|
| Follows a written goal; failures common enough to see | Goal hierarchy and visits, as in `studying-work` | Cheaper, and you see it |
| Happens while you watch, and the person can talk through it | Contextual inquiry | Ask as it happens |
| Judgment under time pressure, or cues the expert can't name | Critical Decision Method | Its probes reach what a visit doesn't show |
| The same, with a team new to it or a short schedule | ACTA | Less training; our reading is less depth |
| A rare event nobody recalls in detail | ACTA's simulation interview | Supplies the incident |

## Mistakes

- **Calling the Critical Decision Method or *Working Minds* the origin of cognitive task
  analysis.** The family is older (facts `cta-since-1980`, `cta-working-minds`).
- **Asking "what do you usually do?"** It gets the procedure. Ask about one incident.
- **Offering your theory of the cue before they've told the incident.** They may adopt it.
  Probe after the telling, in their words.
- **Coding interviews from a domain you don't know.** In Hoffman et al.'s check, the second
  coder marked too many decision points, which they put down to domain knowledge (fact
  `cta-cdm-coder`).
- **Treating ACTA's output as the Critical Decision Method's depth.** It trades depth for ease.
- **Quoting hours per study.** None was found; the two hours is one interview.
- **Claiming it beats a visit or a goal hierarchy as measured.** No comparison was found.
- **Reporting a retold incident as observed.** Label it told.

## Audit

Severity uses the standard's status words.

| Check | Look for | Severity | Fix |
|---|---|---|---|
| Judgment step studied by watching alone | A step under time pressure or with rare events, its purpose settled from a visit | `GAP` | Run incident interviews on it |
| General questions | Interview notes of "usually" and "normally", with no incident | `GAP` | Re-interview around one incident |
| Leading probes | Questions that name the cue or the answer before the telling | `DRIFT` | Tell first, probe after, in their words |
| Coder new to the domain | Decision points coded by someone outside it, unchecked | `DRIFT` | A domain expert codes or checks |
| One method only | Cognitive task analysis with no visit, records or second method | `GAP` | Add one |
| Evidence unlabeled | Retold incidents reported as seen | `DRIFT` | Label told, seen or inferred |
| Overstated method claims | Hours per study, a proven advantage, or the 2006 handbook as the origin | `DRIFT` | State them as the facts give them |
| Used on steps a visit shows | Incident interviews for a routine, visible step | `OVER` | Watch it instead |

## Why

### When to reach for it

- **The advice:** use it where the step rests on judgment, time pressure or rare events.
- **The reason:** the Critical Decision Method was made for tasks with "high time pressure,
  high information content, and changing conditions" (fact `cta-cdm-scope`). A visit samples
  ordinary days, and experts can't tell what they read in the cues, which the `studying-work`
  module also finds.
- **What others do:** contextual inquiry watches and asks during the work; a goal hierarchy
  starts from the task's goal and was built for training. Both are cheaper when the step shows.
- **What it costs:** cognitive task analysis "is resource intensive" (fact `cta-resource`).
- **Choose differently** when the step happens often, in view, and the person can say why.

### One incident, in passes, without leading

- **The reason:** a real incident gives cues and decisions in context; passes add the time line
  and depth without breaking the telling (fact `cta-cdm-sweeps`). Hoffman et al. argue that
  organizing the interview around a personal account may cut interviewer bias, and call it an
  open question (fact `cta-interviewer-bias`). Retelling in the person's words is our practice:
  it lets them correct the account before you add your own terms.
- **What it costs:** recall fades and bends with hindsight, so a retold incident is told
  evidence, not seen.
- **Choose differently** when no one recalls a fitting incident: use a simulation interview.

### The streamlined method or the full one

- **The reason:** ACTA was built because full cognitive task analysis cost too much for
  practitioners (fact `cta-resource`); its users found it easy to use (fact `cta-acta`), and
  graduate students new to it got accurate results after a 6-hour workshop (fact
  `cta-acta-workshop`).
- **What it costs:** our reading is that short examples and a prepared scenario give less depth
  than a full incident worked in passes. No verified comparison measured it.
- **Choose differently:** the Critical Decision Method for a high-stakes step, with an
  interviewer trained in it.

### Domain knowledge and more than one method

- **The reason:** two coders agreed on 81% of decision points; the second marked too many, which
  the authors expect of anyone new to the domain (fact `cta-cdm-coder`). The authors advise against relying on any single
  method (fact `cta-one-method`).
- **What it costs:** a domain expert's time, and a second method's.
- **Choose differently:** never for a decision that removes a step; one method may do to aim a
  first visit.

## Facts

Each named elsewhere in this module by its ID.

| ID | Fact | Source | Quote | Checked | Check by |
|---|---|---|---|---|---|
| `cta-cdm-scope` | The Critical Decision Method's scope, Klein, Calderwood and MacGregor, *IEEE Trans. SMC* 19(3), 1989 | [Klein et al., 1989](https://doi.org/10.1109/21.31053) | "A critical decision method is described for modeling tasks in naturalistic environments characterized by high time pressure, high information content, and changing conditions." | 2026-11-16 | 2027-05-16 |
| `cta-cdm-flanagan` | It descends from Flanagan's critical incident technique | [Klein et al., 1989](https://doi.org/10.1109/21.31053) | "The method is a variant of a J.C. Flanagan's (1954) critical incident technique extended to include probes" | 2026-11-16 | 2027-05-16 |
| `cta-since-1980` | Cognitive task analysis dates from about 1980; Hoffman, Crandall and Shadbolt, *Human Factors* 40(2), 1998 | [Hoffman et al., 1998, Free Library copy](https://www.thefreelibrary.com/Use+of+the+critical+decision+method+to+elicit+expert+knowledge%3a+a...-a021159924) | "Since about 1980, many studies have used diverse methods that have been called cognitive task analysis" | 2026-11-16 | 2027-05-16 |
| `cta-cdm-named` | The method was named in 1989 | [Hoffman et al., 1998, Free Library copy](https://www.thefreelibrary.com/Use+of+the+critical+decision+method+to+elicit+expert+knowledge%3a+a...-a021159924) | "These studies led to some refinements of the method, culminating in the designation Critical Decision Method (Klein, Calderwood, & MacGregor, 1989)." | 2026-11-16 | 2027-05-16 |
| `cta-cdm-passes` | Passes with probes; its products | [Hoffman et al., 1998, abstract](https://journals.sagepub.com/doi/10.1518/001872098779480442) | "The method involves multiple-pass event retrospection guided by probe questions." and "(e.g., Situation Assessment Records, time lines, decision requirements)" | 2026-11-16 | 2027-05-16 |
| `cta-cdm-sweeps` | Three sweeps; about two hours per interview | [Hoffman et al., 1998, Free Library copy](https://www.thefreelibrary.com/Use+of+the+critical+decision+method+to+elicit+expert+knowledge%3a+a...-a021159924) | "What follows are three information-gathering sweeps back through the incident." and "Typically a full CDM procedure takes about 2 h." | 2026-11-16 | 2027-05-16 |
| `cta-interviewer-bias` | A personal account may cut interviewer bias, unproven | [Hoffman et al., 1998, Free Library copy](https://www.thefreelibrary.com/Use+of+the+critical+decision+method+to+elicit+expert+knowledge%3a+a...-a021159924) | "by requesting personal accounts of a specific event and organizing the interview around that account, potential interviewer biases can likewise be minimized" and "This too is an open empirical question." | 2026-11-16 | 2027-05-16 |
| `cta-cdm-coder` | Sensitive to the coder's domain knowledge | [Hoffman et al., 1998, Free Library copy](https://www.thefreelibrary.com/Use+of+the+critical+decision+method+to+elicit+expert+knowledge%3a+a...-a021159924) | "Across transcripts of four incident accounts, the two coders agreed in their identification of 81% of the decision points." and "the CDM method can be modestly sensitive to the domain knowledge of the elicitor/coder" | 2026-11-16 | 2027-05-16 |
| `cta-one-method` | Don't rely on one method | [Hoffman et al., 1998, Free Library copy](https://www.thefreelibrary.com/Use+of+the+critical+decision+method+to+elicit+expert+knowledge%3a+a...-a021159924) | "one should not rely on any single method" | 2026-11-16 | 2027-05-16 |
| `cta-resource` | Cognitive task analysis is costly; Militello and Hutton, *Ergonomics* 41(11), 1998 | [PubMed 9819578](https://pubmed.ncbi.nlm.nih.gov/9819578/) | "However, CTA is resource intensive and has previously been of limited use to design practitioners." | 2026-11-16 | 2027-05-16 |
| `cta-acta` | ACTA: three interviews, easy to use | [PubMed 9819578](https://pubmed.ncbi.nlm.nih.gov/9819578/) | "ACTA consists of three interview methods that help the practitioner to extract information about the cognitive demands and skills required for a task." and "ACTA techniques were found to be easy to use, flexible, and to provide clear output." | 2026-11-16 | 2027-05-16 |
| `cta-acta-methods` | The three interviews; the task diagram's length | [Militello, synoptic report, 2026](https://knowledge.lancashire.ac.uk/id/eprint/59302/1/Militello%2C%20Laura_PhDbyPublication_SynopticReportReSubmission_15Feb26.pdf) | "The ACTA methods include the Task Diagram, the Knowledge Audit, and the Simulation Interview, each with a particular focus" and "This interview generally takes 20 minutes or less" | 2026-11-16 | 2027-05-16 |
| `cta-acta-workshop` | Novices did well after a 6-hour workshop | [Militello, synoptic report, 2026](https://knowledge.lancashire.ac.uk/id/eprint/59302/1/Militello%2C%20Laura_PhDbyPublication_SynopticReportReSubmission_15Feb26.pdf) | "after a 6-hour workshop introducing the ACTA techniques, graduate students were able to elicit relevant, domainspecific, accurate cognitive information" | 2026-11-16 | 2027-05-16 |
| `cta-working-minds` | *Working Minds*, MIT Press, 2006: a handbook | [MIT Press](https://mitpress.mit.edu/9780262532815/working-minds/) | "Pub date: July 7, 2006" and "Working Minds is a true handbook" | 2026-11-16 | 2027-05-16 |

## Sources

| Source | Used for | License |
|---|---|---|
| Klein, Calderwood and MacGregor, 1989 | The method's scope and lineage | Copyright IEEE: brief quotes, our own words |
| Hoffman, Crandall and Shadbolt, 1998 | The method, its products, bias, coding, more than one method | Copyright Human Factors and Ergonomics Society: brief quotes, our own words |
| Militello and Hutton, 1998 | ACTA, its cost and ease | Copyright Taylor & Francis: brief quotes, our own words |
| Militello, synoptic report, 2026 | ACTA's interviews and workshop | Not stated: brief quotes, our own words |
| MIT Press, *Working Minds* | The handbook's date | Copyright MIT Press: brief quotes |
