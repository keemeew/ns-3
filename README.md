# Advanced TCP in ns-3 (CUBIC and DCTCP)
### Introduction
2021년 2월 15일~16일에 진행되는 한국통신학회 주최 "ns-3를 이용한 네트워크 시뮬레이션 기초" 단기 강좌 중
Session 9. Advanced TCP in ns-3 을 진행하기 위한 코드

## Instructions for CUBIC:
Note: Implemented on Ubuntu 16.04 Xenial Xerus (amd64), Feb 2021.

1. ns-3.27 설치

```bash
git clone https://gitlab.com/nsnam/bake.git
cd bake
export BAKE_HOME=`pwd`
export PATH=$PATH:$BAKE_HOME:$BAKE_HOME/build/bin
export PYTHONPATH=$PYTHONPATH:$BAKE_HOME:$BAKE_HOME/build/lib
./bake.py configure -e ns-3.27
./bake.py check
./bake.py download
./bake.py build
cd source/ns-3.27
./waf configure
./waf build
```
※만약 ./bake.py check 시에 비어있는 dependency가 있다면 먼저 설치 한 후 이후 단계를 진행

2. CUBIC 실행코드 다운로드 및 배치
```bash
# home directory로
cd ..
cd ..
cd ..

# CUBIC 실행코드 다운로드
git clone https://github.com/keemeew/ns-3

# CUBIC 실행을 위한 실행코드 배치
cd ns-3/cubic
cp tcp-cubic.cc ~/bake/source/ns-3.27/src/internet/model
cp tcp-cubic.h ~/bake/source/ns-3.27/src/internet/model
cp cubic-test.cc ~/bake/source/ns-3.27/scratch
cp newreno-test.cc ~/bake/source/ns-3.27/scratch
cp wscript ~/bake/source/ns-3.27/src/internet
cp graph_converge.py ~/bake/source/ns-3.27
```

3. 코드 실행
```bash
# home directory로
cd ..
cd ..

# CUBIC과 NEWRENO 코드 실행
cd bake/source/ns-3.27
./waf --run scratch/cubic-test
./waf --run scratch/newreno-test
```

4. 코드 실행 결과 그래프 출력
```bash
gnuplot
load ‘cubic-cwnd.log’
load ‘cubic-ssthresh.log’
load ‘newreno-cwnd.log’
load ‘newreno-ssthresh.log’
```
※만약 gnuplot이 깔려있지 않은 경우 apt-get install gnuplot 를 입력하여 설치 

5. (선택) CUBIC과 NEWRENO 그래프 동시 출력
```bash
python graph_converge.py
gnuplot
load ‘cwnd_compare’
load ‘ssthresh_compare’
```

## Instructions for DCTCP:
Note: Implemented on Ubuntu 16.04 Xenial Xerus (amd64), Feb 2021.

1. DCTCP 실행코드 다운로드 및 배치
```bash
# DCTCP 실행을 위한 ns-3 공식 library 다운로드
git clone https://gitlab.com/nsnam/ns-3-dev

# CUBIC 실행코드 다운로드
git clone https://github.com/keemeew/ns-3

# DCTCP 실행을 위한 실행코드 배치
cd ns-3/dctcp
cp tcp-dctcp.cc ~/ns-3-dev/src/internet/model
cp tcp-dctcp.h ~/ns-3-dev/src/internet/model
cp dctcp-example.cc ~/ns-3-dev/scratch
cp queue_length.py ~/ns-3-dev
```

2. 코드 실행
```bash
cd ..
cd ns-3-dev
./waf configure
./waf build
./waf --run dctcp-example
```


3. 코드 실행 결과 확인
```bash
cat dctcp-example-fairness.dat
cat dctcp-example-t1-length.dat
cat dctcp-example-t2-length.dat
cat dctcp-example-s1-r1-throughput.dat
cat dctcp-example-s2-r2-throughput.dat
cat dctcp-example-s3-r1-throughput.dat
```
__dctcp-example-fairness.dat__: S1-R1, S2-R2, S3-R1 간의 average throughput과 각 sender 간의 fairness<br/> 
__dctcp-example-tx-length.dat__: 스위치의 queue 사이즈<br/>
__dctcp-example-sx-rx-throughput.dat__: 각 sender의 시간 별 throughput

4. (선택) Queue length 그래프 출력
```bash
python queue_length.py
```
- __출력 메세지__<br/> 
T1의 queue length(pkts)<br/>
T2의 queue length(pkts)<br/>
T1의 queue length(us)<br/>
T2의 queue length(us)<br/>

- __Queue length 비교 그래프__<br/> 
'qlen_pkts.png'와 'qlen_us.png' 생성
