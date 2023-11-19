# Extract and compile third-party dependencies
FROM python:3.10-slim AS deps
COPY src.todos/binary-deps.pex /binary-deps.pex
RUN PEX_TOOLS=1 python3.10 /binary-deps.pex venv --scope=deps --compile /app


# Extract and compile first-party codes
FROM python:3.10-slim AS srcs
COPY src.todos/binary-srcs.pex /binary-srcs.pex
RUN PEX_TOOLS=1 python3.10 /binary-srcs.pex venv --scope=srcs --compile /app

# Setup deploy environment
FROM python:3.10-slim

COPY --from=deps /app /app
COPY --from=srcs /app /app

WORKDIR /app
CMD ./pex
