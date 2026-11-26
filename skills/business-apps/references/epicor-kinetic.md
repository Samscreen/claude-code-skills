# Epicor Kinetic

Read this for server-side work on Epicor Kinetic or ERP 10.2.x: BPM method, data and updatable
BAQ directives, C# in directives and Epicor Functions, BAQs, REST API v2 and its keys, and
upgrading from 10.2.x.

C# itself is `coding`'s `csharp-coding`; SQL outside Epicor is `data`; API design is
`architecture`'s `api-patterns`. A company's own directives, UD fields, servers and release
belong in its own skills. This module rests on Epicor's public pages and its user forum, as
Epicor's help is for customers: check each pattern against the help on the release in use. Its C# compiles only inside Kinetic, so it's unchecked and not yet proven on a named release.

## Rules

1. **Know the release before writing code:** ERP 10.2.x, Kinetic on premises, or Kinetic in
   Epicor's cloud, monthly since May 2026 (fact `ek-cadence`). Code that compiles on one fails on
   another: the server moved to .NET 6 in 2022.1 (fact `ek-net6`), and queries to EF Core in
   2026.1 (fact `ek-efcore`).
2. **Put each rule where it holds.** A rule that must hold however data arrives goes in a BPM,
   not a screen layer. A method directive changes one business object method; a data directive
   watches one table, whichever method writes it; an updatable BAQ directive handles that BAQ's
   methods; a Function holds logic several callers share (fact `ek-functions-page`).
3. **Validate in pre-processing, follow up in post-processing.** Pre-processing runs before the
   base method and stops it with an exception. Leave base processing alone: it replaces Epicor's
   own method.
4. **Keep in-transaction data directives small.** They run inside the save, on every write of a
   row; a standard directive runs once per table after the call succeeds (fact `ek-intran`). Set
   the row's fields or stop the save there. Business object calls, mail and network calls go in
   a standard directive or post-processing.
5. **Conditions first, code last.** Narrow each directive with the designer's conditions so most
   calls do nothing, and move long code into a Function the directive calls.
6. **Read with `Db`, write through business objects.** Select only the columns needed, filtered
   by `Company`. Change other records with the service's methods, in the order the screen calls
   them (trace it), so Epicor's validation and directives run. Writing `Db` rows skips both.
7. **Write queries EF Core accepts,** from 2025.2 on (fact `ek-efcore`): copy a value into a
   local before a query uses it; no `DbFunctions`, `SqlFunctions` or `StringComparison` in a
   query; no default value in `FirstOrDefault`; `ToList()` one query before starting the next;
   never set an identity column. `#if USE_EF_CORE` keeps one source for both.
8. **Method directives use `ds.Table`; data directives `ttTable`** (fact `ek-tt-ds`). Test a
   row's state with `Added()`, `Updated()` or `Deleted()`, and every `FirstOrDefault()` for null.
9. **Guard against a directive calling itself.** A business object called from a directive runs
   its own directives too. Test a condition the second pass fails, not a shared
   `callContextBpmData` field another directive may use.
10. **REST v2 takes an API key and a login on every call,** with the company in the path (facts
    `ek-v2-key`, `ek-rest-page`). Each integration gets its own key, an access scope listing only
    what it calls, and its own user. The key goes in the `x-api-key` header, never in a URL.
11. **Read through a BAQ; write through a Function or a business object.** A BAQ is at
    `/api/v2/odata/{Company}/BaqSvc/{BaqID}/Data`, a Function a `POST` to
    `/api/v2/efx/{Company}/{Library}/{Function}` (facts `ek-rest-shape`, `ek-rest-v2`). Nothing
    writes to Epicor's database from outside.
12. **Upgrade with an inventory and a pilot.** List every directive, Function, external assembly
    and Classic customization; keep their code in version control before the conversion rewrites
    it; check syntax on each and test it in the pilot. Classic customizations become Application
    Studio layers (fact `ek-smart-client`).

### Stopping a save

Pre-processing on `Erp.SalesOrder.Update`. The designer's Raise Exception action needs no code;
code earns its place when the rule loops or looks things up.

