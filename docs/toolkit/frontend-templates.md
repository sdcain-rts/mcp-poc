# Frontend Templates

The AI Developer Toolkit provides several frontend templates that are pre-configured with AI capabilities and best practices. Each template can be customized and extended to suit your specific requirements.

## Available Templates

### React Template

A modern React application template with AI integration capabilities.

**Features:**
- React 18 with hooks
- TypeScript support
- React Router for navigation
- AI component library for common LLM interactions
- Optional state management with Redux Toolkit
- OpenAI and Anthropic integration examples
- Responsive design with TailwindCSS
- Testing setup with Vitest

**Usage:**
```bash
task frontend:create:react -- my-ai-app
```

### Next.js Template

Server-side rendering with Next.js, perfect for content-heavy AI applications.

**Features:**
- Next.js 14 with App Router
- Server actions for secure API calls
- Built-in streaming responses for LLM outputs
- AI component library
- OpenAI and Anthropic integration examples
- TailwindCSS and Shadcn UI components
- SEO optimizations

**Usage:**
```bash
task frontend:create:nextjs -- my-ai-app
```

### Vue Template

A Vue 3 template with Composition API and TypeScript.

**Features:**
- Vue 3 with Composition API
- TypeScript support
- Vue Router and Pinia for state management
- AI component library for common LLM interactions
- OpenAI and Anthropic integration examples
- Responsive design with TailwindCSS
- Testing setup with Vitest

**Usage:**
```bash
task frontend:create:vue -- my-ai-app
```

### Angular Template

An Angular template for enterprise-grade AI applications.

**Features:**
- Latest Angular version
- TypeScript support
- Angular Material components
- AI service integrations
- RxJS for reactive programming
- OpenAI and Anthropic integration examples
- Testing setup with Jasmine and Karma

**Usage:**
```bash
task frontend:create:angular -- my-ai-app
```

## Customizing Templates

Each template can be customized during creation by providing additional options:

```bash
task frontend:create:react -- my-ai-app --state=redux --styling=tailwind --ai-sdk=openai
```

## Extending Templates

All templates are designed to be extended. You can add your own components, services, and features as needed. 

Check the [Extending Templates](../development-guides/extending-templates.md) guide for more information.