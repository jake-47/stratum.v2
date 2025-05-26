# Stratum
> An elegant multi-audience documentation framework

Stratum is built on [MkDocs](https://www.mkdocs.org/) with the [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) theme. It lets you serve multiple audiences—internal teams, partners, beta users, and the public—from one unified documentation base. Write documentation once, and serve different audiences (internal, partner, beta, public) with surgical precision using conditional comments and frontmatter tags.

|Audience|Can See Content Marked As|
|---|---|
|**Internal**| **everything**: default (public), partner, beta, internal |
|**Partner**|partner content only|
|**Beta**|beta content only|
|**Public**|default content with no `audiences:` frontmatter (i.e. untagged)|

The reason for that logic:
- Internal teams need full visibility to support partners, test beta features, and manage docs.
- Partners and beta users must only see their authorized content.
- Public users should only see untagged general documentation.

To prevent privacy leaks, confusion, and content drift, Stratum uses purpose-built automated builds—each precisely filtered and clearly labeled to ensure the right content reaches the right audience, every time. Instead of duplicating files or running multiple content trees, Stratum uses audience tags and conditional comments to selectively render content at build time. That's its real advantage. Stratum's way of saying: **"We care about who's reading, but we don't want five versions of the truth in ten different places."**

## Core Strengths
- One set of Markdown files, many tailored outputs
- Granular access control per block, section, or page
- Seamless integration with MkDocs Material
- Clean build system that generates audience-specific config files
- Scalable architecture that's easy to onboard and maintain

Stratum is ideal for teams who need clarity, maintainability, and layered access without sacrificing writing simplicity.

## Installation

### 1. Clone or Download
```bash
git clone https://github.com/your-org/stratum.git
cd stratum
```

### 2. Set Up Virtual Environment (Recommended)
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -e .
```

This installs all dependencies listed in `pyproject.toml`, including `mkdocs`, `mkdocs-material`, `mkdocs-macros-plugin`, and the Stratum audience plugin.

### 4. Generate Audience Configs

```bash
python generate_configs.py
```

This creates `mkdocs.public.yml`, `mkdocs.internal.yml`, `mkdocs.partner.yml`, and `mkdocs.beta.yml` based on audience logic.

### 5. Run Local Development Server

Pick the audience config you want to preview:

```bash
mkdocs serve --config-file mkdocs.public.yml    # Public content
mkdocs serve --config-file mkdocs.internal.yml  # Internal view
mkdocs serve --config-file mkdocs.partner.yml   # Partner-only docs
mkdocs serve --config-file mkdocs.beta.yml      # Beta feature set
```

## Usage

### Audience Comments

Use HTML comments to target specific audiences:

```markdown
<!-- audience: internal -->
This content is only visible to internal users.
<!-- /audience -->

<!-- audience: partner -->
Partner-specific information here.
<!-- /audience -->

<!-- audience: beta -->
Beta features and experimental content.
<!-- /audience -->
```

### Inline Targeting

```markdown
This sentence has <!-- audience: internal -->internal notes<!-- /audience --> embedded.
```

### Page-Level Filtering

Use frontmatter to restrict entire pages:

```markdown
---
audiences: internal
---

# Internal-Only Page
This entire page is only visible to internal users.
```

### Negation (Exclusion)

```markdown
<!-- audience: !partner -->
This content is hidden from partners but visible to everyone else.
<!-- /audience -->
```

### Multiple Audiences

```markdown
<!-- audience: internal, beta -->
Both internal users and beta testers can see this.
<!-- /audience -->
```

## Philosophy

At its core, Stratum is committed to **minimal forking, maximum reuse**. Writers work in a unified Markdown corpus, embedding audience-specific content using simple, declarative logic. A developer building a CLI guide and a designer writing integration tips don't need to worry about which file to use—there's only one. The system handles visibility **surgically** at render time.

### One Source. Multiple Perspectives.

Stratum rejects the traditional tradeoff between centralized content and contextual relevance. With Stratum, documentation can serve diverse needs without creating parallel versions. Instead of duplicating files, writers embed conditional logic where necessary and let the build process determine what each audience sees.

This isn't just a technical decision—it's an editorial one. It prevents divergence, reduces maintenance costs, and ensures that updates flow cleanly to every version of the docs.

### Audience Visibility Without Complexity

Each audience—internal, partner, beta, and public—is configured at build time through YAML flags. Writers specify audience context using the `audiences:` field in the frontmatter and embed conditional content with HTML comments like `<!-- audience: internal -->`.

There is no need for non-technical contributors to learn Python or manipulate configuration files. Markdown remains the authoring language. Writers write; the system frames.

### Design Principles

1. **Clarity Through Context**  
   Content is not hidden; it is framed. Readers see badges, styles, and signals that clarify what is meant for them. Relevance is established through framing, not exclusion.

2. **Configuration, Not Duplication**  
   Audience segmentation lives in config files, not in forks. Whether you're serving one audience or five, the documentation structure stays the same.

3. **Progressive Disclosure**  
   Internal users see everything. Partners and beta testers see what's meant for them. The public sees a refined core. No content is duplicated—only visibility changes.

4. **Scalable Without Fragmentation**  
   Adding a new audience is as simple as adding a new build. There's no need to reorganize files or maintain parallel docs. The system scales cleanly as the organization grows.

5. **Friendly to Writers, Scriptable for Developers**  
   Writers work in familiar Markdown. Developers configure builds using Python and YAML. The tooling remains powerful, but never intrusive.

6. **Style Supports Semantics**  
   Audience-specific content is styled with subtle consistency—purple for internal, blue for partners, amber for beta. This visual hierarchy supports clarity, not distraction.

7. **Operational Sustainability**  
   Stratum's architecture is designed for long-term maintainability. Updates are made once. Builds are automated. Docs stay in sync.

## Why MkDocs

MkDocs is a static site generator purpose-built for documentation. Written in Python, it provides a clean, efficient workflow for developers and writers alike. Unlike general-purpose tools like Jekyll or Docusaurus, MkDocs focuses on speed, simplicity, and structure—making it ideal for teams who want documentation that evolves with their code.

### Python-Friendly Workflow

MkDocs integrates naturally into Python ecosystems. With straightforward pip installation and plugin development in Python, it's ideal for teams that already build, test, and deploy in Python. Unlike Jekyll (Ruby) or Docusaurus (React/JavaScript), MkDocs avoids the context switch and offers direct extensibility in the language many developers already use.

### Simplicity Without Sacrifice

You can get started with MkDocs using only Markdown files and a YAML configuration. It offers a smooth learning curve without sacrificing extensibility. Compared to the complexity of Sphinx or the verbosity of Antora, MkDocs gives you productivity out of the box, ideal for small teams or fast-paced projects where results matter more than customization depth.

### Material Theme Advantage

Starting with the Material for MkDocs theme gives teams a powerful head start. It delivers a responsive, visually polished, and production-grade experience that works seamlessly across mobile and desktop. With support for tabbed content, collapsible sections, code highlighting, and styled admonitions, the Material theme dramatically shortens the time to create high-quality technical documentation.

### Fast, Incremental Builds

MkDocs shines in developer experience with near-instant builds, even for large documentation sets. Its incremental build feature ensures that only changed files are rebuilt, which significantly outperforms Jekyll and Docusaurus as documentation grows.

### Plugin Ecosystem Flexibility

MkDocs has a strong, approachable plugin ecosystem. You can add support for diagrams, mathematical expressions, versioning, audience targeting, and more—all through well-maintained plugins. This flexibility exceeds what mdBook offers and avoids the complexity of Sphinx's plugin system.

### Perfect for Reference Documentation

While tools like Antora suit modular enterprise systems and mdBook favors tutorials, MkDocs excels at reference documentation. Its hierarchical navigation, built-in search, and semantic structure make it ideal for API references, product guides, and technical overviews.

### Collaborative-Friendly

With Markdown authoring and git-based workflows, MkDocs enables both developers and writers to contribute seamlessly. Teams avoid the overhead of GitBook's SaaS model or Confluence's licensing and platform constraints. Writers use familiar syntax, developers benefit from CI/CD-ready infrastructure, and no one is locked into a proprietary editor.

## Architecture

Stratum consists of:

- **Audience Plugin**: Processes audience comments and frontmatter
- **Config Generator**: Creates audience-specific MkDocs configurations  
- **Design System**: Professional CSS with audience-aware styling
- **Material Integration**: Clean template overrides and enhanced navigation

The plugin architecture is designed for maintainability and extensibility, following MkDocs plugin conventions while providing powerful audience targeting capabilities.

## Contributing

Contributions are welcome! Please feel free to:

- Report bugs or suggest features via GitHub Issues
- Submit pull requests for improvements
- Share your use cases and feedback
- Improve documentation or examples

## License

MIT License - feel free to use, modify, and distribute as needed.

---

**Stratum**: *An elegant solution for teams who need sophisticated audience targeting without the complexity of maintaining multiple documentation sources.*