<!-- example: unchecked, compiles only in Kinetic's BPM editor; not yet proven on a named release -->
```csharp
foreach (var order in ds.OrderHed.Where(r => r.Added() || r.Updated()))
{
    if (string.IsNullOrWhiteSpace(order.PONum))
    {
        throw new Ice.BLException($"Order {order.OrderNum} needs the customer's PO number.");
    }
}
```

### A read EF Core accepts

<!-- example: unchecked, compiles only in Kinetic's BPM editor; not yet proven on a named release -->
```csharp
var order = ds.OrderHed.FirstOrDefault(r => r.Added());
if (order == null) return;

string company = Session.CompanyID;
int custNum = order.CustNum; // a plain local, which EF Core can translate
bool onHold = Db.Customer
    .Where(c => c.Company == company && c.CustNum == custNum)
    .Select(c => (bool?)c.CreditHold)
    .FirstOrDefault() ?? false;
```

### A business object call in a Function

The library references the service; `orderNum` and `poNum` are the Function's inputs. A
directive uses `Ice.Assemblies.ServiceRenderer.GetService<T>(Db)`, in `using`.

<!-- example: unchecked, compiles only in Kinetic's Functions editor; not yet proven on a named release -->
```csharp
this.CallService<Erp.Contracts.SalesOrderSvcContract>(svc =>
{
    var ts = svc.GetByID(orderNum);
    ts.OrderHed[0].PONum = poNum;
    ts.OrderHed[0].RowMod = "U";
    svc.Update(ref ts);
});
```

### Reading a BAQ over REST v2

Compiled, not yet run against a server. Paging needs an `$orderby`, or rows move between pages.

```python
import os

import requests

BASE = os.environ["KINETIC_URL"]  # https://erp.example.com/<instance>/api/v2
COMPANY = os.environ["KINETIC_COMPANY"]

session = requests.Session()
session.auth = (os.environ["KINETIC_USER"], os.environ["KINETIC_PASSWORD"])
session.headers.update({"x-api-key": os.environ["KINETIC_API_KEY"], "Accept": "application/json"})


def baq_rows(baq_id, order_by, page=500):
    """Every row of a BAQ, a page at a time."""
    url = f"{BASE}/odata/{COMPANY}/BaqSvc/{baq_id}/Data"
    skip = 0
    while True:
        query = {"$orderby": order_by, "$top": page, "$skip": skip}
        response = session.get(url, params=query, timeout=60)
        response.raise_for_status()
        rows = response.json()["value"]
        yield from rows
        if len(rows) < page:
            return
        skip += page
```

A Function is `session.post(f"{BASE}/efx/{COMPANY}/{library}/{function}", json=inputs)`.

## Mistakes

- **`ttOrderHed` in a Kinetic method directive.** It's `ds.OrderHed` (fact `ek-tt-ds`). The
  upgrade's rename also hits local variables whose names start with `tt`.
- **A business object call, mail or a web call in an in-transaction directive.** It runs on
  every write of the row, inside the save.
- **EF6 code on 2026.1:** `System.Data.Entity`, `DbFunctions`, `FirstOrDefault(false)`, or a
  second query while the first is open (fact `ek-efcore`).
- **`System.Data.SqlClient` or a .NET Framework assembly in server code** since 2022.1 (fact
  `ek-net6`).
- **A v2 call without `x-api-key`,** a v1 URL with `v1` changed to `v2`, or a BAQ URL without
  `/Data` (facts `ek-v2-key`, `ek-rest-shape`).
- **Smart Client customization code for Kinetic** (fact `ek-smart-client`): it's Application Studio.

## Audit

Severity uses the standard's status words.

