## 인터페이스 설계

### 시스템 인터페이스 요구사항 분석

1. 시스템 인터페이스 요구사항 구성
   - 시스템 인터페이스 : 독립적인 시스템끼리 연동, 상호작용을 위한 접속 방법, 규칙
   - 이러한 시스템 인터페이스 명세서에는 인터페이스 이름, 연계 대상 시스템, 연계 범위 및 내용, 연계 방식, 송신 데이터, 인터페이스 주기, 기타 고려사항 등이 포함되어야 한다.
2. 시스템 인터페이스 요구사항 분석
   - 요구사항 분석은 기능적 요구사항, 비기능적 요구사항으로 분류하고 조직하여 명세를 구체화하고 이를 이해관계자에게 전달하는 일련의 과정이다.
   - 요구사항 분석은 소프트웨어 요구사항 분석 기법을 적절히 이용한다.
   - 요구사항 분석 시 누락된 요구사항이나 제한조건을 추가한다.
   - 우선순위를 부가한다.
3. 시스템 인터페이스 요구사항 분석 절차
   - 소프트웨어 요구사항 목록에서 시스템 인터페이스 관련 요구사항을 선별하여 별도로 시스템 인터페이스 요구사항 목록을 만든다.
   - 시스템 인터페이스와 관련된 요구사항 및 아키텍처 정의서, 현행 시스템의 대.내외 연계 시스템 현황 자료 등 시스템 인터페이스 요구사항과 관련된 자료를 준비한다.
   - 시스템 인터페이스에 대한 요구사항 명세서를 확인하여 기능적인 요구사항과 비 기능적인 요구사항으로 분류한다.
   - 시스템 인터페이스 요구사항 명세서와 시스템 인터페이스 요구사항 목록 및 기타 관련 자료들을 비교하여 요구사항을 분석하고 내용을 추가하거나 수정한다.
   - 추가 수정한 시스템 인터페이스 요구사항 명세서와 시스템 인터페이스 요구사항 목록을 관련 이해 관계자에게 전달한다.

### 인터페이스 요구사항 검증

1. 요구사항 검증(Requirements Verification)
   - 요구사항 검증은 인터페이스의 설계 및 구현 전에 사용자들의 요구사항이 요구사항 명세서에 정확하고 완전하게 기술되었는지 검토하고 개발 범위의 기준인 베이스라인을 설정하는 것이다.
   - 후에 많은 비용이 수정 및 보완에 들 수도 있기 떼문에 중요한 과정이다.
2. 인터페이스 요구사항 검토 계획 수립
   - 프로젝트 이해관계자들이 프로젝트 품질 관리 계획을 참조하여 인터페이스 요구사항 검토 계획을 수립한다.
3. 인터페이스 요구사항 검토 및 오류 수정
   - 인터페이스 요구사항 검토는 검토 체크리스트의 항목에 따라 인터페이스 요구사항 명세서를 검토하는 것이다.
4. 인터페이스 요구사항 베이스라인 설정
   - 인터페이스 요구사항 검토를 통해 검증된 인터페이스 요구사항은 프로젝트 관리자와 주요 의사 결정자에게 공시적으로 승인 받는다.
   - 소프트웨어 설계및 구현을 위해 요구사항명세서의 베이스라인을 설정한다.
5. 요구사항 검증 방법
   - 인터페이스 요구사항 검증은 다음과 같은 검증 방법을 적절하게 이용한다.
   - 요구사항 검토, 프로토타이핑, 테스트 설계, CASE 도구 활용
6. 인터페이스 요구사항 검증의 중요 항목
   - 완정성 : 사용자의 모든 요구사항이 누락되지 않고 완전하게 반영되어 있는가 ?
   - 일관성 : 요구사항이 모순되거나 충돌되는 점 없이 일관성을 유지하고 있는가?
   - 명확성 : 모든 참여자가 요구사항을 명확히 이해할 수 있는가 ?
   - 기능성 : 오구사항이 어떻게 보다 무엇을에 중점을 두고 있는가 ?
   - 검증 가능성 : 요구사항이 사용자의 요구를 모두 만족하고, 개발된 소프트웨어가 사용자의 요구 내용과 일치하는지를 검증할 수 있는가 ?
   - 추적 가능성 : 요구사항 명세서와 설계서를 추적할 수 있는가 ?
   - 변경 용이서 : 요구사항 명세서의 변경이 쉽도록 작성 되었는가 ?

### 인터페이스 시스템 식별

