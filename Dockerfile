FROM python:3

#copying source
COPY --chown=10:11 ./src/* /src/

#setting the working directory
WORKDIR /src

RUN mkdir ./output
VOLUME /output "c:/output"

RUN echo 'we are running some # of cool things'

#running the Python program
CMD [ "python", "./string_sort.py", "input1.csv" ]