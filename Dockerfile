FROM python:3.9-slim

# NWQBench's pinned dependencies (numpy 1.20, scipy 1.6, qiskit-aqua 0.9, etc.)
# are from 2021. Some of them still build C/C++ extensions from source on
# Linux, and several rely on setup.py using pkg_resources, which requires a
# matching (old) setuptools -- modern setuptools has dropped it. Pinning
# setuptools/pip before installing the rest avoids "No module named
# pkg_resources" failures.
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        gcc \
        g++ \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements-docker.txt ./requirements-docker.txt
RUN pip install --no-cache-dir "pip==21.1.2" "setuptools==57.0.0" "wheel==0.36.2" \
    && pip install --no-cache-dir -r requirements-docker.txt

COPY . .

RUN mkdir -p /output
VOLUME ["/output"]
ENV OUTPUT_DIR=/output

ENTRYPOINT ["python", "generate_benchmarks.py"]
CMD ["--help"]
