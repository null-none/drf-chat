from distutils.core import setup

setup(
    name="drf-chat",
    packages=[
        "drf_chat",
        "drf_chat/migrations",
    ],
    version="1.0.0",
    description="",
    author="Kalinin Mitko",
    author_email="kalinin.mitko@gmail.com",
    url="https://github.com/null-none/drf-chat",
    keywords=[],
    classifiers=[],
    install_requires=[
        "channels",
        "redis",
        "channels-redis"
    ],
)
