# Stratum
> Clean, author-friendly documentation with smart audience targeting

Stratum is built on [MkDocs](https://www.mkdocs.org/) with the [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) theme. It helps you manage internal and external documentation cleanly from one Markdown codebase—without the complexity of maintaining multiple documentation sources.

**Most teams need just two audiences**: internal (for drafts, processes, unreleased content) and public (for everything else). Stratum defaults to this simple workflow while optionally supporting advanced audience segmentation when your team controls deployment.

## Quick Start: Simple Workflow

### Default Audience Logic

|Audience|Sees|Use When|
|---|---|---|
|**Internal**|Everything (drafts, processes, unreleased content)|Team collaboration, work-in-progress|
|**Public**|Default content with no audience tags|External-facing documentation|

This covers 90% of real-world documentation needs, especially for teams working within engineering-controlled environments where audience access is handled by application logic, not build artifacts.

### When to Use Advanced Audiences

Enable `partner` and `beta` audiences only when:
- **Your docs team controls deployment** and access logic
- You need to **publish separate documentation artifacts**
- You have **dedicated partner portals** or customer-facing documentation
- Your documentation workflow is **independent from engineering** environments

If engineering handles audience access through authentication, environments, or application logic, stick with the simple internal/public workflow.

## Installation

### 1. Quick Setup
```bash
# Create project
mkdir my-docs && cd my-docs

# Set up environment
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install Stratum
git clone https://github.com/your-org/stratum.git .
pip install -e .
```

### 2. Generate Configs
```bash
# Creates audience-specific MkDocs configurations
python generate_configs.py
```

### 3. Start Writing
```bash
# Public documentation (default)
mkdocs serve --config-file mkdocs.public.yml

# Internal view (shows everything including internal content)
mkdocs serve --config-file mkdocs.internal.yml
```

## Usage

### Simple Workflow (Recommended)

**Default**: Write normal Markdown. Content is public by default.

**Internal content**: Mark sensitive content for internal teams only:

```markdown
<!-- audience: internal -->
## Internal Process Notes

- API keys are stored in 1Password
- Deploy using the staging environment first
- Contact @devops for production access
<!-- /audience -->
```

**Inline internal notes**:
```markdown
The API endpoint is `/api/v1/users` <!-- audience: internal -->(rate limited to 1000/hour)<!-- /audience -->.
```

That's it. No complex audience logic needed.

### Advanced Workflow (When You Control Deployment)

If your team publishes separate documentation artifacts, you can enable advanced audiences:

**Page-level targeting**:
```markdown
---
audiences: partner
---

# Partner Integration Guide
This entire page is only visible in partner builds.
```

**Multi-audience content**:
```markdown
<!-- audience: partner, beta -->
This section is visible to both partners and beta users.
<!-- /audience -->
```

**Exclusion logic**:
```markdown
<!-- audience: !beta -->
This content is hidden from beta users but visible to everyone else.
<!-- /audience -->
```

**Available configurations**:
```bash
mkdocs serve --config-file mkdocs.public.yml    # Public content only
mkdocs serve --config-file mkdocs.internal.yml  # Everything (internal view)
mkdocs serve --config-file mkdocs.partner.yml   # Partner-specific builds
mkdocs serve --config-file mkdocs.beta.yml      # Beta user documentation
```

## Philosophy

### Simplicity First, Complexity When Needed

Stratum follows the **80/20 rule**: the simple internal/public workflow covers 90% of documentation needs. Advanced audience features are available when genuinely needed, but they don't complicate the default experience.

**Default mindset**: Mark internal content as internal, leave everything else public. Let engineering handle access control.

**Advanced mindset**: When your docs team controls deployment, use targeted builds for different stakeholder groups.

### Documentation Should Follow Deployment Reality

Most documentation teams work within engineering-controlled environments where:
- Audience gating happens at the infrastructure level
- Documentation follows code via cherry-pick, JIRA, or CI processes  
- Partner and beta access is managed through authentication systems
- Complex audience logic creates unnecessary overhead

Stratum respects this reality by defaulting to the simple workflow while supporting advanced use cases when teams actually control audience access.

### One Source, Multiple Perspectives

Instead of maintaining separate documentation repositories, Stratum uses conditional logic to serve different audiences from unified content. This prevents divergence, reduces maintenance costs, and ensures updates flow cleanly to every version.

Writers focus on content quality, not audience complexity. The system handles visibility surgically at build time.

### Design Principles

1. **Default to Public**  
   Unless marked otherwise, content should be accessible to external users. This prevents accidental information hiding and encourages clear, helpful documentation.

2. **Internal When Necessary**  
   Mark content as internal only when it truly needs to stay within the organization—processes, credentials, unreleased features, or work-in-progress.

3. **Advanced Audiences When You Control Access**  
   Use partner/beta builds only when your team publishes separate documentation artifacts and controls who sees what.

4. **Configuration Over Duplication**  
   Audience logic lives in build configuration, not in content forks. Adding new audiences doesn't require reorganizing files or maintaining parallel documentation.

5. **Author-Friendly Complexity**  
   Complex features should be opt-in. Writers shouldn't need to understand advanced audience logic unless their workflow requires it.

6. **Visual Clarity**  
   Audience-specific content gets subtle styling—badges and highlighting that clarify context without creating distraction.

## Why MkDocs + Material

**MkDocs** provides a clean, Python-friendly workflow with fast builds and excellent developer experience. Unlike Jekyll (Ruby) or Docusaurus (JavaScript), it integrates naturally into Python ecosystems.

**Material for MkDocs** delivers production-grade design out of the box—responsive layout, excellent mobile experience, comprehensive theming, and extensive customization options. Teams get professional results without design overhead.

**Together**, they create an ideal foundation for technical documentation that scales from small teams to enterprise deployments.

## Architecture

Stratum consists of:

- **Audience Plugin**: Processes audience comments and frontmatter with minimal overhead
- **Config Generator**: Creates audience-specific MkDocs configurations based on simple flags
- **Design System**: Professional CSS with subtle audience-aware styling  
- **Material Integration**: Clean template overrides and enhanced navigation

The plugin architecture follows MkDocs conventions while providing powerful targeting capabilities that don't interfere with the writing experience.

## Configuration Options

### Simple Configuration (Default)
```yaml
# mkdocs.yml - covers most teams
plugins:
  - stratum-audience  # Auto-detects internal/public workflow

extra:
  audience_internal: false  # Set to true for internal builds
```

### Advanced Configuration (When Needed)
```yaml
# mkdocs.yml - for teams that control deployment
plugins:
  - stratum-audience:
      audiences: [internal, partner, beta]
      auto_labels: true
      label_style: badge

extra:
  audience_internal: false
  audience_partner: false
  audience_beta: false
```

## Decision Framework

**Use Simple Workflow When**:
- Documentation is closely tied to code development
- Engineering controls deployment and access
- You want minimal maintenance overhead
- Team values writing simplicity

**Use Advanced Workflow When**:
- Your docs team controls publishing
- You need separate stakeholder portals
- You publish independent documentation artifacts
- You have complex partner/customer relationships

**Consider Alternatives When**:
- You need real-time collaborative editing (use Notion, Confluence)
- Content is primarily marketing-focused (use marketing platforms)
- You require highly interactive documentation (use purpose-built tools)

## Contributing

Contributions welcome! Please:

- Report bugs or suggest features via GitHub Issues
- Submit pull requests for improvements
- Share your use cases and feedback
- Help improve documentation and examples

Focus areas:
- Simplifying the default workflow
- Improving advanced audience features
- Better integration with CI/CD pipelines
- Enhanced Material theme customization

## License

MIT License - use, modify, and distribute freely.

---

**Stratum**: Clean documentation that scales from simple internal/external separation to sophisticated multi-audience publishing—without sacrificing writing simplicity.