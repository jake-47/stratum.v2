
# Examples

Practical examples of audience targeting with Material design.

## Basic Targeting

Public content that everyone sees with beautiful Material styling.

<!-- audience: internal -->

!!! danger "Internal Only"
    
    This is sensitive internal information with:
    
    - Development secrets
    - Internal processes
    - Confidential data

<!-- /audience -->

## Inline Examples

This is a regular sentence with <!-- audience: partner -->partner-specific API keys and credentials<!-- /audience --> embedded naturally in the text.

## Complex Scenarios

<!-- audience: internal, beta -->

!!! info "Internal & Beta Users"
    
    This content is visible to both internal users and beta testers:
    
    - Early feature previews
    - Testing instructions
    - Debug information

<!-- /audience -->

<!-- audience: !partner -->

!!! warning "Everyone Except Partners"
    
    This content is hidden from partners but visible to everyone else:
    
    - Competitive information
    - Internal pricing
    - Strategy details

<!-- /audience -->

## Material Features Demo

=== "Tab 1"

    Content in first tab.
    
    <!-- audience: internal -->
    With internal-only additions.
    <!-- /audience -->

=== "Tab 2"

    ```python
    def example():
        # Public code
        return "hello"
    ```

=== "Tab 3"

    <!-- audience: partner -->
    Partner-specific tab content only visible to partners.
    <!-- /audience -->

## Code Highlighting

```python title="audience_example.py"
def public_api():
    """This function is documented for everyone."""
    return {"status": "public"}

# audience: internal
def internal_debug():
    """Only internal developers see this.""" 
    return {"debug": True, "secrets": "classified"}
# /audience
```

---

