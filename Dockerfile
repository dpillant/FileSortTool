FROM python:3

ADD ListContentRepository.py /

RUN pip install pystrich

CMD [ "python", "./ListContentRepository.py" ]
