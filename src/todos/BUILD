python_sources()

pex_binary(
    name="binary-deps",
    entry_point="main.py",
    layout="packed",
    include_sources=False,
    include_tools=True,
    environment="docker_linux_arm64",
)

pex_binary(
    name="binary-srcs",
    entry_point="main.py",
    layout="packed",
    include_requirements=False,
    include_tools=True,
    environment="docker_linux_arm64",
)

docker_image(
    name="my-little-todo-app",
    dependencies=[":binary-deps", ":binary-srcs"],
    image_tags=["{build_args.GIT_COMMIT}"],
    image_labels={"app": "{build_args.APP}", "environment": "{build_args.ENVIRONMENT}"},
    source="Dockerfile",
)
