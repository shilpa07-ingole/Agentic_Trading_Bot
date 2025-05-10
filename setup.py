from setuptools import find_packages,setup

setup(name="Agentic_Trading_System",
      version="0.0.1",
      author="shilpa",
      author_email="shilpa.ingole@gmail.com",
      packages=find_packages(),
      install_requires=['lancedb','langchain','langgraph','tavily-python','polygon'],
      )



