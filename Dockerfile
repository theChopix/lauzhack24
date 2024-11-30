# Use the official Neo4j image as the base image
FROM neo4j:5.8-community

# Environment variables
ENV NEO4J_ACCEPT_LICENSE_AGREEMENT=yes \
    NEO4J_AUTH=neo4j/password123 \
    NEO4J_dbms_memory_pagecache_size=512M \
    NEO4J_dbms_memory_heap_initial__size=512M \
    NEO4J_dbms_memory_heap_max__size=1G

# Expose Neo4j ports
EXPOSE 7474 7687 7473

# Default command to run the Neo4j server
CMD ["neo4j"]
