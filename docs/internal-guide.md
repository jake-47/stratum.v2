# Internal Guide

!!! note "Internal Documentation"
    This page demonstrates Stratum's internal content features. Internal users see everything on this page, while public builds exclude internal-only sections.

## Using Stratum for Internal Content

Stratum makes it easy to include team-specific information alongside public documentation. Mark sensitive content as internal, leave everything else public.

### When to Use Internal Sections

Use `<!-- audience: internal -->` tags for:

- Work-in-progress documentation
- Internal processes and procedures  
- Team contact information
- Development notes and TODOs
- Sensitive configuration details

<!-- audience: internal -->
## Internal Development Setup

### Quick Start for New Team Members

```bash
# Clone the project
git clone git@github.com:company/project.git
cd project

# Set up environment
cp .env.example .env.local
# Edit .env.local with your settings

# Install dependencies  
npm install

# Start development server
npm run dev
```

### Internal Tools and Access

**Development Environments:**
- Staging: `https://staging.ourapp.com` 
- Development: `https://dev.ourapp.com`
- Local: `http://localhost:3000`

**Access Requirements:**
- VPN connection required for staging/dev
- GitHub access: Contact @devops for repository access
- Database access: Use staging DB for development

### Team Contacts

| Role | Contact | Notes |
|------|---------|-------|
| DevOps | @jane-ops | For deployment and infrastructure |
| Backend Lead | @john-backend | API and database questions |
| Design System | @sarah-design | Component and styling questions |

## Release Process

### Pre-release Checklist

- [ ] All tests passing in CI
- [ ] Code review completed
- [ ] Documentation updated
- [ ] Staging deployment verified
- [ ] Security review (if needed)

### Deployment Steps

1. **Create release branch**: `git checkout -b release/v1.2.3`
2. **Update version numbers** in `package.json` and `CHANGELOG.md`
3. **Test staging deployment**: Verify everything works
4. **Create pull request** with release notes
5. **Merge to main** after approval
6. **Deploy to production** using GitHub Actions

!!! warning "Important"
    
    Always deploy during low-traffic periods (typically Tuesday-Thursday, 10 AM - 2 PM EST).

### Rollback Procedure

If issues are discovered after deployment:

```bash
# Quick rollback via GitHub Actions
# Go to Actions tab → Latest deployment → Re-run previous successful deployment
```

For database migrations, contact @jane-ops immediately.
<!-- /audience -->

## Public Documentation Guidelines

This section is visible to both internal and external users, demonstrating mixed content.

### Writing Style

- Use clear, concise language
- Include code examples where helpful
- Link to related documentation
- Keep explanations beginner-friendly

<!-- audience: internal -->
**Internal Note**: Remember to review public documentation for any accidental internal references before publishing.
<!-- /audience -->

### Content Organization

Structure documentation with logical hierarchy:

1. **Overview** - What this feature/API does
2. **Quick Start** - Minimal working example  
3. **Detailed Guide** - Complete reference
4. **Examples** - Real-world usage patterns
5. **Troubleshooting** - Common issues and solutions

### Code Examples

Always test code examples before publishing. Include:

- Complete, runnable code snippets
- Expected output or results
- Common variations or alternatives
- Error handling where relevant

<!-- audience: internal -->
## Internal Content Guidelines

### What Should Be Internal

**Always Internal:**
- Team processes and contacts
- Unreleased feature documentation
- Internal tool configurations
- Development environment details
- Security-sensitive information

**Usually Public:**
- API documentation
- User guides and tutorials
- Installation instructions
- Troubleshooting guides
- Concept explanations

### Content Review Process

1. **Draft**: Write in internal sections first
2. **Review**: Team reviews for accuracy and sensitivity
3. **Clean**: Move appropriate content to public sections
4. **Publish**: Deploy public build for external users

### Managing Work-in-Progress

Use internal sections for drafts:

```markdown
<!-- audience: internal -->
## Feature X Documentation [DRAFT]

This feature is in development. Current status:
- [ ] API endpoints defined
- [ ] Basic implementation complete
- [ ] Tests written
- [ ] Documentation review needed

**TODO**: Add examples and troubleshooting section.
<!-- /audience -->
```

Once ready, move content outside the internal tags.
<!-- /audience -->

## Documentation Tools

We use Stratum for multi-audience documentation management:

- **Internal builds**: Include all content for team reference
- **Public builds**: Only verified, external-ready content
- **Single source**: One set of files, multiple outputs

This approach prevents content drift and reduces maintenance overhead while ensuring the right information reaches the right audience.

For questions about documentation process or Stratum usage, <!-- audience: internal -->contact @sarah-docs or<!-- /audience --> check the main documentation.