__defaults__(all=dict(environment="__local__"))

local_environment(
    name="local_env_macos",
    compatible_platforms=[
        "linux_x86_64", 
        "linux_arm64", 
        "macos_arm64"
    ],
)

docker_environment(
    name="docker_env_linux",
    platform="linux_arm64",
    image="python:3.10-slim",
)