1. 개발 시스템 식별
2. 내외부 시스템 식별
3. 내외부 시스템 환경 및 관리 주체 식별
4. 내외부 시스템 네트워크 연결 정보 식별
5. 인터페이스 식별
6. 인터페이스 시스템 식별

### 송수신 데이터 식별

1. 식별 대상 데이터
2. 정보 흐름 식별
3. 송수신 데이터 식별

### 인터페이스 방법 명세화

1. 인터페이스 방법 명세화의 개념
   - 인터페이스 방법 명세화는 내외부 시스템이 연계하여 작동할 때 인터페이스별 송 수신 방법, 송 수신데이터 오류 식별 및 처리 방안에 대한 내용을 문서로 명확하게 정리하는 것이다.
   - 인터페이스별로 송수신 방법을 명세화하기 위해서는 시스템 연계 기술, 인터페이스 통신 유형, 처리 유형, 발생 주기 등에 대한 정보가 필요하다.
2. 시스템 연계 기술
   - 시스템 연계기술은 개발할 시스템과 내외부 시스템을 연계할 때 사용되는 기술을 의미한다.
   - 주요 시스템 연계 기술에는 아래와 같은 것들이 있다.
   - DB Link : DB에서 제공하는 DB Link 객채를 이용하는 방식이다.
   - API/Open API : 송신 시스템의 데이터베이스에서 데이터를 읽어와 제공하는 애플리케이션 프로그래밍 인터페이스 프로그램이다.
   - 연계 솔루션 : EAI 서버와 송수신 시스템에 설치되는 클라이언트를 이용하는 방식이다.
   - SOCKET : 서버는 통신을 위한 소켓을 생성하여 포트를 할당하고 클라이언트의 통신 요청시 클라이언트와 연결하여 통신하는 네트워크 기술이다.
   - Web Service : 웹 서비스에서 WSDL과 UDDI SOAP 프로토콜을 이용하여 연계하는 서비스이다.
3. 인터페이스 통신 유형
   - 인터페이스 통신 유형은 개발항 시스템과 내외부 시스템간 데이터를 송수신하는 형태를 의미한다.
   - 단방향 : 시스템에서 거래를 요청만 하고 응답이 없는 방식이다.
   - 동기 : 시스템에서 거래를 요청하고 응답이 올 때까지 대기하는 방식이다.
   - 비동기 : 시스템에서 거래를 요청하고 다른 작업을 수행하다 응답이 오면 처리하는 방식
4. 인터페이스 처리 유형
   - 인터페이스 처리 유형은 송수신 데이터를 어떤 형태로 처리할 것인지에 대한 방식을 의미한다.
   - 실시간 방식 : 사용자가 요청한 내용을 바로 처리해야 할 때 사용하는 방식이다.
   - 지연 처리 방식 : 데이터를 매건 단위로 처리할 경우 비용이 많이 발생할 때 사용하는 방식이다.
   - 배치 방식 : 대량의 데이터를 처리할 때 사용하는 방식이다.
5. 인터페이스 발생 주기
   - 인터페이스 발생 주기는 개발할 시스템과 내외부 시스템 간 송수신 데이터가 전송되어 인터페이스가 사용되는 주기를 의마한다.
6. 송수신 방법 명세화
   - 송수신방법 명세화는 내외부 인터페이스 목록에 있는 각각의 인터페이스에 대해 연계 방식, 통신 및 처리 유형, 발생 주기 등의 송수신 방법을 정의하고 명세를 작성하는 것이다.
7. 송수신 데이터 명세화
   - 송수신 데이터 명세화는 내외부 인터페이스 목록에 있는 각각의 인터펭스에 대해 인터페이스, 시 필요한 송수신 데이터에 대한 명세를 작성하는 것이다.
8. 오류 식별 및 처리 방안 명세화
   - 오류 식별 및 처리방안 명세화는 내 외부 인터페이스 목록에 있는 각각의 인터페이스에 대해 인터페이스 시 발생할 수 있는 오류를 식별하고 오류 처리 방안에 대한 명세를 작성하는 것이다.

### 시스템 인터페이스 설계서 작성

1. 시스템 인터페이스 설계서의 개요
   - 시스템 인터페이스 설계서는 시스템의 인터페이스 현황을 확인하기 위해, 시스템이 갖는 인터페이스 목록과 각 인터페이스의 상세 데이터 명세를 정의한 문서이다.
2. 시스템 인터페이스 목록 작성
   - 시스템 인터페이스 목록은 업무 시스템과 내외부 시스템 간 데이터를 주고받는 경우에 사용하는 인터페이스에 대해 기술한 것이다.