| Check | What to look for | Severity | Fix |
|---|---|---|---|
| Release named | The release the code targets | `GAP` | Ask, and name the facts that differ |
| In-transaction weight | Service calls, mail, network calls or `Db` loops in an in-transaction directive | `BLOCKER` | Move them to a standard directive or post-processing |
| Company filter | Every `Db` query and BAQ join uses `Company` | `BLOCKER` | Add it |
| Direct writes | Assignments to `Db` rows of a table the directive doesn't own | `DRIFT` | Call the business object's methods |
| EF Core | `System.Data.Entity`, `DbFunctions`, `SqlFunctions`, defaults in `FirstOrDefault`, another row's fields inside a query | `BLOCKER` on 2026.1, `GAP` before | Rewrite, or `#if USE_EF_CORE` |
| API keys | A key and access scope per integration, sent in a header | `GAP` | Issue them; rotate a key seen in a URL |
| Code kept | Directive and Function code in version control | `GAP` | Export it before the next upgrade |

## Why

### A directive, a Function or a screen

- **The advice:** rules in directives; shared or outside-facing logic in Functions; screens in
  Application Studio.
- **The reason:** a screen layer runs for its screen alone, and every service is on REST (fact
  `ek-rest-page`), so other callers skip a rule kept there.
- **What others do, and why:** many keep a directive to a condition and a Function call, so the
  code lives in one place.
- **What it costs:** a Function needs a library, a published version and a security role (fact
  `ek-rest-v2`), and adds a hop.
- **When to choose differently:** a one-line check on one method can stay in its directive.

### Small in-transaction directives, writes through business objects

- **The advice:** in-transaction, set the row's own fields or stop the save; elsewhere, change
  records with the methods the screen calls.
- **The reason:** the directive fires on every write inside the transaction (fact `ek-intran`),
  so a service called there runs inside a trigger. A direct write skips the validation, change
  methods and directives a business object runs.
- **What it costs:** a standard directive can't stop the save; business objects take more code.
- **When to choose differently:** a UD table only your own code writes.

### What changed from 10.2.x

| Area | ERP 10.2.x | Kinetic |
|---|---|---|
| Server | .NET Framework | .NET 6 and later from 2022.1 (fact `ek-net6`) |
| Queries in custom code | EF6 | EF Core from 2026.1 (fact `ek-efcore`) |
| Method directive tables | `ds.Table`, and `ttTable` | `ds.Table` only (fact `ek-tt-ds`) |
| REST v2, Functions | From 10.2.400 and 10.2.500 (fact `ek-rest-v2`) | Both |
| Screens | Classic forms, C# customizations | Application Studio (fact `ek-smart-client`) |
| Releases | Updates within 10.2 | Twice a year, then monthly in the cloud from May 2026; 2028.1 last on premises (facts `ek-cadence`, `ek-onprem-final`) |

## Facts

Versions, dates and defaults, each named elsewhere in this module by its ID. Checked 2026-11-26.
Forum rows quote Epicor staff where a post exists, and otherwise users reporting what they ran.

