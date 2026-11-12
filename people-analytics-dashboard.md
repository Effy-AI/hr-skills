# Build a people analytics dashboard

**People analytics dashboard** (`people_analytics_dashboard`)  
Finds which of your connected tools hold people data, tells you what each export would unlock,
then builds one dashboard — headcount, attrition, engagement, performance, mobility, pay
equity, hiring, absence, D&I, workforce planning — with a formula under every chart. Falls back
to a fully worked sample dashboard if you have no data to hand.

The user wants a people analytics dashboard they can open again next month and send upward. Not a
pile of charts — a page where each block answers a question, the numbers carry a comparison, and
every metric says how it was calculated so nobody argues about definitions in the meeting.

Work in three phases. Don't build anything until phase 2 is done.

## Ground rules

- **No invented numbers.** Every figure comes from data the user gave you or a tool you read. If
  you build the sample version, label it as sample on every screen.
- **Anonymity threshold of 5.** Any survey-derived slice with fewer than five respondents is
  suppressed and shown as "n<5". Individual-level views (flight risk, pay) carry a visible note
  that they're for HR and the direct manager only.
- **State the denominator.** Turnover uses headcount at the start of the period unless the catalog
  below says average headcount. Mixing denominators across cards makes the numbers disagree with
  each other.
- **A number without a comparison is decoration.** Every KPI carries a delta against the prior
  period or a benchmark the user supplied. If neither exists, say "no comparison available" rather
  than showing a bare figure. Don't supply benchmarks from memory.
- **A predictive score without its drivers is ignored.** If you show flight risk or an attrition
  forecast, show the reasons next to the score, and only build them when the data supports it.
- **No compensation or legal advice.** Pay-equity numbers are reported as findings; decisions on
  them need HR, finance or legal.

## Phase 1 — Find what data is already reachable

Before asking for anything, look at the tools you can call in this session. Search for anything
that reads employees, HR records, payroll, surveys, engagement, reviews, performance, goals or
growth plans, career levels, applicants, requisitions, time off, or files and spreadsheets
(Drive, Sheets, OneDrive, Notion, Airtable). Vendors worth checking: HiBob, Personio, BambooHR,
Rippling, Deel, Gusto, Workday, Lattice, Leapsome, Culture Amp, 15Five, Greenhouse, Lever, Ashby,
Effy AI. In Effy AI: the employee directory feeds headcount and span of control, review reports
feed performance, growth plans feed growth-plan coverage, career tracks and assignments feed level
mix, and 1-on-1 activities show 1:1 cadence per manager.

For each candidate, make one small read to confirm the fields exist and are populated. A
"department" column that's empty for everyone means that block can't segment.

Name any connector that's configured but not authorised or failed to connect — that's a gap the
user may be able to fix in one click.

Then show a short table: **source → which blocks it can feed → what's still missing**. Skip
connectors that can't help (CRM, calendar, email, SEO tools).

## Phase 2 — Ask for data, and show what each kind unlocks

Ask what the user can upload or point you to, and make the ask concrete with this table (drop rows
phase 1 already covers):

| If you give me… | I can build… |
| --- | --- |
| Employee list — ID, department, manager, level, start date, contract type, location; gender optional | Headcount & composition, and the segmentation every other block uses |
| Exits — ID, exit date, voluntary/involuntary, regretted flag, reason | Retention & attrition: turnover, regretted, first-year, cohorts, heatmaps |
| Survey results — segment (never the person), theme, score, date; an eNPS 0–10 item | Engagement & sentiment: trend vs benchmark, eNPS, drivers, heatmaps |
| Review data — ID, cycle, self rating, manager rating, 9-box, goal completion | Performance & talent: distributions, calibration by manager, self–manager gap |
| Level history — ID, level, effective date | Career & mobility: promotion rate, time since promotion, time in level |
| Salaries + bands — ID, salary, band min/mid/max, gender, level | Compensation & pay equity: compa-ratio, gender pay gap by level |
| ATS export — requisition dates, stages, offers, source | Hiring: time to fill vs hire, funnel, source quality, offer acceptance |
| Time off / attendance — ID, type, days, month | Absence & wellbeing: absenteeism, PTO use, overtime, sick leave |
| Consented demographics + inclusion survey items | Diversity & inclusion: representation by level, fairness of hires/promotions/exits |
| Revenue and headcount plan by department | Workforce planning: revenue per employee, labour cost %, plan vs actual |

