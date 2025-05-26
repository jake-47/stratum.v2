# Logo & Site Title Customization Guide
*Complete guide for teams using Stratum to customize their brand identity*

## Overview
Stratum uses a **seamless logo system** with design tokens that creates a unified brand phrase while maintaining audience-specific badges. Your logo displays as one cohesive phrase (e.g., "YourBrand Documentation") with optional audience indicators.

## What You Can Customize
- **Brand Name**: Change "Stratum" to your company name  
- **Site Title**: Change "Knowledge Base" to your preferred title  
- **Seamless Phrase**: Both appear as one unified logo phrase  
- **Brand Colors**: Custom colors for light and dark themes  
- **Typography**: Custom fonts for your brand and site title  
- **Audience Badges**: Automatic "(Internal)", "(Partner)", "(Beta)" indicators  
- **Automatic Theming**: Everything adapts to light/dark modes  

## Change Brand Name & Site Title

### 1. Edit the Logo File

1. **Open** `docs/assets/logo.svg` in any text editor
2. **Find** these two text elements:
   ```svg
   <text x="36" y="24" ...>Stratum</text>
   <text x="145" y="24" ...>Knowledge Base</text>
   ```
3. **Replace** with your brand:
   ```svg
   <text x="36" y="24" ...>YourBrand</text>
   <text x="145" y="24" ...>Your Title</text>
   ```
4. **Adjust spacing** for the second text element:
   - **Short brand names** (4-6 chars): Change `x="145"` to `x="120"`
   - **Medium brand names** (7-9 chars): Keep `x="145"`
   - **Long brand names** (10+ chars): Change `x="145"` to `x="170"`

### 2. Update Site Configuration

Edit `mkdocs.yml`:
```yaml
site_name: YourBrand Your Title  # Used for browser tab title and SEO
```

**Important:** The `site_name` is only used for browser tabs and SEO. The actual visible header shows your seamless logo phrase + audience badges.



## Step 2: Customize Brand Colors & Fonts

1. **Open** `docs/assets/styles/extra.css`
2. **Find** the design tokens section (around line 15):
  {% raw %}
        ```css
        :root {
          /* Logo Design Tokens */
          --st-brand-font: "Inter, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif";
          --st-brand-weight: 700;
          --st-title-font: inherit;
          --st-title-weight: 400;
          
          /* Brand Colors */
          --st-brand-color-light: #0d1b0f;
          --st-title-color-light: #333333;
          --st-brand-color-dark: #ffffff;
          --st-title-color-dark: #e0e0e0;
        }
        ```
  {% endraw %}
3. **Customize** these values for your brand:

#### Option A: Quick Brand Templates

**Tech Startup:**
```css
:root {
  --st-brand-font: "SF Pro Display, -apple-system, BlinkMacSystemFont, sans-serif";
  --st-brand-weight: 800;
  --st-brand-color-light: #000000;
  --st-brand-color-dark: #ffffff;
}
```

**Financial Services:**
```css
:root {
  --st-brand-font: "Helvetica Neue, Arial, sans-serif";
  --st-brand-weight: 600;
  --st-brand-color-light: #1a365d;
  --st-brand-color-dark: #63b3ed;
}
```

**Creative Agency:**
```css
:root {
  --st-brand-font: "Poppins, sans-serif";
  --st-brand-weight: 700;
  --st-brand-color-light: #e53e3e;
  --st-brand-color-dark: #feb2b2;
}
```

#### Option B: Create Your Custom Brand

```css
:root {
  /* Your brand font (always include fallbacks!) */
  --st-brand-font: "YourBrandFont, Helvetica, Arial, sans-serif";
  --st-brand-weight: 700;
  
  /* Your brand colors */
  --st-brand-color-light: #your-light-color;  /* Dark color for light theme */
  --st-brand-color-dark: #your-dark-color;    /* Light color for dark theme */
  
  /* Optional: Customize site title separately */
  --st-title-font: inherit;  /* Uses site's main font */
  --st-title-weight: 400;
  --st-title-color-light: #333333;
  --st-title-color-dark: #e0e0e0;
}
```



