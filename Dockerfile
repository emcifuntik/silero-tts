FROM archlinux:base
WORKDIR /out
ENV PYTHONUNBUFFERED=1
RUN pacman -Sy
RUN pacman -S --noconfirm python3
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools
RUN pip install -q torchaudio omegaconf torch ipython
RUN pip install -q numpy
COPY init.sh /init.sh
COPY python /python
ENTRYPOINT ["/init.sh"]