Take anything tabular — CSV, spreadsheet, Google Sheet, Notion database, a pasted table. When
something arrives, profile it before promising anything: columns, row count, date range, and a
feasibility line per block ("Retention: feasible — exit date and type found; regretted flag
missing, so no regretted attrition card"). If a column header is ambiguous, ask **one** question
about it. Don't guess what `status` means.

**If the user has nothing, or says "just show me what it looks like":** offer the sample dashboard
explicitly — all ten blocks on invented data for a fictional company of around 400 people, so
they can see every chart and decide which they want on their own data. If they say yes, build it,
keep the "sample data" label visible on every block, and stop there unless they ask for changes.

## Phase 3 — Choose the blocks, compute, build

Pick blocks, not everything. Four full blocks beat ten half-empty ones. Include a block when its
top two or three metrics can be computed from what you have; skip it and say why otherwise. Order
by the priority below unless the user's question dictates otherwise — if they asked "why are
people leaving", Retention comes first, then Engagement, then Compensation.

Compute every metric before writing a line of the page. For anything beyond a handful of rows, do
the arithmetic in code from the files, and keep that code so the numbers can be re-run on next
month's export. Never hand-type an aggregate.

**Build it as a dashboard artifact if the session offers one; otherwise as one self-contained HTML
page**: a left-hand navigation of blocks; each block opens with the question it answers, the data
sources, and 3–4 KPIs with deltas; then the charts; under every chart, the formula used and one
sentence on why that chart type. Green / amber / red mean good / watch / act and nothing else.
Both light and dark themes must be readable. Charts read to one labelled scale. Use a heatmap for
two categorical dimensions times one rate, ranked horizontal bars for long labels, a line with a
dashed prior-period or benchmark reference for trends, stacked bars when the total matters as much
as the split. **If you can produce neither**, output the KPIs and tables in chat as markdown, block
by block, with the same formula notes.

## The metrics catalog

Ten blocks in priority order for a 30–1000 person company. Inside each block, metrics are in
priority order. Each line: metric — what it shows · *formula* · best view. Where no standard
formula exists, the line says so.

**1. Headcount & composition** (foundation — everything else segments on this)
- Headcount — size at a point in time · *active employees on the date; FTE = contracted hours ÷ full-time hours* · line over time, stacked bar by department
- Movements — where growth comes from · *hires, exits, transfers per period* · waterfall start → +hires → −exits → end
- Tenure distribution — how fragile the org is · *months since start, bucketed <1y, 1–2, 2–5, 5+* · histogram
- Span of control — manager load · *direct reports ÷ managers, plus per-manager spread* · histogram with 6–9 target band
- Layers — org depth · *max reporting levels from CEO* · number or table
- Employment type mix · *count by type ÷ headcount* · donut
- Manager ratio · *managers ÷ headcount* · KPI with benchmark

**2. Retention & attrition** (the most-used block)
- Turnover rate · *exits in period ÷ headcount at start × 100* · monthly line with 12-month rolling average and prior-year dashed
- Voluntary vs involuntary · *same, split by exit type* · stacked bar by month
- Regretted attrition · *regretted voluntary exits ÷ average headcount × 100; also share of voluntary exits* · KPI + bar by department
- First-year attrition · *hires who left within 12 months ÷ hires in cohort × 100* · bar by hiring quarter
- Retention by cohort · *still active at month N ÷ cohort size × 100* · survival curves
- Turnover by segment · *rate by department × tenure band* · heatmap
- Exit reasons · *count by categorised reason ÷ voluntary exits* · sorted horizontal bar
- Flight risk · *no standard — model on tenure, months since promotion or raise, engagement trend, manager change, rating* · ranked table with drivers; role-gated

**3. Engagement & sentiment**
- Engagement score · *% of responses at 4–5 on a 5-point scale across core items* · KPI with trend and benchmark
- eNPS · *% promoters (9–10) − % detractors (0–6); range −100 to +100* · stacked 100% bar by quarter
- Driver analysis · *correlation of each theme with the engagement outcome* · scatter of impact × score; bottom-right quadrant is the action list
- Engagement by segment · *score by department × quarter* · heatmap
- Participation · *responses ÷ invited × 100* · KPI; hide slices under 5
- Open-text themes · *comments classified by theme and by positive/negative* · horizontal bar coloured by sentiment
- Manager effectiveness · *mean of upward-feedback items per manager; define once, keep stable* · ranked bars with org median, managers with ≥5 respondents only

**4. Performance & talent**
- Rating distribution · *count per level ÷ rated × 100* · bar with guideline overlay
- Distribution by manager · *same per reviewer, ≥5 reports* · heatmap
- Self vs manager gap · *mean(manager − self) per team* · diverging bar around zero
- 9-box · *count per cell* · 3×3 grid
- Goal completion · *achieved ÷ set × 100; average progress of open goals* · line by cycle
- Review completion · *completed ÷ assigned × 100* · progress bar
- Pay vs performance · *rating against compa-ratio* · scatter
- High-performer retention · *voluntary turnover of top rating bands vs everyone else, trailing 12 months* · two lines

**5. Career & mobility**
- Promotion rate · *promotions ÷ average headcount × 100* · bar by department, line by quarter
- Time since last promotion · *months since last level change* · histogram, flag 30+
- Internal mobility · *transfers ÷ average headcount × 100* · stacked with promotions
- Internal fill rate · *roles filled internally ÷ total filled × 100* · KPI
- Growth-plan coverage · *active plans ÷ headcount × 100* · progress bars with target
- Time in level · *average months before promotion, per level* · bar per level

**6. Compensation & pay equity** (EU Pay Transparency Directive reporting applies from 2026 — check current national transposition before stating obligations)
- Compa-ratio · *salary ÷ band midpoint* · histogram; in-range 0.90–1.10
- Range penetration · *(salary − band min) ÷ (band max − band min)* · bar per level
- Gender pay gap, unadjusted · *(median male − median female) ÷ median male × 100, per level* · bar with 5% threshold line
- Adjusted pay gap · *regression residual after level, role, tenure; no simple formula* · KPI with confidence note
- Payroll cost per employee · *total comp ÷ headcount* · stacked bar by department over time
- Merit distribution · *median increase ÷ prior salary × 100, per rating band* · grouped bar by cycle
- Pay vs market · *median salary ÷ benchmark median × 100* · horizontal bar by role family

**7. Hiring** (needs the ATS)
- Time to fill · *requisition approval → offer accepted, days* · horizontal bar with target
- Time to hire · *application → acceptance, days* · line alongside time to fill
- Cost per hire · *(internal + external costs) ÷ hires* · KPI
- Offer acceptance · *accepted ÷ extended × 100* · line with segment overlay
- Source of hire · *hires by source ÷ total, paired with first-year attrition per source* · grouped bar
- New-hire quality · *first-year retention + first rating; no standard* · bar by cohort
- Funnel · *count per stage; conversion = stage ÷ previous* · sorted horizontal bar, log scale if needed
- Open reqs vs plan · *(filled + open) ÷ planned* · progress bars

**8. Absence & wellbeing**
- Absenteeism · *unplanned absent days ÷ working days × 100* · line with prior-year reference
- PTO utilisation · *days taken ÷ accrued × 100* · horizontal bar by team; low is the problem, invert the colours
- Overtime · *overtime hours ÷ contracted × 100* · heatmap team × month
- Sick leave · *sick days ÷ headcount per month* · bar with 3-month average

**9. Diversity & inclusion**
- Representation by level · *group ÷ level headcount × 100* · stacked 100% bar
- Fairness of pipeline · *group share of hires, promotions, exits vs share of headcount* · grouped bar
- Age distribution · *count per band* · histogram
- Belonging · *favourability on belonging items per group, ≥5 respondents* · bars with org line

**10. Workforce planning & impact** (needs finance data)
- Revenue per employee · *trailing-12-month revenue ÷ average headcount* · line with benchmark
- Labour cost / revenue · *total comp ÷ revenue × 100* · line
- Plan vs actual · *actual ÷ planned per department* · bullet bars
- Attrition forecast · *trend + seasonality + risk model, with an 80% band* · line with projection band
- HR-to-employee ratio · *HR headcount ÷ total* · KPI
- Skills coverage · *at required proficiency ÷ roles requiring the skill × 100* · heatmap team × skill

Every chart gets the same six filters — department, manager, level, tenure, location, employment
type — and a period comparison. If the user can only give one or two files, build blocks 1–4 plus
the unadjusted pay gap from block 6: that's what companies of 30–1000 people actually use, and
what an HRIS plus a performance tool can feed today.

Demographic blocks (9, and the gender cuts in 6) use only explicit, consented demographic columns.
Never infer gender, ethnicity or age from names.

## Finish with

Three sentences: what's in the dashboard, which blocks you skipped and why, and the one export
that would unlock the most next. If the source was a connected tool, offer to re-run this on a
schedule.
