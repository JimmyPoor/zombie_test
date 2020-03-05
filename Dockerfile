FROM centos/python-36-centos7
ENV PATH /usr/local/bin:$PATH
ADD . /code
WORKDIR /code
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple  requests
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple  locustio
EXPOSE 8089
#ENV HOST 0
WORKDIR /code/performance
CMD locust --host=http://192.168.1.2  -f performance_child_info.py

#CMD ["dir"]