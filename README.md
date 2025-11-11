# Accflo: Git-Native Revenue Recognition for Usage-Based SaaS

## The Problem: Modern SaaS Finance is Fundamentally Broken

The business model for SaaS has irreversibly changed. 85% of software companies now use usage-based pricing (UBP), with 46% operating hybrid models that combine subscriptions, prepaid credits, variable overages, and minimum commitments. This shift has created a systemic compliance crisis.

**The core issue:** Billing systems can invoice but cannot recognize revenue correctly. ERPs can store journal entries but cannot model usage logic or process millions of daily events. ASC 606 requires event-level revenue recognition, but traditional systems operate on monthly summaries, breaking the audit trail.

Finance teams compensate with a "fragile system held together by humans":
- 36% still use spreadsheets for revenue recognition
- Manual reconciliations take weeks each month
- ~70% of finance transformations are failing or moving slower than expected
- Auditors increasingly refuse to rely on spreadsheet-based processes

The result: extended close cycles, revenue errors, audit failures, and a finance function that blocks rather than enables pricing innovation.

## The Solution: Accounting as Code

**Accflo is a programmable, Git-native subledger for usage-based SaaS.** We sit between billing/usage systems and the general ledger, transforming raw events into GAAP-compliant revenue, journal entries, and audit evidence—automatically.

### How It Works

1. **Ingest**: Connect to billing systems (Stripe, Chargebee), usage databases, and contract data via APIs or lightweight connectors (dlt)
2. **Process**: High-performance event engine (Iceberg + DuckDB) handles millions of usage events daily
3. **Apply Logic**: Version-controlled rules codify pricing, allocation, and ASC 606 logic—expressed as testable code, not spreadsheets
4. **Generate**: Produce revenue schedules, journal entries, and reconciliations automatically
5. **Sync**: Push clean journal entries to ERPs (NetSuite, QuickBooks, ERPNext) via API
6. **Audit**: Complete event-to-revenue lineage with Git commit history as the audit trail

### Core Value Propositions

- **Deterministic Accuracy**: GAAP-compliant revenue recognition with unit-tested rules
- **Speed**: Collapse financial close from weeks to days; 30% reduction in close time
- **Auditability**: Full event-to-revenue traceability; move from sampling to 100% verification
- **Flexibility**: New pricing models deploy in days via Git workflows, not months via ERP customization
- **Scalability**: Process millions of events without adding finance headcount

## Why We Win: Accounting-as-Code Discipline

Our competitive moat isn't any single feature—it's applying **software engineering discipline to accounting operations**. Like dbt disrupted analytics by making data transformation version-controlled and testable, Accflo makes revenue recognition programmable and deterministic.

### Competitive Landscape

| Capability | Billing Platforms | Legacy Rev-Rec | Custom Build | Accflo |
|------------|-------------------|----------------|--------------|---------|
| Usage ingestion | ✓ | ✗ | ✓ | ✓ |
| Revenue recognition | ✗ | ✓ | ✓ | ✓ |
| Version control | ✗ | ✗ | Maybe | ✓ |
| Event lineage | ✗ | ✗ | ✗ | ✓ |
| ERP integration | Limited | ✓ | ✓ | ✓ |
| Testing & CI | ✗ | ✗ | Maybe | ✓ |

**Key differentiation:**
- **Maxio/Chargebee**: Excel at billing, lack revenue recognition and GL integration
- **Zuora RevPro**: Handles rev-rec but rigid (config-based, not code), expensive, built for legacy subscriptions
- **NetSuite**: Provides GL but can't model usage events; ARM module designed for simple subscriptions
- **Custom SQL pipelines**: Flexible but brittle, undocumented, and lack financial controls (SOX nightmare)

Accflo is the first platform combining usage event processing, GAAP-compliant revenue recognition, Git-native workflows, and direct ERP integration.

## Why Now: Technology and Market Convergence

**Technology enablers:**
- Modern data infrastructure (columnar databases, cloud warehouses) makes processing millions of events feasible
- dbt democratized "transformation as code"; analytics engineers now embedded in finance orgs
- Git workflows ubiquitous; teams expect version control and CI/CD
- LLMs reducing friction in code generation and rule authoring

**Market dynamics:**
- Usage-based pricing growing faster than seat-based; customers demand consumption-aligned models
- CFOs own automation budgets and view it as competitive advantage
- Finance transformation failures create urgency for new approaches
- Composable ERP trend (Gartner: 60% of finance orgs seeking composable apps) needs intelligent middleware

## Market Opportunity

**Core ICP:** Usage-based SaaS companies with >$5M ARR, hybrid pricing models, multiple revenue streams, and technical finance teams.

**Market size:** Thousands of qualifying companies globally (15,000+ funded SaaS companies in US alone; 20-30% fit profile). As usage-based pricing expands downmarket, TAM grows.

**Unit economics:** Enterprise software pricing with usage-based expansion; customers see ROI in reduced close time, eliminated audit risk, and freed finance capacity.

## Strategic Vision: The Financial Graph

Accflo becomes the **system of record for revenue** across the entire order-to-cash lifecycle. Our vision:

- **Contracts = Code**: Programmatically readable agreements drive downstream logic
- **Pricing = Code**: All pricing rules version-controlled and testable
- **Revenue = Deterministic**: Every dollar traceable from event to financial statement
- **Compliance = Automated**: Deterministic tasks (most compliance) codified and tested proactively

We're building the composable accounting platform that enables the next 20 years of SaaS business models—where finance moves from reactive bottleneck to strategic enabler.

## The Path Forward

Accflo represents a paradigm shift: **accounting is now a software discipline**. The consumption economy demands data engineering rigor applied to financial compliance. Spreadsheets and monolithic ERPs cannot scale. 

We provide the bridge: Git-native workflows, event-driven architecture, deterministic compliance, and complete auditability. Finance finally gets the modern, programmable infrastructure it needs to operate at the speed of the business.

**The future of finance is code. We're building the platform that makes it possible.**
