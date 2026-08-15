# AI worker agents

This directory contains portable, platform-neutral agent definitions. Each JSON
file documents an agent's purpose, operating instructions, permissions, and
approval boundaries so that an implementation can map them onto its own tools.

## Available agents

| Agent | Responsibilities |
| --- | --- |
| [Administration / Customer Care](administration-customer-care.json) | Phones, customer inquiries, CRM hygiene, deposits, scheduling, invoicing, review requests, and document control |

## Integration requirements

An agent runner must enforce the declared `access` and `approval_required`
rules outside the model. Treat the definition as policy input, not as a security
boundary. Implementations should authenticate every operator, use least-privilege
tool credentials, retain an audit log, and make approval prompts show the exact
action and payload that will be executed.
