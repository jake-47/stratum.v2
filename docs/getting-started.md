# File: docs/getting-started.md

# Getting Started

Learn how to use Stratum's audience targeting system with Material design.

## Comment Syntax

Use HTML comments to target specific audiences:

```markdown
<!-- audience: internal -->
Internal-only content here
<!-- /audience -->
```

## Advanced Features

<!-- audience: internal -->

!!! tip "Advanced Usage"
    
    ### Negation Syntax
    
    Use `!` to exclude specific audiences:
    
    ```markdown
    <!-- audience: !partner -->
    Everyone except partners sees this
    <!-- /audience -->
    ```
    
    ### Multiple Audiences
    
    Target multiple audiences at once:
    
    ```markdown
    <!-- audience: internal, partner -->
    Both internal and partner users see this
    <!-- /audience -->
    ```

<!-- /audience -->

## Material Integration

Stratum works seamlessly with Material for MkDocs features:

=== "Audience Blocks"

    ```markdown
    <!-- audience: internal -->
    !!! note "Internal Only"
        This is an internal-only admonition block.
    <!-- /audience -->
    ```

=== "Inline Content"

    ```markdown
    This paragraph has <!-- audience: partner -->partner info<!-- /audience --> inline.
    ```

=== "Code Examples"

    ```python
    # This code is visible to everyone
    def public_function():
        return "Hello World"
    
    <!-- audience: internal -->
    # Internal implementation details
    def internal_helper():
        return "Secret sauce"
    <!-- /audience -->
    ```

---

