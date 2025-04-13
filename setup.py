from setuptools import setup, find_packages

setup(
    name='asgardeo_agent_identity_sdk',
    version='0.1.0',
    description='Build seamless identity-aware integrations for LLM agents',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='WSO2',
    author_email='asgardeo-help@wso2.com',
    url='https://github.com/wso2/agent-identity-sdk',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.7',
    install_requires=[],
)
