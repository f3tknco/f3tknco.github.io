# Personal homepage redesign — Structured Core, Living Edge

## Intent

Reframe the homepage away from a work-history / technology inventory and toward a higher-level personal identity: someone who looks for structure in complexity, makes relationships and boundaries visible, and remains interested in what can grow from a coherent system.

CASE/CSC/work-specific identity is not public content. Work-derived design exploration may inform the design grammar, but no CASE names, internal architecture, mascots, characters, project stories, private systems, or organization-specific language should appear.

## Core idea

**Structured Core, Living Edge**

The page should feel precise without feeling sterile, expressive without becoming a design portfolio, and personal without becoming autobiographical.

The conceptual pair is:

- **Structured Core** — structure, relationships, boundaries, coherence.
- **Living Edge** — curiosity, evolution, emergence, expression.

A concise verbal expression of the theme is:

> I like finding structure in complexity — then seeing what can grow from it.

## Positioning

The homepage should no longer define the person primarily through a job title or a list of technologies.

Software engineering remains background context, not the identity headline.

The page should communicate a recurring way of seeing and working across different media:

- find structure in complexity;
- prefer relationships over inventories;
- clarify boundaries and responsibilities;
- create enough coherence for things to evolve;
- leave room for exploration and unexpected expression.

## Information architecture

### 1. Hero — identity before occupation

Primary statement:

> I like finding structure in complexity — then seeing what can grow from it.

Supporting copy:

> My background is in software engineering, but I tend to be drawn to relationships, boundaries, and the ways ideas and systems become coherent enough to evolve.

The current “traditional applications → application platforms → platform engineering” strip should be removed from the homepage because it is too close to work-history framing.

### 2. Ways of seeing — four lenses

Replace the technology/domain map with a more abstract but still concrete visual composition built around four recurring lenses:

- **Structure** — What is actually here?
- **Relationships** — How do the pieces affect one another?
- **Boundaries** — Where should responsibility live?
- **Emergence** — What becomes possible once the whole is coherent?

These are not presented as steps, skills, or a maturity model. They should visually behave like parts of one field.

The caption **relationships over inventory** remains, but as a personal principle rather than an engineering-diagram caption.

### 3. Between things — short personal note

Keep the spirit of “The interesting part is usually between things,” but generalize the prose beyond technical domains.

Suggested direction:

> I’m usually less interested in collecting more pieces than in understanding how they fit together. Once the relationships make sense, the system becomes easier to explain, change, and sometimes turn into something unexpected.

This section is where the page can subtly bridge engineering, visual systems, communication, and exploration without naming private work.

### 4. Public edge — footer / closing note

Keep the existing idea that this is not a conventional portfolio.

Suggested direction:

> This is a small public edge of a much larger set of things I explore, build, and think about.

Keep the GitHub link prominent but quiet.

## Visual system

### Base

Retain the warm off-white / graphite foundation because it already carries calmness and precision well.

The current copper/orange accent remains, but its semantic role changes: it becomes a **living signal**, used only where the page is showing connection, change, curiosity, or emergence.

### Grid

Do not use one uniform engineering grid across the whole page.

The grid should be strongest near the structured areas and gradually weaken, break, curve, or dissolve toward the expressive edge of the composition. The page should visually imply that order is creating room for evolution rather than constraining it.

### Geometry

Avoid dashboard cards, floating pills, skill badges, or conventional timeline UI.

Prefer:

- thin structural rules;
- inline SVG paths;
- asymmetric but deliberate placement;
- a small number of nodes with clear relationships;
- branching / secondary marks that suggest possibility rather than data flow;
- generous negative space.

The identity mark may evolve from the current diamond-and-dot into a seed / node / boundary motif, but it should remain abstract and personal rather than resemble a project logo.

### Typography

Keep the contrast between clean sans-serif display type and monospace annotations.

Use monospace for small observations, coordinates, principles, or margin notes — not for large blocks of content.

The page should feel closer to an editorial systems sketch than a developer landing-page template.

## Motion

Motion must be subtle and optional.

Preferred motions:

- one slow pulse or drift along a living signal path;
- a branch or node appearing only after the main structure is visible;
- small opacity / stroke changes on hover or focus.

No particle field, parallax spectacle, large scroll-jacking effect, or continuously busy animation.

Respect `prefers-reduced-motion`.

No animation library is required unless implementation proves CSS/SVG insufficient. For this single page, native CSS and inline SVG are preferred because they provide exact control with no dependency overhead.

## Non-goals

- Do not expose CASE, CSC, internal systems, architecture, project names, mascots, characters, or workplace stories.
- Do not make the page a résumé.
- Do not create a technology badge wall.
- Do not position the user as a professional visual designer.
- Do not make the page look like a CASE-branded derivative.
- Do not add a framework simply to make the implementation look sophisticated.

## Accessibility / implementation boundaries

- Semantic HTML first.
- Inline SVG should have accessible title/description where it carries meaning.
- Text remains readable without motion.
- Responsive behavior must work at desktop and narrow mobile widths.
- Color contrast should remain comfortable on the warm-paper background.
- External dependencies should be zero unless a specific visual behavior clearly justifies one.

## Acceptance criteria

The redesigned homepage succeeds if:

1. a first-time visitor can understand the page without knowing the user’s employer or projects;
2. software engineering is visible as background context, not the page’s organizing principle;
3. the visual language communicates both structure and emergence;
4. the page does not read as a résumé, portfolio template, or workplace brand derivative;
5. `relationships over inventory` feels like a genuine personal principle;
6. the design remains lightweight, responsive, accessible, and coherent as a single-page site.