## Step 3: Test Your Changes

### Preview Locally

```bash
mkdocs serve
```

- Logo phrase: Should appear as one seamless unit (e.g., "YourBrand Documentation")
- No duplication: Should not see separate site title text
- Proper spacing: Brand name and title should look naturally connected
- Theme switching: Test light/dark mode toggle

### **Multi-Audience Testing**

Test all your audience builds to see the badge system:
```bash
mkdocs serve --config-file mkdocs.public.yml     # No badge
mkdocs serve --config-file mkdocs.internal.yml   # (Internal) badge
mkdocs serve --config-file mkdocs.partner.yml    # (Partner) badge
mkdocs serve --config-file mkdocs.beta.yml       # (Beta) badge
```

**Expected Results:**  
{% raw %}
- Public: `[YourBrand Your Title] [Search] [Theme]`
- Internal: `[YourBrand Your Title] (Internal) [Search] [Theme]`
- Partner: `[YourBrand Your Title] (Partner) [Search] [Theme]`
- Beta: `[YourBrand Your Title] (Beta) [Search] [Theme]`
{% endraw %}

## Complete Examples

### **Example 1: TechCorp Documentation**

**Result**: "TechCorp Developer Docs" as seamless phrase + "(Internal)" badge

#### 1. Edit `docs/assets/logo.svg`:
```svg
<text x="36" y="24" ...>TechCorp</text>
<text x="145" y="24" ...>Developer Docs</text>
```

#### 2. Edit `docs/assets/styles/extra.css` (add to design tokens section):
```css
:root {
  --st-brand-font: "SF Pro Display, -apple-system, BlinkMacSystemFont, sans-serif";
  --st-brand-weight: 800;
  --st-brand-color-light: #000000;
  --st-brand-color-dark: #ffffff;
}
```

#### 3. Edit `mkdocs.yml`:
```yaml
site_name: TechCorp Developer Docs  # Browser tab title
```

**Visual Result:**
- **Public**: `[TechCorp Developer Docs] [🔍] [🌙]`
- **Internal**: `[TechCorp Developer Docs] (Internal) [🔍] [🌙]`

### **Example 2: FinanceFlow Knowledge Base**

**Result**: "FinanceFlow Knowledge Base" as seamless phrase + audience badges

#### 1. Edit `docs/assets/logo.svg`:
```svg
<text x="36" y="24" ...>FinanceFlow</text>
<text x="170" y="24" ...>Knowledge Base</text>
```
*(Note: "FinanceFlow" is longer, so we use `x="170"` for proper spacing)*

#### 2. Edit `docs/assets/styles/extra.css`:
```css
:root {
  --st-brand-font: "Helvetica Neue, Arial, sans-serif";
  --st-brand-weight: 600;
  --st-brand-color-light: #1a365d;
  --st-brand-color-dark: #63b3ed;
}
```

#### 3. Edit `mkdocs.yml`:
```yaml
site_name: FinanceFlow Knowledge Base  # Browser tab title
```

**Visual Result:**
- **Public**: `[FinanceFlow Knowledge Base] [🔍] [🌙]`
- **Partner**: `[FinanceFlow Knowledge Base] (Partner) [🔍] [🌙]`



## Font Guidelines

### **Always Include Fallbacks**

❌ **Wrong:**
```css
--st-brand-font: "CustomFont";
```

**Correct:**
```css
--st-brand-font: "CustomFont, Helvetica Neue, Arial, sans-serif";
```

### **Popular Font Stacks**

**Modern/Tech:**
```css
--st-brand-font: "Inter, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif";
```

**Corporate/Professional:**
```css
--st-brand-font: "Helvetica Neue, Arial, sans-serif";
```

**Creative/Friendly:**
```css
--st-brand-font: "Poppins, Nunito, sans-serif";
```

**Enterprise:**
```css
--st-brand-font: "IBM Plex Sans, Helvetica Neue, Arial, sans-serif";
```



## Color Guidelines