3. 시스템 인터페이스 정의서 작성
   - 시스템 인터페이스 정의서는 인터페이스별로 시스템 간의 연게를 위해 필요한 데이터 항목 및 구현 요건등을 기술하는 것이다.

### 미들웨어(MiddleWare) 솔루션 명세

1. 미들웨어의 개념 및 종류
   - 미들웨어는 미들과 소프트웨어의 합성어로 운영체제와 해당 운영체제에서 실행되는 응용 프로그램 사이에서 운영체제가 제공하는 서비스 이외에 추가적인 서비스를 제공하는 소프트웨어이다.
   - 미들웨어는 표준화된 인터페이스를 제공함으로써 시스템간의 데이터 교환에 일관성을 보장한다.
   - 미들웨어는 통신 제공 방법이나 기능에 따라 DB, RPC, MOM, TP-Monitor, ORB, WAS 등으로 구분된다.
2. DataBase
   - DB는 데이터베이스 벤더에서 제공하는 클라이언트에서 원격의 데이터베이스와 연결하기 위한 미들웨어이다.
   - 디비를 사용하여 시스템을 구축하는 경우 보동 2-Tier 아케텍처라고 한다.
   - 대표적인 DB의 종류에는 마이크로소프트의 ODBC, 볼랜드의 IDAPI 오라클의 GLUE 등이 있다.
3. RPC (Remote Procudure Call)
   - 원격 프로시저 호출은 응용 프로그램의 프로시저를 사용하여 원격 프로시저를 마치 로컬 프로시저처럼 호출하는 방식의 미들웨어이다.
4. Message Oriented Middleware
   - MOM은 메시지 기반의 비동기형 메시지를 전달하는 방식의 미들웨어이다.
   - 온라인 업무보다는 이기종 분산 데이터 시스템의 데이터 동기를 위해 많이 사용된다.
5. Transaction Processing Monitor
   - TP-Monitor는 항공기나 철도 예약 업무 등과 같은 온라인 트랜잭션 업무에서 트랜잭션을 처리 및 감시하는 미들웨어이다.
   - 사용자 수가 증가해도 빠른 응답 속도를 유지해야 하는 업무에 주로 사용된다.
6. ORB(Object Request Broker)
   - 객체 요청 브로커는 객체지향 미들웨어로 코바 표준 스펙을 구현한 미들웨어이다.
7. WAS(Web Application Server)
   - 앱 어플리케이션 서버는 정적인 콘텐츠를 처리하는 웹 서버와 달리 사용자의 요구에 따라 변하는 동적인 콘텐츠를 처리하기 위해 사용되는 미들웨어이다.
8. 미들웨어 솔루션 식별
   - 미들웨어 솔루션 식별은 개발 및 운영 환경에 사용될 미들웨어 솔루션을 확인하고 목록을 작성하는 것이다.
   - 소프트웨어 아키텍처에서 정의한 아키텍처 구성 정보와 프로젝트에서 구매가 진행 중이거나 구매 예정인 소프트웨어 내역을 확인하여 개발 및 운영 환경에서 사용될 미들웨어 솔루션을 식별한다.
   - 식별한 미들웨어 솔루션들에 대해 솔루션의 시스템, 구분, 솔루션명, 버전, 제조사 등의 정보를 정리한 미들웨어 솔루션 목록을 작성한다.
   - 작성된 미들웨어 솔루션 목록은 이해관계자 등에게 전달하여 오류 및 누락을 확인하고 수정하다.
9. 미들웨어 솔루션 명세서 작성
   - 미들웨어 솔루션 명세서는 미들웨어 솔루션 목록의 미들웨어 솔루션별로 관련 정보들을 상세하게 기술하는 것이다.
   - 미들웨어 솔루션 제품 명칭 및 버전, 제품 사용 목적 등을 솔루션에 대한 제품안내서 및 설명 자료 등을 통해 검토한다.
   - 미들웨어 솔루션 제품에 대한 사용 환경과 특징 등을 솔루션 설명 자료나 관련 담당자를 통해 검토한다.
   - 미들웨어 솔루션이 지원하는 시스템 범위와 정상적인 서비스 제공을 위한 환경 구성, 제공 기능 등에 대한 제약사항이 존재하는지 제품안내서 및 기술 지원 담당자를 통해 검토한다.
   - 미들웨어 솔루션에 대한 상세 정보 및 제공 기능, 특징, 시스템 구성 환경 등에 대한 제약사항을 정리하여 솔루션에 대한 명세서를 작성한다.
