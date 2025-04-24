# Database Management

The AI Developer Toolkit provides robust database management capabilities with a focus on version control and migration management through Liquibase. This allows you to track, version, and deploy database changes reliably across environments.

## Database Templates

The toolkit includes ready-to-use database templates that can be deployed with Docker Compose:

### PostgreSQL

Full-featured relational database with JSON support and vector extensions.

**Features:**
- Ready-to-use Docker Compose configuration
- pgvector extension pre-installed for vector embeddings
- Optimized configuration for AI workloads
- Connection examples for all backend templates

**Usage:**
```bash
task db:create:postgres -- my-project
```

### MongoDB

Document database with vector search capabilities.

**Features:**
- Ready-to-use Docker Compose configuration
- Vector search capabilities
- Atlas compatibility
- Connection examples for all backend templates

**Usage:**
```bash
task db:create:mongodb -- my-project
```

### Redis

In-memory database for caching and vector search.

**Features:**
- Ready-to-use Docker Compose configuration
- RedisJSON and RediSearch modules
- Vector similarity search support
- Connection examples for all backend templates

**Usage:**
```bash
task db:create:redis -- my-project
```

## Liquibase Integration

The toolkit provides comprehensive Liquibase integration for database schema management:

### Liquibase Templates

Pre-configured Liquibase templates for common AI database patterns:

- User authentication and management
- Embedding storage with vector capabilities
- Conversation history tracking
- Document management
- Fine-tuning dataset management

### Getting Started with Liquibase

1. **Initialize Liquibase**:
   ```bash
   task db:liquibase:init -- my-project
   ```

2. **Create a new migration**:
   ```bash
   task db:liquibase:new -- my-project "Add embedding table"
   ```

3. **Apply migrations**:
   ```bash
   task db:liquibase:update -- my-project
   ```

4. **Roll back migrations**:
   ```bash
   task db:liquibase:rollback -- my-project 1
   ```

### Liquibase Folder Structure

The generated Liquibase structure follows best practices:

```
my-project/
├── database/
│   ├── changelog/
│   │   ├── db.changelog-master.xml
│   │   ├── db.changelog-1.0.xml
│   │   └── ...
│   ├── liquibase.properties
│   └── scripts/
│       └── ...
```

## Common Database Patterns for AI Applications

The toolkit includes documentation and templates for common AI database patterns:

1. **Vector Storage**: Storing and querying vector embeddings
2. **Conversation Management**: Tracking multi-turn conversations
3. **Tool Usage Logging**: Auditing AI tool calls
4. **Content Management**: Managing training data and documents
5. **User Feedback**: Storing user feedback for model improvement

## Database Tasks

The toolkit provides several tasks to help manage your databases:

```bash
# Start all database services
task db:start

# Stop all database services
task db:stop

# View database logs
task db:logs

# Connect to specific database
task db:connect -- postgres
```

For more detailed information about database management and Liquibase integration, see the [Database Migrations Guide](../user-guides/database-migrations.md).