| ID | Fact | Source | Quote | Checked | Check by |
|---|---|---|---|---|---|
| `ek-cadence` | Kinetic releases monthly from May 2026 | [Epicor blog](https://www.epicor.com/en-us/blog/industries/release-2026-100-of-kinetic/) | "Kinetic is moving away from a semi-annual model and toward a monthly CI/CD cadence." | 2026-11-26 | 2027-02-26 |
| `ek-smart-client` | 2025.2 is the last release with the Smart Client; Classic forms retired 2026-05 | [Epicor blog](https://www.epicor.com/en-us/blog/industries/release-2025-2-of-kinetic/) | "With 2025.2 as the final release supporting Smart Client" | 2026-11-26 | 2027-05-26 |
| `ek-onprem-final` | 2028.1 is the last on-premises feature release; Active Support through 2029-12-31 | [Epicor news](https://www.epicor.com/en-us/newsroom/news-releases/epicor-announces-schedule-of-final-on-premises-feature-releases/) | "Final on-premises release: 2028.1" and "Active Support for release 2028.1 through December 31, 2029" | 2026-11-26 | 2027-05-26 |
| `ek-functions-page` | Functions take C# and run from directives, REST and schedules | [Epicor Functions](https://www.epicor.com/en-us/products/enterprise-resource-planning-erp/kinetic/tools-and-technology/epicor-functions/) | "include custom C# code within functions" and "Functions can be called from BPM directives, application events, RESTful services, scheduled jobs, or other functions" | 2026-11-26 | 2027-05-26 |
| `ek-rest-page` | Every service is on REST, as OData v4, behind API keys and scopes | [Open REST API](https://www.epicor.com/en-us/products/enterprise-resource-planning-erp/kinetic/tools-and-technology/open-rest-api/) | "REST services follow the OData v4 standard" and "API keys, access scopes, and standard authentication methods control which services" | 2026-11-26 | 2027-05-26 |
| `ek-rest-v2` | REST v2 came in 10.2.400 and Functions in 10.2.500; C# in a Function needs Power Developer | [Bart Elia (Epicor)](https://www.epiusers.help/t/lets-get-funcy-epicor-functions/59714) | "spoke the Odata 4 spec" and "In 10.2.500, Epicor ERP brings this to market as Epicor Functions." and "the Power Developer role is required to write C# code" | 2026-11-26 | 2027-05-26 |
| `ek-v2-key` | REST v2 refuses a call without an API key, and needs a login too | [Forum](https://www.epiusers.help/t/rest-services-v2/57725) | "Rest v2 requires both an authorized login and an api key." and "Rest calls must pass a valid API Key" | 2026-11-26 | 2027-05-26 |
| `ek-rest-shape` | A BAQ's v2 URL ends in `/Data`; a Function's is under `/api/v2/efx/` | [Forum](https://www.epiusers.help/t/rest-efx-baq-examples-from-a-python-script/115273) | "BaqSvc/KEV_ABC/Data" and "api/v2/efx/Company/TestDataLibrary" | 2026-11-26 | 2027-05-26 |
| `ek-net6` | From 2022.1 the server runs on .NET 6, with `Microsoft.Data.SqlClient` | [Epicor staff](https://www.epiusers.help/t/broken-bpm-after-upgrade-pilot/89444) and [forum](https://www.epiusers.help/t/call-store-procedure-in-kinetic-function-not-working/100890) | "the server runs on .NET 6" and "System.Data.SQLClient has been replaced with Microsoft.Data.SQLClient" | 2026-11-26 | 2027-05-26 |
| `ek-efcore` | Custom code queries run on EF Core from 2026.1; 2025.2 warns | [Epicor's notes, on the forum](https://www.epiusers.help/t/entity-core-framework-fix-at-2026-100/135268) | "EF Core does not support DbFunctions" and "USE_EF_CORE which is a conditional compilation value" | 2026-11-26 | 2027-05-26 |
| `ek-tt-ds` | Upgrades rename method directives' `tt` tables to `ds`; data directives keep `tt` | [Forum](https://www.epiusers.help/t/bpms-not-functioning-after-kinetic-upgrade/93003) and [forum](https://www.epiusers.help/t/upgrading-to-2023-1-8-and-jobmtl-rowmod-is-no-longer/108554) | "renames them to ds.XXXX for you during the upgrade" and "tt tables are still used for data directives." | 2026-11-26 | 2027-05-26 |
| `ek-intran` | In-transaction directives fire on every write; standard ones once per table | [Forum](https://www.epiusers.help/t/data-directive/59479) | "In-Transaction DD fire on every update to the DB. Standard DD fire once per table" | 2026-11-26 | 2027-05-26 |

## Sources

Every source, with its license and how this module uses it: quoted, adapted with a notice, or
stated in our own words with a link.

| Source | Used for | License |
|---|---|---|
| [Epicor's blog, news and product pages](https://www.epicor.com/en-us/products/enterprise-resource-planning-erp/kinetic/tools-and-technology/) | Releases, support dates, BPM, Functions, REST | Epicor copyright: our own words, short quotes |
| [Epicor User Help Forum](https://www.epiusers.help/) | Release changes, directive behavior, URL shapes | Each poster's, no open license found: our own words, short quotes; our own code |
| Epicor's product help, EpicCare and EpicWeb | Not used | Customers only |
