__defaults__(all=dict(environment="__local__"))

local_environment(
    name="local_env_macos",
    compatible_platforms=["macos_arm64"],
    fallback_environment="docker",
)

docker_environment(
    name="docker_env_linux",
    platform="linux_arm64",
    image="python:3.10-slim",
)
