FROM python:3.6

# Maintainer
LABEL maintainer="Vmoksha Technologies <devops@vmokshagroup.com>"

#Set the path as /usr/local to install anaconda
ENV PATH /opt/conda/bin:$PATH

#Install Base Packages or dependence softwares of Build
#RUN apt-get -qq update && apt-get -qq -y install curl bzip2 \
#    && curl -sSL https://repo.anaconda.com/archive/Anaconda3-5.2.0-Linux-x86_64.sh -o /tmp/anaconda.sh \
#    && bash /tmp/anaconda.sh -bfp /usr/local \
    #&& rm -rf /tmp/miniconda.sh \
#    && apt-get -qq -y remove curl bzip2 \
#    && apt-get -qq -y autoremove \
#    && apt-get autoclean \
#    && rm -rf /var/lib/apt/lists/* /var/log/dpkg.log \
#    && conda clean --all --yes
# For temporary we are commenting anaconda packages

#Add Python packages
COPY . /usr/app
#set the working directory
WORKDIR /usr/app
# Install the Python PIP program packages from requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
# Run the Python API Server
#CMD [ "python", "./api/api.py" ]
CMD [ "gunicorn", "-b", "0.0.0.0:5000", "api.app" ]