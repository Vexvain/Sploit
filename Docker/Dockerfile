FROM phocean/msf

COPY "entrypoint.sh" .

RUN apt-get update && \
 	apt-get install -y \
					git \
					python-dev \
					python-pip \
					apache2

RUN chmod +x entrypoint.sh && \
	git clone https://github.com/Vexvain/Sploit.git && \
	pip install -r Sploit/requirements.txt
	
EXPOSE 4444
CMD [ "./entrypoint.sh" ]
