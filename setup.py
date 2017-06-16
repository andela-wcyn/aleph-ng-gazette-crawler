from setuptools import setup

setup(
    name='aleph_ng_gazette_crawler',
    entry_points={
        'aleph.crawlers': [
            'NG_gazettes = aleph_ng_gazette_crawler.crawler:Crawler',
        ]
    },
    version='0.2',
    description='Aleph crawler to index Nigerian government gazettes archived at https://s3-eu-west-1.amazonaws.com/cfa-opengazettes-ng/gazettes/',
    url='https://github.com/OpenGazettes/aleph_ng_gazette_crawler',
    author='Code For Africa',
    author_email='info@codeforafrica.org',
    license='MIT',
    packages=["aleph_ng_gazette_crawler"],
    zip_safe=False
)
