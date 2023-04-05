FROM python
LABEL maintainer = "Colin McAllister - colin.mcallister0723@gmail.com"
USER root
RUN apt-get update && apt-get install -y \
    # curl \
    # wget \
    # apt-transport-https \
    # ca-certificates \
    # software-properties-common \
    git
# RUN apt install python3
COPY requirements.txt .
# RUN python -m ensurepip --upgrade
RUN pip install -r requirements.txt
COPY . .
RUN chmod +x bot.py
CMD ["python3","-u","bot.py"]