### **Contrast Requirements**

Ensure good contrast for accessibility:

**Light theme colors:** Dark colors work best
- `#000000`, `#1a365d`, `#2d3748`
- ❌ `#ffff00`, `#90cdf4`, `#fed7d7`

**Dark theme colors:** Light colors work best
- `#ffffff`, `#f7fafc`, `#e2e8f0`
- ❌ `#1a202c`, `#2d3748`, `#4a5568`

### **Brand Color Examples**

```css
/* Blue Brand */
--st-brand-color-light: #1e40af;  /* Dark blue for light theme */
--st-brand-color-dark: #60a5fa;   /* Light blue for dark theme */

/* Green Brand */
--st-brand-color-light: #059669;  /* Dark green for light theme */
--st-brand-color-dark: #34d399;   /* Light green for dark theme */

/* Purple Brand */
--st-brand-color-light: #7c3aed;  /* Dark purple for light theme */
--st-brand-color-dark: #a78bfa;   /* Light purple for dark theme */
```


## Troubleshooting

### **Logo Not Showing**

1. **Check file path**: Ensure `docs/assets/logo.svg` exists
2. **Check mkdocs.yml**: Verify `logo: assets/logo.svg` is set
3. **Check CSS loading**: Ensure `extra.css` is in `extra_css` list

### **Site Title Still Duplicating**

If you see both your logo phrase AND a separate site title:
{% raw %}
1. **Check template override**: Ensure `docs/overrides/main.html` exists:
   ```html
   {% extends "base.html" %}
   {% block site_name %}
     {% if config.extra.audience_internal %}
       <span class="audience-badge audience-badge--internal">(Internal)</span>
     {% elif config.extra.audience_partner %}
       <span class="audience-badge audience-badge--partner">(Partner)</span>
     {% elif config.extra.audience_beta %}
       <span class="audience-badge audience-badge--beta">(Beta)</span>
     {% endif %}
   {% endblock %}
   ```

2. **Force hide duplicates** by adding to `extra.css`:
   ```css
   .md-header__title {
     font-size: 0 !important;
   }
   .md-header__title .audience-badge {
     font-size: 0.75rem !important;
   }
   ```
{% endraw %}
### **Font Not Changing**

1. **Check design tokens** in `extra.css`:
   ```css
   :root {
     --st-brand-font: "YourFont, fallback, sans-serif";
   }
   ```
2. **Include fallback fonts** after your custom font
3. **Clear browser cache** and reload

### **Audience Badges Not Showing**

1. **Check template file**: `docs/overrides/main.html` must exist
2. **Check config flags**: Ensure audience flags are set in generated configs:
   ```bash
   python generate_configs.py
   mkdocs serve -f mkdocs.internal.yml
   ```
3. **Verify CSS**: Check that badge styles are in `extra.css`

### **Colors Not Working**

1. **Set both light and dark colors**:
   ```css
   :root {
     --st-brand-color-light: #your-light-color;
     --st-brand-color-dark: #your-dark-color;
   }
   ```
2. **Test theme switching** with the theme toggle
3. **Use proper hex codes** (6 characters: `#1a365d`)

### **Spacing Issues**

If your brand name is longer/shorter than "Stratum":

- **Short names (4-6 chars):** Change `x="145"` to `x="120"`
- **Medium names (7-9 chars):** Keep `x="145"`  
- **Long names (10+ chars):** Change `x="145"` to `x="170"`
- **Very long names (12+ chars):** Change `x="145"` to `x="190"`

### **Mobile Issues**

If the logo looks bad on mobile:
1. **Check responsive CSS** in `extra.css`
2. **Test different screen sizes**
3. **Consider shorter titles** for mobile compatibility


## Best Practices

### Do
- Always include font fallbacks
- Test both light and dark themes
- Use high contrast colors
- Keep brand names concise (under 12 characters)
- Test on mobile devices

###  Don't
- Edit SVG files directly for complex changes
- Use fonts without fallbacks
- Use low-contrast colors
- Forget to test dark mode
- Make the logo too wide for mobile